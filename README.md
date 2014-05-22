p5tools
=======
p5tools is a set of commands that performs common tasks when developing [Processing](http://processing.org) apps.

Commands
--------

### `p5tools.py init`
Usage: `p5tools.py init directory`

`init` creates the following directory structure:
	directory/
	directory/build
	directory/build/build.pde

`init` will create `directory/` and place everything inside. It can be an existing directory, but it has to be empty.

Aditionally, `init` will initialize `directory` as a git repository.

Installation
------------
Place p5tools.py in your $PATH.

What I do is create a `~/bin` directory (inside my home folder) and place my command line apps inside there. My PATH includes `~/bin` so it knows where to look for `p5tools.py`.

### Dependencies
This script uses the [scriptine](https://pypi.python.org/pypi/scriptine/0.2.0a2) module. You can installe it using PIP:
	pip install scriptine

Contact
-------
If you have any questions or comments, feel free to contact me via GitHub or email.