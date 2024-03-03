#!/usr/bin/python3
"""testing cases ( city )"""

from models.city import City
import unittest


class testcases(unittest.TestCase):
	def testcase1(self):
		x = City()
		self.assertTrue(isinstance(x.name, str))
		self.assertTrue(isinstance(x.state_id, str))