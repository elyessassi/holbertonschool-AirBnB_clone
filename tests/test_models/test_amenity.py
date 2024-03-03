#!/usr/bin/python3
"""testing cases ( amenity )"""

from models.amenity import Amenity
import unittest


class testcases(unittest.TestCase):
	def testcase1(self):
		x = Amenity()
		self.assertTrue(isinstance(x.name, str))