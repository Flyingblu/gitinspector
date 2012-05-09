# coding: utf-8
#
# Copyright © 2012 Ejwa Software. All rights reserved.
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

import os
import platform

__bold__ =  "\033[1m"
__normal__ =  "\033[0;0m"

def __get_size_windows__():
	res = None
	try:
		from ctypes import windll, create_string_buffer

		handler = windll.kernel32.GetStdHandle(-12) # stderr
		csbi = create_string_buffer(22)
		res = windll.kernel32.GetConsoleScreenBufferInfo(handler, csbi)
	except:
		return None

	if res:
		import struct
		(_, _, _, _, _, left, top, right, bottom, _, _) = struct.unpack("hhhhHhhhhhh", csbi.raw)
		sizex = right - left + 1
		sizey = bottom - top + 1
		return sizex, sizey
	else:
		return None

def __get_size_tput__():
	try:
		import subprocess
		proc = subprocess.Popen(["tput", "cols"], stdin = subprocess.PIPE, stdout = subprocess.PIPE)
		output = proc.communicate(input = None)
		cols = int(output[0])
		proc = subprocess.Popen(["tput", "lines"], stdin = subprocess.PIPE, stdout = subprocess.PIPE)
		output = proc.communicate(input = None)
		rows = int(output[0])
		return (cols, rows)
	except:
		return None

def __get_size_linux__():
	def ioctl_get_window_size(file_descriptor):
		try:
			import fcntl, termios, struct
			size = struct.unpack('hh', fcntl.ioctl(file_descriptor, termios.TIOCGWINSZ, '1234'))
		except:
			return None

		return size

	size = ioctl_get_window_size(0) or ioctl_get_window_size(1) or ioctl_get_window_size(2)

	if not size:
		try:
			file_descriptor = os.open(os.ctermid(), os.O_RDONLY)
			size = ioctl_get_window_size(file_descriptor)
			os.close(file_descriptor)
		except:
			pass
	if not size:
		try:
			size = (os.environ["LINES"], os.environ["COLUMNS"])
		except:
			return None

	return int(size[1]), int(size[0])

def skip_escapes(skip):
	if skip:
		global __bold__
		global __normal__
		__bold__ = ""
		__normal__ = ""

def printb(string):
	print __bold__ + string + __normal__

def get_size():
	current_os = platform.system()
	tuple_xy = None

	if current_os == 'Windows':
		tuple_xy = __get_size_windows__()
	if tuple_xy is None:
		tuple_xy = __get_size_tput__()
	if current_os == 'Linux' or current_os == 'Darwin' or  current_os.startswith('CYGWIN'):
		tuple_xy = __get_size_linux__()
	if tuple_xy is None:
		tuple_xy = (80, 25)

	return tuple_xy