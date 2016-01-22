# Modgrammar #

Modgrammar is a general-purpose library for building language parsers and
interpreters using context-free grammar definitions in Python.  Language
parsing rules (grammars) are defined as standard Python classes, which can then
be used to parse and validate input strings or files into meaningful data
structures.  Possible applications range from simple input validation, to
complex expression evaluation, to full-fledged programming language parsing for
compilers or interpreters. 

## Features ##

* Pure-Python cross-platform design.
* Full Unicode support
* Grammars are defined using standard Python syntax.
* Supports arbitrarily complex grammars, including recursion.
* Defining a grammar automatically creates a working parser in the process (no
  compilation steps or lengthy startup times).
* Parse results contain full parse-tree information, including heirarchical
  tokenization of the input.
* Parse result objects can have custom methods, producing rich data objects.
* Modular grammar design supports distributing grammars as python library
  modules, combining grammars from multiple sources into larger grammars, and
  even parameterized grammar definitions.

## Updates ##

* 2016-01-22: Moved project to BitBucket from Google Code
* 2013-02-15: modgrammar-0.10 released
* 2013-01-11: modgrammar-0.9.1 released
* 2013-01-03: modgrammar-0.9 released
* 2011-12-22: modgrammar-0.8 released
* 2011-12-22: We have a new discussion group!
* 2011-04-12: modgrammar-0.7 released

## Useful Links ##

* Python Package Index Entry: http://pypi.python.org/pypi/modgrammar
* Current Documentation: http://packages.python.org/modgrammar
* Discussion Group: http://groups.google.com/group/modgrammar

