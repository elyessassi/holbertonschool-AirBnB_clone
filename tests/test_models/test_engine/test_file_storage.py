#!/usr/bin/python3
"""testing cases ( file storage )"""

import models
from models.engine.file_storage import FileStorage
import unittest
import os

class testcases(unittest.TestCase):
	def testcase1(self):
		testobj = FileStorage()
		testobj.__file_path
		self.assertTrue(os.path.isfile(testobj))
		
