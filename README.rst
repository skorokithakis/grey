Grey: Black, but brighter, but not as bright as White (arbitrarily–inspired)
============================================================================

`Black <https://github.com/ambv/black>`_ is an amazing tool for auto–formatting
Python code in a style that I don't really care about, but I like consistency,
so I use it in all my projects.

It has **one** configuration option — to change its default line–length of ``88``
chars to, say, ``120``, like I like.

-----------

That is *exactly* what **grey** does. It invokes ``$ black --line-length 120`` on your behalf.


Usage
=====

::

    $ grey myapp.py
    reformatted myapp.py



Installation
============

::

	$ pipenv install white
	✨🍰✨
