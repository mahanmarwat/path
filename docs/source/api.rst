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

These can be used with the ``ispath`` function. i.e ``ispath(EXIST)``

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

.. function:: cwd()

	return current working directory.
	
.. function:: chd(path)

	change current working directory.

Properties as functions:
------------------------

.. function:: size(path)

	return size.
	
.. function:: atime(path)

	return access time.
	
.. function:: mtime(path)

	return modified time.
	
.. function:: ctime(path)

	return creation time.

Path Components as functions:
-----------------------------


.. function:: full(path)

	return full path (Absolute path).
	
.. function:: path(path)

	return given path.
	
.. function:: drive(path)

	return drive part.
	
.. function:: dir(path)

	return path without filename.
	
.. function:: filedir(path)

	return file dir.
	
.. function:: file(path)

	return name with extension.
	
.. function:: name(path)

	return name without extension.
	
.. function:: ext(path)

	return extension.

General path functions:
-----------------------

.. function:: join(path, path, [path, ...])

	join two or more paths.
	
.. function:: stat(path)

	return properties.
	
.. function:: list(path, pattern='')

	list contents of path.
	
.. function:: dirs(path, pattern='')

	list dirs.
	
.. function:: files(path, pattern='')

	list files.
	
.. function:: chprop(path, mode=None, times=None)

	change properties of a path.
	
.. function:: walk(path)

	walk path.
	
	.. note:: 
	
		This function is not yet implemented.

Conditional path functions:
---------------------------

.. function:: ispath(path, access)

	check path permission.
	
.. function:: isdir(path)

	check if path is a dir.
	
.. function:: isfile(path)

	check if path is a file.
	
.. function:: islink(path)

	check if path is a link.
	
.. function:: ismount(path)

	check if path is a mount.
	
.. function:: isempty(path)

	check weather the dir or file is empty.

High Level path functions:
--------------------------

.. function:: move(oldpath, newpath)
 
	move path.
	
.. function:: rename(oldpath, newpath)

	rename path.
	
.. function:: copy(oldpath, newpath)

	copy path.
	
.. function:: create(path, type='dir', mode=0o777)

	create path.
	
.. function:: delete(path)

	delete path.
	
	.. warning::

		This function will delete the file or dir, weather it is empty or not.
	
Classes
~~~~~~~

.. class:: Properties(path)

	Properties of a path.

	.. attribute:: size
	.. attribute:: atime
	.. attribute:: mtime
	.. attribute:: ctime
	
.. class:: Components(path)

	Components of a path.

	.. attribute:: full
	.. attribute:: path
	.. attribute:: drive
	.. attribute:: dir
	.. attribute:: filedir
	.. attribute:: file
	.. attribute:: name
	.. attribute:: ext
	
.. class:: Path(path)

	Path object, represent a path to OS file or dir.

	Path Components:
	
	.. attribute:: full
	.. attribute:: path
	.. attribute:: drive
	.. attribute:: dir
	.. attribute:: filedir
	.. attribute:: file
	.. attribute:: name
	.. attribute:: ext
	
	Path Properties:
	
	.. attribute:: size
	.. attribute:: atime
	.. attribute:: mtime
	.. attribute:: ctime
	
	General path methods:

	.. method:: join(path, [path, ...])

		join two or more paths.
		
	.. method:: stat()

		return properties.
		
	.. method:: list(pattern='')

		list contents of path.
		
	.. method:: dirs(pattern='')

		list dirs.
		
	.. method:: files(pattern='')

		list files.
		
	.. method:: chprop(mode=None, times=None)

		change properties of a path.
		
	.. method:: walk()

		walk path.
		
		.. note:: 
		
			This method is not yet implemented.
	
	Conditional path methods:

	.. method:: ispath(access)

		check path permission.
		
	.. method:: isdir()

		check if path is a dir.
		
	.. method:: isfile()

		check if path is a file.
		
	.. method:: islink()

		check if path is a link.
		
	.. method:: ismount()

		check if path is a mount.
		
	.. method:: isempty()

		check weather the dir or file is empty.
		
	High Level path methods:

	.. method:: move(newpath)
	 
		move path.
		
	.. method:: rename(newpath)

		rename path.
		
	.. method:: copy(newpath)

		copy path.
		
	.. method:: create(type='dir', mode=0o777)

		create path.
		
	.. method:: delete()

		delete path.
		
		.. warning::

			This method will delete the file or dir, weather it is empty or not.
	
.. class:: HttpPath(path)

	Path object, represent a path to URL.
	
	Subclass of ``Path``.
	
Exceptions:
~~~~~~~~~~~

.. exception:: PathError