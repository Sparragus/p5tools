#!/usr/bin/env python

import os, subprocess

def init_command(directory):
	""" 
Initializes a Processing project.
This program will create a directory structure for working with Processing
inside the Sublime Text editor. This structure was suggested by 
Joshua Davis (http://joshuadavis.com).
Additionally, it will initialize the root directory with a git repository.

:param directory: where to create the project
    """

	base_directory = os.path.abspath(directory)

	print base_directory

	# Verify if the directory exists
	if os.path.exists(base_directory) :
		# Verify if directory is empty
		# if not empty...
		if not os.listdir( base_directory ) == []:
			print "Directory is not empty. Aborting..."
			return 1

	# If base_directory does not exists, create it in the current directory
	else:
		# print "Does not exist!"
		os.mkdir(base_directory)

	# Create build directory
	os.mkdir(base_directory + "/build")

	# Create build.pde inside ./build/ and initialize it with setup() and draw()
	with open(base_directory + "/build/build.pde", 'w') as f:
		f.write("""
void setup() {

}

void draw() {

}
				""")
		f.close()

	# Initialize a git repository at the base_directory
	if subprocess.call(["git", "init", base_directory]) == 0:
		# Git prints a message confirming it succesfully initialized a repository at the dir
		# it did it.
		pass
	else: 
		print "Couldn't initialize a git repository. Please verify that git is installed."

	print "Finished. Project is ready."
	# END - init

def install_command(package_name):
	"""
	Installs a package in the current directory.
	"""

	#END - install
	pass

# TODO: Remove scriptine dependency
if __name__ == '__main__':
    import scriptine
    scriptine.run()