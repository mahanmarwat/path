Path: Path for Pretty People
============================

.. image:: https://readthedocs.org/projects/path/badge/?version=latest
  :target: https://readthedocs.org/projects/path/?badge=latest
  :alt: Documentation Status


Path provide highly **readable** API to access and manipulate both filesystem path and URL path.

	>>> p = path.Path('c:\\hello\world.py')
	>>> p.name
	'world'
	>>> p.ext
	'.py'
	>>> p = path.HttpPath('https://github.com/docopt/docopt')
	>>> p.path
	'/docopt/docopt'
	>>> p.name
	'world'
	>>> p.ext
	'.py'

Contents:
~~~~~~~~~

.. toctree::
   :maxdepth: 2
   :titlesonly:
   
   Overview <README>
   API <api>