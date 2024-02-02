# coding: utf-8
#
# Copyright © 2012-2017 Ejwa Software. All rights reserved.
#
# This file is part of gitinspector.
#
# gitinspector is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gitinspector is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with gitinspector. If not, see <http://www.gnu.org/licenses/>.

from __future__ import division
from __future__ import unicode_literals
import bisect
import datetime
import multiprocessing
import os
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor

from .localization import N_
from . import extensions, filtering, format, interval, terminal

CHANGES_PER_THREAD = 200
NUM_THREADS = multiprocessing.cpu_count()

__thread_lock__ = threading.BoundedSemaphore(NUM_THREADS)
__changes_lock__ = threading.Lock()

class FileDiff(object):
	def __init__(self, string):
		commit_line = string.split()

		if commit_line.__len__() == 3:
			self.name = commit_line[2].strip()
			self.insertions = int(commit_line[0])
			self.deletions = int(commit_line[1])

	@staticmethod
	def is_filediff_line(string):
		if '|' in string or len(string) == 0:
			return False
		string = string.split()
		# skip binary changes
		if string[0] == '-':
			return False
		return string.__len__() == 3

	@staticmethod
	def get_extension(string):
		string = string.split("|")[0].strip().strip("{}").strip("\"").strip("'")
		return os.path.splitext(string)[1][1:]

	@staticmethod
	def get_filename(string):
		return string.split("|")[0].strip().strip("{}").strip("\"").strip("'")

	@staticmethod
	def is_valid_extension(string):
		extension = FileDiff.get_extension(string)

		for i in extensions.get():
			if (extension == "" and i == "*") or extension == i or i == '**':
				return True
		return False

class Commit(object):
	def __init__(self, string):
		# get rid of the double quotes
		string = string[1:-1]
		self.filediffs = []
		commit_line = string.split("|")

		if commit_line.__len__() == 5:
			self.timestamp = int(commit_line[1].strip())
			self.date = datetime.date.fromtimestamp(self.timestamp)
			self.sha = commit_line[2]
			self.author = commit_line[3].strip()
			self.email = commit_line[4].strip()

	def __lt__(self, other):
		return self.timestamp.__lt__(other.timestamp) # only used for sorting; we just consider the timestamp.

	def add_filediff(self, filediff):
		self.filediffs.append(filediff)

	def get_filediffs(self):
		return self.filediffs

	@staticmethod
	def get_author_and_email(string):
		commit_line = string.split("|")
		return (commit_line[3].strip(), commit_line[4].strip())

	@staticmethod
	def is_commit_line(string):
		return string.startswith('"COMMIT|')


class AuthorInfo(object):
	insertions = 0
	deletions = 0
	commits = 0


PROGRESS_TEXT = N_("Fetching and calculating primary statistics (1 of 2): {0:.0f}%")


class Changes(object):
	authors = {}
	authors_dateinfo = {}

	def __init__(self, repo, hard):
		worker_pool = ThreadPoolExecutor(max_workers=NUM_THREADS)
		self.commits = []
		if interval.get_start_ref() is not None:
			interval.set_ref(interval.get_start_ref())
		else:
			interval.set_ref("HEAD")
		# Fetch all commit stats
		git_log_p = subprocess.Popen(filter(None, ["git", "--no-pager", "log", "--reverse", "--no-merges", '--pretty="COMMIT|%ct|%H|%aN|%aE"',
									"--numstat", "--diff-algorithm=minimal",
									interval.get_since(), interval.get_until()] + (["-C", "-C", "-M"] if hard else []) + [interval.get_ref()]),
									bufsize=1, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		self.lines = [line.decode("utf-8", "replace").strip() for line in git_log_p.communicate()[0].splitlines()]
		git_log_p.stdout.close()

		if git_log_p.returncode != 0 or len(self.lines) == 0:
			return

		num_commits = 0
		start_idx = -1
		end_idx = -1
		futures = []
		print('Changes: analyzing commits from git log ({} rows)'.format(len(self.lines)))
		for i, entry in enumerate(self.lines):
			if Commit.is_commit_line(entry):
				num_commits += 1
				if start_idx == -1:
					start_idx = i
				else:
					end_idx = i
				if num_commits % (CHANGES_PER_THREAD + 1) == 0:
					futures.append(worker_pool.submit(self.process_commits, start_idx, end_idx))
					start_idx = end_idx
		else:
			futures.append(worker_pool.submit(self.process_commits, start_idx, len(self.lines)))

		print('Changes: finished submitting analytical jobs ({} commits)'.format(num_commits))

		worker_pool.shutdown()
		self.commits = sorted(self.commits)
		print('Changes: finished analyzing commits')

		if len(self.commits) > 0:
			if interval.has_interval():
				interval.set_ref(self.commits[-1].sha)

			self.first_commit_date = self.commits[0].date
			self.last_commit_date = self.commits[-1].date

	def __iadd__(self, other):
		try:
			self.authors.update(other.authors)
			self.authors_dateinfo.update(other.authors_dateinfo)

			for commit in other.commits:
				bisect.insort(self.commits, commit)
			if not self.commits and not other.commits:
				self.commits = []

			return self
		except AttributeError:
			return other

	def process_commits(self, start_idx, end_idx):
		commit = None
		found_valid_extension = False
		is_filtered = False

		for i in range(start_idx, end_idx):
			j = self.lines[i]

			if Commit.is_commit_line(j) or i == end_idx - 1:
				if found_valid_extension:
					self.commits.append(commit)

				found_valid_extension = False
				is_filtered = False
				commit = Commit(j)

				if Commit.is_commit_line(j) and \
						(filtering.set_filtered(commit.author, "author") or \
						 filtering.set_filtered(commit.email, "email") or \
						 filtering.set_filtered(commit.sha, "revision") or \
						 filtering.set_filtered(commit.sha, "message")):
					is_filtered = True

			if FileDiff.is_filediff_line(j) and not \
					filtering.set_filtered(FileDiff.get_filename(j)) and not is_filtered:
				extensions.add_located(FileDiff.get_extension(j))

				if FileDiff.is_valid_extension(j):
					found_valid_extension = True
					filediff = FileDiff(j)
					commit.add_filediff(filediff)

	def get_commits(self):
		return self.commits

	@staticmethod
	def modify_authorinfo(authors, key, commit):
		if authors.get(key, None) is None:
			authors[key] = AuthorInfo()

		if commit.get_filediffs():
			authors[key].commits += 1

		for j in commit.get_filediffs():
			authors[key].insertions += j.insertions
			authors[key].deletions += j.deletions

	def get_authorinfo_list(self):
		if not self.authors:
			for i in self.commits:
				Changes.modify_authorinfo(self.authors, (i.author, i.email), i)

		return self.authors

	def get_authordateinfo_list(self):
		if not self.authors_dateinfo:
			for i in self.commits:
				Changes.modify_authorinfo(self.authors_dateinfo, (i.date, i.author, i.email), i)

		return self.authors_dateinfo
