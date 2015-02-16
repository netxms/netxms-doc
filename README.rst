How to export GPL documentation
===============================

make clean html pdf

How to export GPL docs + extensions
===================================

MODULES=module1,module2,module3 make clean html pdf

File system structure
=====================

adminguide/ - Administrator guide for GPL build

conceptguide/ - Concept guide for GPL build

developguide/ - Developers guide for GPL build

All documents share the same root conf.py, while each one
have it's own override in their folders.

Non-GPL documentation should be placed in
source/extensions/MODULE_NAME/index.rst

Useful links
============

http://sphinx-doc.org/markup/para.html
http://sphinx-doc.org/markup/inline.html
http://sphinx-doc.org/markup/
