#!/usr/bin/env python

import os, sys

def init_command(directory):
	""" 
Initializes a Processing project.

This program will create a directory structure for working with Processing
inside the Sublime Text editor. This structure was suggested by 
Joshua Davis (http://joshuadavis.com).

Additionally, it will initialize the root directory with a git repository.
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
		f.write(
"""
void setup() {
	
}

void draw() {
	
}
"""
)
		f.close()

	# Finish!


if __name__ == '__main__':
    import scriptine
    scriptine.run()