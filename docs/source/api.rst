API
===

Constants
~~~~~~~~~~

Properties constants:
---------------------
::

	SIZE  = 6 # stat.ST_SIZE
	ATIME = 7 # stat.ST_ATIME
	MTIME = 8 # stat.ST_MTIME
	CTIME = 9 # stat.ST_CTIME

Access constants:
-----------------
::

	EXIST      = 0 # os.F_OK
	EXECUTABLE = 1 # os.X_OK
	WRITABLE   = 2 # os.W_OK
	READABLE   = 4 # os.R_OK

Separators constants:
---------------------
::

	CURDIR  = os.curdir
	PARDIR  = os.pardir
	PATHSEP = os.pathsep
	DIRSEP  = os.sep
	EXTSEP  = os.extsep
	
Functions
~~~~~~~~~

General functions:
------------------
::

	cwd # return current working directory.
	chd # change current working directory.

Properties as functions:
------------------------
::

	size  # return size.
	atime # return access time.
	mtime # return modified time.
	ctime # return creation time.

Path Components as functions:
-----------------------------
::

	full     # Full path (Absolute path)
	#path    # Given path
	drive    # Drive part
	dir      # Path without filename
	filedir  # File parent dir
	file     # Name with extension
	name     # Name without extension
	ext      # Extension

General path functions:
-----------------------
::

	join   # join two or more paths.
	stat   # return properties.
	list   # list contents of path.
	dirs   # list dirs.
	files  # list files.
	chprop # change properties of a path.
	walk   # walk path.

Conditional path functions:
---------------------------
::

	ispath  # check path permission.
	isdir   # check if path is a dir.
	isfile  # check if path is a file.
	islink  # check if path is a link.
	ismount # check if path is a mount.
	isempty # check weather the dir or file is empty.

High Level path functions:
--------------------------
::

	move   # move path.
	rename # rename path.
	copy   # copy path.
	create # create path.
	delete # delete path.
	
Classes
~~~~~~~