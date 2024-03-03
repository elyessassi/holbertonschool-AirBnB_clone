#!/usr/bin/python3
"""testing cases ( state )"""

from models.state import State
import unittest


class testcases(unittest.TestCase):
	def testcase1(self):
		x = State()
		self.assertTrue(isinstance(x.name, str))
