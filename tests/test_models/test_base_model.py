#!/usr/bin/python3
"""testing cases ( basemodel )"""

from models.base_model import BaseModel
import unittest


class testcases(unittest.TestCase):
    """testing cases"""
    def testcase1(self):
        """testing save"""
        test1 = BaseModel()
        test1.save()
        self.assertTrue(test1.updated_at != test1.created_at)
