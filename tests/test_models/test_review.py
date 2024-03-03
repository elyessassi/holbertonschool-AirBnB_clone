#!/usr/bin/python3
"""testing cases ( review )"""

from models.review import Review
import unittest


class testcases(unittest.TestCase):
	def testcase1(self):
		x = Review()
		self.assertTrue(isinstance(x.place_id, str))
		self.assertTrue(isinstance(x.user_id, str))
		self.assertTrue(isinstance(x.text, str))