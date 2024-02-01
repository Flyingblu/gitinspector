import subprocess
import sys


def pull_branch(branch):
    git_pull_proc = subprocess.Popen(filter(None, ["git", "pull", "origin", branch]), bufsize=1,
                                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = git_pull_proc.communicate()[0].splitlines()
    git_pull_proc.stdout.close()
    if git_pull_proc.returncode != 0:
        print('\n'.join([line.decode("utf-8", "replace").strip() for line in output]))
        print('Pull branch failed, exiting...')
        sys.exit(git_pull_proc.returncode)
