import unittest
import sys
import re
from modgrammar import *
from modgrammar import OR_Operator
from modgrammar.util import RepeatingTuple
from . import util

grammar_whitespace_mode = 'optional'

WSRE = re.compile('-*')

###############################################################################
# These tests simply verify that the grammar_whitespace attribute gets set
# correctly on all forms of grammar constructs when they're created.  Actual
# testing of whether each form of grammar actually deals with whitespace
# correctly on parsing should be tested in the basic_grammar tests.
###############################################################################

# Note: The following grammars are predefined constants and thus don't have the
# ability to change their grammar_whitespace based on module setting, etc.
# This is ok, because these are all 'explicit' mode anyway (verified in
# whitespace_mode.py tests), so we don't care what their grammar_whitespace is
# set to:
#   WHITESPACE
#   ANY
#   EOL
#   EOF
#   EMPTY
#   REST_OF_LINE

class G_Default (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')

class G_Default_True (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')
  grammar_whitespace = True

class G_Default_False (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')
  grammar_whitespace = False

default_grammars = (
  ("G_Default", G_Default, True),
  ("G_Default_True", G_Default_True, True),
  ("G_Default_False", G_Default_False, False),
  ("GRAMMAR('A', 'B')", GRAMMAR('A', 'B'), True),
  ("G('A', 'B')", G('A', 'B'), True),
  ("REPEAT(L('A'))", REPEAT(L('A')), True),
  ("ZERO_OR_MORE(L('A'))", ZERO_OR_MORE(L('A')), True),
  ("ONE_OR_MORE(L('A'))", ONE_OR_MORE(L('A')), True),
  ("LIST_OF(L('A'), sep=L('A'))", LIST_OF(L('A'), sep=L('A')), True),
  ("LITERAL('A')", LITERAL('A'), True),
  ("L('A')", L('A'), True),
  ("WORD('A')", WORD('A'), True),
  ("ANY_EXCEPT('A')", ANY_EXCEPT('A'), True),
  ("OR(L('A'), L('B'))", OR(L('A'), L('B')), True),
  ("L('A') | L('B')", L('A') | L('B'), True),
  ("OPTIONAL(L('A'))", OPTIONAL(L('A')), True),
  ("EXCEPT(L('A'), L('B'))", EXCEPT(L('A'), L('B')), True),
  # GRAMMAR with a single element just returns that element, so the following
  # should resolve to LITERALs:
  ("GRAMMAR('A')", GRAMMAR('A'), True),
  ("G('A')", G('A'), True),

  # Override False:
  ("GRAMMAR('A', whitespace=False)", GRAMMAR('A', whitespace=False), False),
  ("G('A', whitespace=False)", G('A', whitespace=False), False),
  ("LITERAL('A', whitespace=False)", LITERAL('A', whitespace=False), False),
  ("L('A', whitespace=False)", L('A', whitespace=False), False),
  ("WORD('A', whitespace=False)", WORD('A', whitespace=False), False),
  ("ANY_EXCEPT('A', whitespace=False)", ANY_EXCEPT('A', whitespace=False), False),
  ("OR(L('A'), L('B'), whitespace=False)", OR(L('A'), L('B'), whitespace=False), False),
  ("EXCEPT(L('A'), L('B'), whitespace=False)", EXCEPT(L('A'), L('B'), whitespace=False), False),
  ("REPEAT(L('A'), whitespace=False)", REPEAT(L('A'), whitespace=False), False),
  ("OPTIONAL(L('A'), whitespace=False)", OPTIONAL(L('A'), whitespace=False), False),
  ("ZERO_OR_MORE(L('A'), whitespace=False)", ZERO_OR_MORE(L('A'), whitespace=False), False),
  ("ONE_OR_MORE(L('A'), whitespace=False)", ONE_OR_MORE(L('A'), whitespace=False), False),
  ("LIST_OF(L('A'), sep=L('A'), whitespace=False)", LIST_OF(L('A'), sep=L('A'), whitespace=False), False),

  # Override True:
  ("GRAMMAR('A', whitespace=True)", GRAMMAR('A', whitespace=True), True),
  ("G('A', whitespace=True)", G('A', whitespace=True), True),
  ("LITERAL('A', whitespace=True)", LITERAL('A', whitespace=True), True),
  ("L('A', whitespace=True)", L('A', whitespace=True), True),
  ("WORD('A', whitespace=True)", WORD('A', whitespace=True), True),
  ("ANY_EXCEPT('A', whitespace=True)", ANY_EXCEPT('A', whitespace=True), True),
  ("OR(L('A'), L('B'), whitespace=True)", OR(L('A'), L('B'), whitespace=True), True),
  ("EXCEPT(L('A'), L('B'), whitespace=True)", EXCEPT(L('A'), L('B'), whitespace=True), True),
  ("REPEAT(L('A'), whitespace=True)", REPEAT(L('A'), whitespace=True), True),
  ("OPTIONAL(L('A'), whitespace=True)", OPTIONAL(L('A'), whitespace=True), True),
  ("ZERO_OR_MORE(L('A'), whitespace=True)", ZERO_OR_MORE(L('A'), whitespace=True), True),
  ("ONE_OR_MORE(L('A'), whitespace=True)", ONE_OR_MORE(L('A'), whitespace=True), True),
  ("LIST_OF(L('A'), sep=L('A'), whitespace=True)", LIST_OF(L('A'), sep=L('A'), whitespace=True), True),
)

grammar_whitespace = False

class G_False (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')

class G_False_True (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')
  grammar_whitespace = True

class G_False_False (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')
  grammar_whitespace = False

modfalse_grammars = (
  ("G_False", G_False, False),
  ("G_False_True", G_False_True, True),
  ("G_False_False", G_False_False, False),
  ("GRAMMAR('A', 'B')", GRAMMAR('A', 'B'), False),
  ("G('A', 'B')", G('A', 'B'), False),
  ("REPEAT(L('A'))", REPEAT(L('A')), False),
  ("ZERO_OR_MORE(L('A'))", ZERO_OR_MORE(L('A')), False),
  ("ONE_OR_MORE(L('A'))", ONE_OR_MORE(L('A')), False),
  ("LIST_OF(L('A'), sep=L('A'))", LIST_OF(L('A'), sep=L('A')), False),
  ("LITERAL('A')", LITERAL('A'), False),
  ("L('A')", L('A'), False),
  ("WORD('A')", WORD('A'), False),
  ("ANY_EXCEPT('A')", ANY_EXCEPT('A'), False),
  ("OR(L('A'), L('B'))", OR(L('A'), L('B')), False),
  ("L('A') | L('B')", L('A') | L('B'), False),
  ("OPTIONAL(L('A'))", OPTIONAL(L('A')), False),
  ("EXCEPT(L('A'), L('B'))", EXCEPT(L('A'), L('B')), False),
  # GRAMMAR with a single element just returns that element, so the following
  # should resolve to LITERALs:
  ("GRAMMAR('A')", GRAMMAR('A'), False),
  ("G('A')", G('A'), False),

  # Override False:
  ("GRAMMAR('A', whitespace=False)", GRAMMAR('A', whitespace=False), False),
  ("G('A', whitespace=False)", G('A', whitespace=False), False),
  ("LITERAL('A', whitespace=False)", LITERAL('A', whitespace=False), False),
  ("L('A', whitespace=False)", L('A', whitespace=False), False),
  ("WORD('A', whitespace=False)", WORD('A', whitespace=False), False),
  ("ANY_EXCEPT('A', whitespace=False)", ANY_EXCEPT('A', whitespace=False), False),
  ("OR(L('A'), L('B'), whitespace=False)", OR(L('A'), L('B'), whitespace=False), False),
  ("EXCEPT(L('A'), L('B'), whitespace=False)", EXCEPT(L('A'), L('B'), whitespace=False), False),
  ("REPEAT(L('A'), whitespace=False)", REPEAT(L('A'), whitespace=False), False),
  ("OPTIONAL(L('A'), whitespace=False)", OPTIONAL(L('A'), whitespace=False), False),
  ("ZERO_OR_MORE(L('A'), whitespace=False)", ZERO_OR_MORE(L('A'), whitespace=False), False),
  ("ONE_OR_MORE(L('A'), whitespace=False)", ONE_OR_MORE(L('A'), whitespace=False), False),
  ("LIST_OF(L('A'), sep=L('A'), whitespace=False)", LIST_OF(L('A'), sep=L('A'), whitespace=False), False),

  # Override True:
  ("GRAMMAR('A', whitespace=True)", GRAMMAR('A', whitespace=True), True),
  ("G('A', whitespace=True)", G('A', whitespace=True), True),
  ("LITERAL('A', whitespace=True)", LITERAL('A', whitespace=True), True),
  ("L('A', whitespace=True)", L('A', whitespace=True), True),
  ("WORD('A', whitespace=True)", WORD('A', whitespace=True), True),
  ("ANY_EXCEPT('A', whitespace=True)", ANY_EXCEPT('A', whitespace=True), True),
  ("OR(L('A'), L('B'), whitespace=True)", OR(L('A'), L('B'), whitespace=True), True),
  ("EXCEPT(L('A'), L('B'), whitespace=True)", EXCEPT(L('A'), L('B'), whitespace=True), True),
  ("REPEAT(L('A'), whitespace=True)", REPEAT(L('A'), whitespace=True), True),
  ("OPTIONAL(L('A'), whitespace=True)", OPTIONAL(L('A'), whitespace=True), True),
  ("ZERO_OR_MORE(L('A'), whitespace=True)", ZERO_OR_MORE(L('A'), whitespace=True), True),
  ("ONE_OR_MORE(L('A'), whitespace=True)", ONE_OR_MORE(L('A'), whitespace=True), True),
  ("LIST_OF(L('A'), sep=L('A'), whitespace=True)", LIST_OF(L('A'), sep=L('A'), whitespace=True), True),
)

grammar_whitespace = True

class G_True (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')

class G_True_True (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')
  grammar_whitespace = True

class G_True_False (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')
  grammar_whitespace = False

modtrue_grammars = (
  ("G_True", G_True, True),
  ("G_True_True", G_True_True, True),
  ("G_True_False", G_True_False, False),
  ("GRAMMAR('A', 'B')", GRAMMAR('A', 'B'), True),
  ("G('A', 'B')", G('A', 'B'), True),
  ("REPEAT(L('A'))", REPEAT(L('A')), True),
  ("ZERO_OR_MORE(L('A'))", ZERO_OR_MORE(L('A')), True),
  ("ONE_OR_MORE(L('A'))", ONE_OR_MORE(L('A')), True),
  ("LIST_OF(L('A'), sep=L('A'))", LIST_OF(L('A'), sep=L('A')), True),
  ("LITERAL('A')", LITERAL('A'), True),
  ("L('A')", L('A'), True),
  ("WORD('A')", WORD('A'), True),
  ("ANY_EXCEPT('A')", ANY_EXCEPT('A'), True),
  ("OR(L('A'), L('B'))", OR(L('A'), L('B')), True),
  ("L('A') | L('B')", L('A') | L('B'), True),
  ("OPTIONAL(L('A'))", OPTIONAL(L('A')), True),
  ("EXCEPT(L('A'), L('B'))", EXCEPT(L('A'), L('B')), True),
  # GRAMMAR with a single element just returns that element, so the following
  # should resolve to LITERALs:
  ("GRAMMAR('A')", GRAMMAR('A'), True),
  ("G('A')", G('A'), True),

  # Override False:
  ("GRAMMAR('A', whitespace=False)", GRAMMAR('A', whitespace=False), False),
  ("G('A', whitespace=False)", G('A', whitespace=False), False),
  ("LITERAL('A', whitespace=False)", LITERAL('A', whitespace=False), False),
  ("L('A', whitespace=False)", L('A', whitespace=False), False),
  ("WORD('A', whitespace=False)", WORD('A', whitespace=False), False),
  ("ANY_EXCEPT('A', whitespace=False)", ANY_EXCEPT('A', whitespace=False), False),
  ("OR(L('A'), L('B'), whitespace=False)", OR(L('A'), L('B'), whitespace=False), False),
  ("EXCEPT(L('A'), L('B'), whitespace=False)", EXCEPT(L('A'), L('B'), whitespace=False), False),
  ("REPEAT(L('A'), whitespace=False)", REPEAT(L('A'), whitespace=False), False),
  ("OPTIONAL(L('A'), whitespace=False)", OPTIONAL(L('A'), whitespace=False), False),
  ("ZERO_OR_MORE(L('A'), whitespace=False)", ZERO_OR_MORE(L('A'), whitespace=False), False),
  ("ONE_OR_MORE(L('A'), whitespace=False)", ONE_OR_MORE(L('A'), whitespace=False), False),
  ("LIST_OF(L('A'), sep=L('A'), whitespace=False)", LIST_OF(L('A'), sep=L('A'), whitespace=False), False),

  # Override True:
  ("GRAMMAR('A', whitespace=True)", GRAMMAR('A', whitespace=True), True),
  ("G('A', whitespace=True)", G('A', whitespace=True), True),
  ("LITERAL('A', whitespace=True)", LITERAL('A', whitespace=True), True),
  ("L('A', whitespace=True)", L('A', whitespace=True), True),
  ("WORD('A', whitespace=True)", WORD('A', whitespace=True), True),
  ("ANY_EXCEPT('A', whitespace=True)", ANY_EXCEPT('A', whitespace=True), True),
  ("OR(L('A'), L('B'), whitespace=True)", OR(L('A'), L('B'), whitespace=True), True),
  ("EXCEPT(L('A'), L('B'), whitespace=True)", EXCEPT(L('A'), L('B'), whitespace=True), True),
  ("REPEAT(L('A'), whitespace=True)", REPEAT(L('A'), whitespace=True), True),
  ("OPTIONAL(L('A'), whitespace=True)", OPTIONAL(L('A'), whitespace=True), True),
  ("ZERO_OR_MORE(L('A'), whitespace=True)", ZERO_OR_MORE(L('A'), whitespace=True), True),
  ("ONE_OR_MORE(L('A'), whitespace=True)", ONE_OR_MORE(L('A'), whitespace=True), True),
  ("LIST_OF(L('A'), sep=L('A'), whitespace=True)", LIST_OF(L('A'), sep=L('A'), whitespace=True), True),
)

grammar_whitespace = WSRE

class G_WSRE (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')

class G_WSRE_True (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')
  grammar_whitespace = True

class G_WSRE_False (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')
  grammar_whitespace = False

modwsre_grammars = (
  ("G_WSRE", G_WSRE, WSRE),
  ("G_WSRE_True", G_WSRE_True, True),
  ("G_WSRE_False", G_WSRE_False, False),
  ("GRAMMAR('A', 'B')", GRAMMAR('A', 'B'), WSRE),
  ("G('A', 'B')", G('A', 'B'), WSRE),
  ("REPEAT(L('A'))", REPEAT(L('A')), WSRE),
  ("ZERO_OR_MORE(L('A'))", ZERO_OR_MORE(L('A')), WSRE),
  ("ONE_OR_MORE(L('A'))", ONE_OR_MORE(L('A')), WSRE),
  ("LIST_OF(L('A'), sep=L('A'))", LIST_OF(L('A'), sep=L('A')), WSRE),
  ("LITERAL('A')", LITERAL('A'), WSRE),
  ("L('A')", L('A'), WSRE),
  ("WORD('A')", WORD('A'), WSRE),
  ("ANY_EXCEPT('A')", ANY_EXCEPT('A'), WSRE),
  ("OR(L('A'), L('B'))", OR(L('A'), L('B')), WSRE),
  ("L('A') | L('B')", L('A') | L('B'), WSRE),
  ("EXCEPT(L('A'), L('B'))", EXCEPT(L('A'), L('B')), WSRE),
  # GRAMMAR with a single element just returns that element, so the following
  # should resolve to LITERALs:
  ("GRAMMAR('A')", GRAMMAR('A'), WSRE),
  ("G('A')", G('A'), WSRE),

  # Override False:
  ("GRAMMAR('A', whitespace=False)", GRAMMAR('A', whitespace=False), False),
  ("G('A', whitespace=False)", G('A', whitespace=False), False),
  ("LITERAL('A', whitespace=False)", LITERAL('A', whitespace=False), False),
  ("L('A', whitespace=False)", L('A', whitespace=False), False),
  ("WORD('A', whitespace=False)", WORD('A', whitespace=False), False),
  ("ANY_EXCEPT('A', whitespace=False)", ANY_EXCEPT('A', whitespace=False), False),
  ("OR(L('A'), L('B'), whitespace=False)", OR(L('A'), L('B'), whitespace=False), False),
  ("EXCEPT(L('A'), L('B'), whitespace=False)", EXCEPT(L('A'), L('B'), whitespace=False), False),
  ("REPEAT(L('A'), whitespace=False)", REPEAT(L('A'), whitespace=False), False),
  ("OPTIONAL(L('A'), whitespace=False)", OPTIONAL(L('A'), whitespace=False), False),
  ("ZERO_OR_MORE(L('A'), whitespace=False)", ZERO_OR_MORE(L('A'), whitespace=False), False),
  ("ONE_OR_MORE(L('A'), whitespace=False)", ONE_OR_MORE(L('A'), whitespace=False), False),
  ("LIST_OF(L('A'), sep=L('A'), whitespace=False)", LIST_OF(L('A'), sep=L('A'), whitespace=False), False),

  # Override True:
  ("GRAMMAR('A', whitespace=True)", GRAMMAR('A', whitespace=True), True),
  ("G('A', whitespace=True)", G('A', whitespace=True), True),
  ("LITERAL('A', whitespace=True)", LITERAL('A', whitespace=True), True),
  ("L('A', whitespace=True)", L('A', whitespace=True), True),
  ("WORD('A', whitespace=True)", WORD('A', whitespace=True), True),
  ("ANY_EXCEPT('A', whitespace=True)", ANY_EXCEPT('A', whitespace=True), True),
  ("OR(L('A'), L('B'), whitespace=True)", OR(L('A'), L('B'), whitespace=True), True),
  ("EXCEPT(L('A'), L('B'), whitespace=True)", EXCEPT(L('A'), L('B'), whitespace=True), True),
  ("REPEAT(L('A'), whitespace=True)", REPEAT(L('A'), whitespace=True), True),
  ("OPTIONAL(L('A'), whitespace=True)", OPTIONAL(L('A'), whitespace=True), True),
  ("ZERO_OR_MORE(L('A'), whitespace=True)", ZERO_OR_MORE(L('A'), whitespace=True), True),
  ("ONE_OR_MORE(L('A'), whitespace=True)", ONE_OR_MORE(L('A'), whitespace=True), True),
  ("LIST_OF(L('A'), sep=L('A'), whitespace=True)", LIST_OF(L('A'), sep=L('A'), whitespace=True), True),
)

class WhitespaceModeTestCase (util.TestCase):
  def __init__(self, module_setting, name, grammar, expected, modset_str=None):
    util.TestCase.__init__(self, 'perform_test')
    if module_setting is None:
      self.module_setting = True
      self.module_setting_str = '(unset)'
    else:
      self.module_setting = module_setting
      self.module_setting_str = repr(module_setting)
    if modset_str is not None:
      self.module_setting_str = modset_str
    self.name = name
    self.grammar = grammar
    self.expected = expected

  def __str__(self):
    return "grammar_whitespace={}: {}".format(self.module_setting_str, self.name)

  def perform_test(self):
    self.check_recursive("{} (module grammar_whitespace={})".format(self.name, self.module_setting_str), self.grammar, self.expected, self.module_setting)

  def check_recursive(self, name, g, expected, expected_sub):
    if g.grammar_whitespace_mode != 'explicit':
      if g.grammar_whitespace != expected:
        raise self.failureException("When testing {}: grammar_whitespace for {!r} is {!r}".format(name, g, g.grammar_whitespace))
    if issubclass(g, ListRepetition):
      if g.grammar[1].grammar_whitespace != expected:
        raise self.failureException("When testing {}: grammar_whitespace for {!r} is {!r}".format(name, g.grammar[1], g.grammar[1].grammar_whitespace))
      sub_list = [g.grammar[0], g.sep]
    else:
      sub_list = g.grammar
      if isinstance(sub_list, RepeatingTuple):
        sub_list = [g.grammar[0]]
        if len(g.grammar) > 1:
          sub_list.append(g.grammar[1])
    for sub_g in sub_list:
      self.check_recursive(name, sub_g, expected_sub, expected_sub)

def load_tests(loader, tests, pattern):
  for name, g, expected in default_grammars:
    tests.addTest(WhitespaceModeTestCase(None, name, g, expected))
  for name, g, expected in modfalse_grammars:
    tests.addTest(WhitespaceModeTestCase(False, name, g, expected))
  for name, g, expected in modtrue_grammars:
    tests.addTest(WhitespaceModeTestCase(True, name, g, expected))
  for name, g, expected in modwsre_grammars:
    tests.addTest(WhitespaceModeTestCase(WSRE, name, g, expected, 'WSRE'))
  return tests

###############################################################################
# The following tests the use of a custom regular expression for
# grammar_whitespace
###############################################################################

grammar_whitespace = True

class WSNormGrammar (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B', 'C')

grammar_whitespace = WSRE

class WSREGrammar (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B', 'C')

class WSMixGrammar (Grammar):
  grammar = (ONE_OR_MORE('A', whitespace=True), 'B', 'C')

class TestWSNorm (util.BasicGrammarTestCase):
  def setUp(self):
    self.grammar = WSNormGrammar
    self.grammar_name = "WSNormGrammar"
    self.grammar_details = "(REPEAT(L('A')), L('B'), L('C'))"
    self.subgrammar_types = (Repetition, Literal, Literal)
    self.terminal = False
    self.check_min_max = False
    self.matches = ('ABC', 'AABC', 'A A B C')
    self.fail_matches = ('A-BC', 'A-ABC', 'AB-C')

class TestWSRE (util.BasicGrammarTestCase):
  ws_strs = ('-',)
  def setUp(self):
    self.grammar = WSREGrammar
    self.grammar_name = "WSREGrammar"
    self.grammar_details = "(REPEAT(L('A')), L('B'), L('C'))"
    self.subgrammar_types = (Repetition, Literal, Literal)
    self.terminal = False
    self.check_min_max = False
    self.matches = ('ABC', 'AABC', 'A-A-B-C', 'A--A--B--C')
    self.fail_matches = ('A BC', 'A ABC', 'AB C')

class TestWSMix (util.BasicGrammarTestCase):
  ws_strs = (' ', '-')
  def setUp(self):
    self.grammar = WSMixGrammar
    self.grammar_name = "WSMixGrammar"
    self.grammar_details = "(REPEAT(L('A')), L('B'), L('C'))"
    self.subgrammar_types = (Repetition, Literal, Literal)
    self.terminal = False
    self.check_min_max = False
    self.matches = ('ABC', 'AABC', 'A-BC', 'AA-B-C', 'A A-B-C', 'A  ABC')
    self.fail_matches = ('A BC', 'A-ABC', 'AB C')

