# -*- coding: utf-8 -*-
# vi:et:ts=2:sw=2

import unittest
from modgrammar import *
from . import util

grammar_whitespace_mode = 'explicit'

###############################################################################
# Make sure that Modgrammar can correctly handle non-iso-8859-1 text in both
# grammars and inputs.
###############################################################################

class TestUnicodeInput (util.TestCase):
  def test_unicode_input(self):
    grammar = G('\u30d5', REPEAT('\u30eb' | WORD('\u30d0'), max=2))
    text = 'フバル'
    p = grammar.parser()
    o = p.parse_text(text)
    self.assertEqual(p.remainder(), '')
    self.assertEqual(o.string, text)
    self.assertIsInstance(o[0], Literal)
    self.assertEqual(len(o[0].string), 1)
    self.assertIsInstance(o[1][0], Word)
    self.assertEqual(len(o[1][0].string), 1)
    self.assertIsInstance(o[1][1], Literal)
    self.assertEqual(len(o[1][1].string), 1)

  def test_unicode_word_ranges(self):
    grammar = WORD('ぁ-ゟ', max=2)  # Should match (up to two of) any hirigana characters
    p = grammar.parser()
    o = p.parse_text('ふばる')
    self.assertEqual(p.remainder(), 'る')
    o = p.parse_text('ふバる', reset=True)
    self.assertEqual(p.remainder(), 'バる')

  def test_any_except(self):
    grammar = ANY_EXCEPT('ぁ-ゟ')  # Should match anything _except_ hirigana characters
    p = grammar.parser()
    o = p.parse_text('フバル', eof=True)
    self.assertEqual(p.remainder(), '')
    with self.assertRaises(ParseError):
      o = p.parse_text('ふ', reset=True)
    o = p.parse_text('バる', reset=True)
    self.assertEqual(p.remainder(), 'る')

###############################################################################
# Make sure that the default whitespace definitions correctly match all
# standard unicode whitespace characters (not just the basic ASCII ones)
###############################################################################

class TestUnicodeWS (util.TestCase):
  def test_WS_DEFAULT(self):
    grammar = G('A', 'B', whitespace=WS_DEFAULT, whitespace_mode='optional')
    o = grammar.parser().parse_text('A\u0009\u000a\u000b\u000c\u000d\u0020\u0085\u00a0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u2028\u2029\u202f\u205f\u3000B')

  def test_WS_NOEOL(self):
    grammar = G('A', 'B', whitespace=WS_NOEOL, whitespace_mode='optional')
    o = grammar.parser().parse_text('A\u0009\u0020\u00a0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000B')

  def test_WS_NOEOL_eolchars(self):
    grammar = G('A', 'B', whitespace=WS_NOEOL, whitespace_mode='optional')
    with self.assertRaises(ParseError):
      o = grammar.parser().parse_text('A\u000aB')
    with self.assertRaises(ParseError):
      o = grammar.parser().parse_text('A\u000bB')
    with self.assertRaises(ParseError):
      o = grammar.parser().parse_text('A\u000cB')
    with self.assertRaises(ParseError):
      o = grammar.parser().parse_text('A\u000dB')
    with self.assertRaises(ParseError):
      o = grammar.parser().parse_text('A\u0085B')
    with self.assertRaises(ParseError):
      o = grammar.parser().parse_text('A\u2028B')
    with self.assertRaises(ParseError):
      o = grammar.parser().parse_text('A\u2029B')

  def testEOL(self):
    grammar = G(REPEAT(EOL), 'A')  # Note: grammar_whitespace_mode = 'explicit'
    p = grammar.parser()
    # Make sure EOL matches all the possible EOL sequences properly
    o = p.parse_text('\u000a\u000b\u000c\u000d\u0085\u2028\u2029\r\n\n\rA')
    self.assertEqual(p.remainder(), '')
    self.assertEqual(len(o[0].elements), 9)
    # Check to make sure the parser counts lines the same way EOL does
    self.assertEqual(p.line, 9)
    # Check to make sure ParseErrors report lines the same way EOL does
    p.reset()
    try:
      o = p.parse_text('\u000a\u000b\u000c\u000d\u0085\u2028\u2029\r\n\n\rB')
    except ParseError as e:
      self.assertEqual(e.line, 9)

