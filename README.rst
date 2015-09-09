Path: Path for Pretty People
============================

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/mahanmarwat/path
   :target: https://gitter.im/mahanmarwat/path?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. image:: https://readthedocs.org/projects/path/badge/?version=latest
  :target: https://readthedocs.org/projects/path/?badge=latest
  :alt: Documentation Status


Path provide highly **readable** API to access and manipulate both filesystem path and URL path.

All operations are available at module level as functions.

    >>> import path
    >>> path.cwd() # return current working directory.
    >>> path.chd() # change current working directory.
    ...
    
Operations are available as ``Path`` object methods too.

    >>> p = path.Path('c:\\hello\world.py')
    >>> p.name
    'world'
    >>> p.ext
    '.py'
    >>> p.ispath(path.EXIST) # check path or file existence.
    >>> p.isempty() # whether the file or dir is empty.
    ...
    
Individual classes for readability.

    >>> comp = path.Components('c:\\hello\world.py')
    >>> comp.name
    'world'
    >>> comp.ext
    '.py'
    
Unlike other packages, path also work on **URL** too. Which ease web-scrapper coding.

    >>> p = path.HttpPath('https://github.com/docopt/docopt')
    >>> p.path
    '/docopt/docopt'
    >>> p.create() # will create dir or file according to args.
    ...

Features
--------

- Work both on path and URL
- Highly readable API
- Provide constants
- Operations are available as functions and methods
- Individual classes for everything

Installation
------------

    $ pip install https://github.com/mahanmarwat/path/archive/master.zip

Documentation
-------------

http://path.readthedocs.org

Check ``path.py`` which is self explanatory.

I am not pretty, can I still use it?
------------------------------------

Sorry No, LOL! Yes you can.

Contribute
----------

Give us a star.
