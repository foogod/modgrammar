import unittest
import sys
import re
from modgrammar import *
from modgrammar import OR_Operator
from modgrammar.util import RepeatingTuple
from . import util

###############################################################################
# These tests simply verify that the grammar_whitespace_required attribute gets
# set correctly on all forms of grammar constructs when they're created.
# (Similar to the tests in whitespace.py)
###############################################################################

# Note that the following always have grammar_whitespace = False normally, so
# there is no reason to check grammar_whitespace_required on these:
#  ("LITERAL('A')", LITERAL('A'), False),
#  ("L('A')", L('A'), False),
#  ("WORD('A')", WORD('A'), False),
#  ("ANY_EXCEPT('A')", ANY_EXCEPT('A'), False),
#  ("OR(L('A'), L('B'))", OR(L('A'), L('B')), False),
#  ("L('A') | L('B')", L('A') | L('B'), False),
#  ("OPTIONAL(L('A'))", OPTIONAL(L('A')), False),
#  ("EXCEPT(L('A'), L('B'))", EXCEPT(L('A'), L('B')), False),
#  ("ANY", ANY, False),
#  ("EOL", EOL, False),
#  ("EOF", EOF, False),
#  ("EMPTY", EMPTY, False),
#  ("REST_OF_LINE", REST_OF_LINE, False),
#  ("SPACE", SPACE, False),

class G_Default (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')

class G_Default_True (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')
  grammar_whitespace_required = True

class G_Default_False (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')
  grammar_whitespace_required = False

default_grammars = (
  ("G_Default", G_Default, False),
  ("G_Default_True", G_Default_True, True),
  ("G_Default_False", G_Default_False, False),
  ("GRAMMAR('A', 'B')", GRAMMAR('A', 'B'), False),
  ("G('A', 'B')", G('A', 'B'), False),
  ("REPEAT(L('A'))", REPEAT(L('A')), False),
  ("ZERO_OR_MORE(L('A'))", ZERO_OR_MORE(L('A')), False),
  ("ONE_OR_MORE(L('A'))", ONE_OR_MORE(L('A')), False),
  ("LIST_OF(L('A'), sep=L('A'))", LIST_OF(L('A'), sep=L('A')), False),

  # explicit False:
  ("GRAMMAR('A', whitespace_required=False)", GRAMMAR('A', whitespace_required=False), False),
  ("G('A', whitespace_required=False)", G('A', whitespace_required=False), False),
  ("LITERAL('A', whitespace_required=False)", LITERAL('A', whitespace_required=False), False),
  ("L('A', whitespace_required=False)", L('A', whitespace_required=False), False),
  ("WORD('A', whitespace_required=False)", WORD('A', whitespace_required=False), False),
  ("ANY_EXCEPT('A', whitespace_required=False)", ANY_EXCEPT('A', whitespace_required=False), False),
  ("OR(L('A'), L('B'), whitespace_required=False)", OR(L('A'), L('B'), whitespace_required=False), False),
  ("EXCEPT(L('A'), L('B'), whitespace_required=False)", EXCEPT(L('A'), L('B'), whitespace_required=False), False),
  ("REPEAT(L('A'), whitespace_required=False)", REPEAT(L('A'), whitespace_required=False), False),
  ("OPTIONAL(L('A'), whitespace_required=False)", OPTIONAL(L('A'), whitespace_required=False), False),
  ("ZERO_OR_MORE(L('A'), whitespace_required=False)", ZERO_OR_MORE(L('A'), whitespace_required=False), False),
  ("ONE_OR_MORE(L('A'), whitespace_required=False)", ONE_OR_MORE(L('A'), whitespace_required=False), False),
  ("LIST_OF(L('A'), sep=L('A'), whitespace_required=False)", LIST_OF(L('A'), sep=L('A'), whitespace_required=False), False),

  # explicit True:
  ("GRAMMAR('A', whitespace_required=True)", GRAMMAR('A', whitespace_required=True), True),
  ("G('A', whitespace_required=True)", G('A', whitespace_required=True), True),
  ("LITERAL('A', whitespace_required=True)", LITERAL('A', whitespace_required=True), True),
  ("L('A', whitespace_required=True)", L('A', whitespace_required=True), True),
  ("WORD('A', whitespace_required=True)", WORD('A', whitespace_required=True), True),
  ("ANY_EXCEPT('A', whitespace_required=True)", ANY_EXCEPT('A', whitespace_required=True), True),
  ("OR(L('A'), L('B'), whitespace_required=True)", OR(L('A'), L('B'), whitespace_required=True), True),
  ("EXCEPT(L('A'), L('B'), whitespace_required=True)", EXCEPT(L('A'), L('B'), whitespace_required=True), True),
  ("REPEAT(L('A'), whitespace_required=True)", REPEAT(L('A'), whitespace_required=True), True),
  ("OPTIONAL(L('A'), whitespace_required=True)", OPTIONAL(L('A'), whitespace_required=True), True),
  ("ZERO_OR_MORE(L('A'), whitespace_required=True)", ZERO_OR_MORE(L('A'), whitespace_required=True), True),
  ("ONE_OR_MORE(L('A'), whitespace_required=True)", ONE_OR_MORE(L('A'), whitespace_required=True), True),
  ("LIST_OF(L('A'), sep=L('A'), whitespace_required=True)", LIST_OF(L('A'), sep=L('A'), whitespace_required=True), True),
)

grammar_whitespace_required = False

class G_False (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')

class G_False_True (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')
  grammar_whitespace_required = True

class G_False_False (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')
  grammar_whitespace_required = False

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

  # explicit False:
  ("GRAMMAR('A', whitespace_required=False)", GRAMMAR('A', whitespace_required=False), False),
  ("G('A', whitespace_required=False)", G('A', whitespace_required=False), False),
  ("LITERAL('A', whitespace_required=False)", LITERAL('A', whitespace_required=False), False),
  ("L('A', whitespace_required=False)", L('A', whitespace_required=False), False),
  ("WORD('A', whitespace_required=False)", WORD('A', whitespace_required=False), False),
  ("ANY_EXCEPT('A', whitespace_required=False)", ANY_EXCEPT('A', whitespace_required=False), False),
  ("OR(L('A'), L('B'), whitespace_required=False)", OR(L('A'), L('B'), whitespace_required=False), False),
  ("EXCEPT(L('A'), L('B'), whitespace_required=False)", EXCEPT(L('A'), L('B'), whitespace_required=False), False),
  ("REPEAT(L('A'), whitespace_required=False)", REPEAT(L('A'), whitespace_required=False), False),
  ("OPTIONAL(L('A'), whitespace_required=False)", OPTIONAL(L('A'), whitespace_required=False), False),
  ("ZERO_OR_MORE(L('A'), whitespace_required=False)", ZERO_OR_MORE(L('A'), whitespace_required=False), False),
  ("ONE_OR_MORE(L('A'), whitespace_required=False)", ONE_OR_MORE(L('A'), whitespace_required=False), False),
  ("LIST_OF(L('A'), sep=L('A'), whitespace_required=False)", LIST_OF(L('A'), sep=L('A'), whitespace_required=False), False),

  # explicit True:
  ("GRAMMAR('A', whitespace_required=True)", GRAMMAR('A', whitespace_required=True), True),
  ("G('A', whitespace_required=True)", G('A', whitespace_required=True), True),
  ("LITERAL('A', whitespace_required=True)", LITERAL('A', whitespace_required=True), True),
  ("L('A', whitespace_required=True)", L('A', whitespace_required=True), True),
  ("WORD('A', whitespace_required=True)", WORD('A', whitespace_required=True), True),
  ("ANY_EXCEPT('A', whitespace_required=True)", ANY_EXCEPT('A', whitespace_required=True), True),
  ("OR(L('A'), L('B'), whitespace_required=True)", OR(L('A'), L('B'), whitespace_required=True), True),
  ("EXCEPT(L('A'), L('B'), whitespace_required=True)", EXCEPT(L('A'), L('B'), whitespace_required=True), True),
  ("REPEAT(L('A'), whitespace_required=True)", REPEAT(L('A'), whitespace_required=True), True),
  ("OPTIONAL(L('A'), whitespace_required=True)", OPTIONAL(L('A'), whitespace_required=True), True),
  ("ZERO_OR_MORE(L('A'), whitespace_required=True)", ZERO_OR_MORE(L('A'), whitespace_required=True), True),
  ("ONE_OR_MORE(L('A'), whitespace_required=True)", ONE_OR_MORE(L('A'), whitespace_required=True), True),
  ("LIST_OF(L('A'), sep=L('A'), whitespace_required=True)", LIST_OF(L('A'), sep=L('A'), whitespace_required=True), True),
)

grammar_whitespace_required = True

class G_True (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')

class G_True_True (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')
  grammar_whitespace_required = True

class G_True_False (Grammar):
  grammar = (ONE_OR_MORE('A'), 'B')
  grammar_whitespace_required = False

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

  # explicit False:
  ("GRAMMAR('A', whitespace_required=False)", GRAMMAR('A', whitespace_required=False), False),
  ("G('A', whitespace_required=False)", G('A', whitespace_required=False), False),
  ("LITERAL('A', whitespace_required=False)", LITERAL('A', whitespace_required=False), False),
  ("L('A', whitespace_required=False)", L('A', whitespace_required=False), False),
  ("WORD('A', whitespace_required=False)", WORD('A', whitespace_required=False), False),
  ("ANY_EXCEPT('A', whitespace_required=False)", ANY_EXCEPT('A', whitespace_required=False), False),
  ("OR(L('A'), L('B'), whitespace_required=False)", OR(L('A'), L('B'), whitespace_required=False), False),
  ("EXCEPT(L('A'), L('B'), whitespace_required=False)", EXCEPT(L('A'), L('B'), whitespace_required=False), False),
  ("REPEAT(L('A'), whitespace_required=False)", REPEAT(L('A'), whitespace_required=False), False),
  ("OPTIONAL(L('A'), whitespace_required=False)", OPTIONAL(L('A'), whitespace_required=False), False),
  ("ZERO_OR_MORE(L('A'), whitespace_required=False)", ZERO_OR_MORE(L('A'), whitespace_required=False), False),
  ("ONE_OR_MORE(L('A'), whitespace_required=False)", ONE_OR_MORE(L('A'), whitespace_required=False), False),
  ("LIST_OF(L('A'), sep=L('A'), whitespace_required=False)", LIST_OF(L('A'), sep=L('A'), whitespace_required=False), False),

  # explicit True:
  ("GRAMMAR('A', whitespace_required=True)", GRAMMAR('A', whitespace_required=True), True),
  ("G('A', whitespace_required=True)", G('A', whitespace_required=True), True),
  ("LITERAL('A', whitespace_required=True)", LITERAL('A', whitespace_required=True), True),
  ("L('A', whitespace_required=True)", L('A', whitespace_required=True), True),
  ("WORD('A', whitespace_required=True)", WORD('A', whitespace_required=True), True),
  ("ANY_EXCEPT('A', whitespace_required=True)", ANY_EXCEPT('A', whitespace_required=True), True),
  ("OR(L('A'), L('B'), whitespace_required=True)", OR(L('A'), L('B'), whitespace_required=True), True),
  ("EXCEPT(L('A'), L('B'), whitespace_required=True)", EXCEPT(L('A'), L('B'), whitespace_required=True), True),
  ("REPEAT(L('A'), whitespace_required=True)", REPEAT(L('A'), whitespace_required=True), True),
  ("OPTIONAL(L('A'), whitespace_required=True)", OPTIONAL(L('A'), whitespace_required=True), True),
  ("ZERO_OR_MORE(L('A'), whitespace_required=True)", ZERO_OR_MORE(L('A'), whitespace_required=True), True),
  ("ONE_OR_MORE(L('A'), whitespace_required=True)", ONE_OR_MORE(L('A'), whitespace_required=True), True),
  ("LIST_OF(L('A'), sep=L('A'), whitespace_required=True)", LIST_OF(L('A'), sep=L('A'), whitespace_required=True), True),
)

class WhitespaceRequiredTests (util.TestCase):

  def check_recursive(self, name, g, expected, expected_sub):
    if g.grammar_whitespace_required != expected:
      raise self.failureException("When testing {}: grammar_whitespace_required for {!r} is {!r}".format(name, g, g.grammar_whitespace_required))
    if issubclass(g, ListRepetition):
      if g.grammar[1].grammar_whitespace_required != expected:
        raise self.failureException("When testing {}: grammar_whitespace_required for {!r} is {!r}".format(name, g.grammar[1], g.grammar[1].grammar_whitespace_required))
      sub_list = [g.grammar[0], g.sep]
    else:
      sub_list = g.grammar
      if isinstance(sub_list, RepeatingTuple):
        sub_list = [g.grammar[0]]
        if len(g.grammar) > 1:
          sub_list.append(g.grammar[1])
    for sub_g in sub_list:
      if issubclass(sub_g, (Terminal, OR_Operator)):
        # Terminals (and OR constructs) always normally have grammar_whitespace
        # set to False
        self.check_recursive(name, sub_g, False, expected_sub)
      else:
        self.check_recursive(name, sub_g, expected_sub, expected_sub)

  def test_ws_default(self):
    for name, g, expected in default_grammars:
      self.check_recursive(name + " (module grammar_whitespace_required unset)", g, expected, False)

  def test_ws_modfalse(self):
    for name, g, expected in modfalse_grammars:
      self.check_recursive(name + " (module grammar_whitespace_required=False)", g, expected, False)

  def test_ws_modtrue(self):
    for name, g, expected in modtrue_grammars:
      self.check_recursive(name + " (module grammar_whitespace_required=True)", g, expected, True)


