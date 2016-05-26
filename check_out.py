import os
import sys
from subprocess import call

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def update(directory):
	child_directory = directory
	os.chdir(child_directory)
	call("svn up", shell=True)
	os.chdir("..")

def main(time):
	directories = get_immediate_subdirectories(time)
	os.chdir(time)
	# Go into each directory and SVN update.
	for directory in directories:
		update(directory)

if __name__ == '__main__':
	main(sys.argv[1])