#!/usr/bin/python3
"""testing cases ( basemodel )"""

from models.base_model import BaseModel
import unittest


class testcases(unittest.TestCase):
    """testing cases"""
    def testcase1(self):
        """testing save"""
        test1 = BaseModel()
        old = test1.updated_at
        test1.save()
        new = test1.updated_at
        self.assertTrue(old != new)
    
    def testcase2(self):
        """testing __dict__"""
        test1 = BaseModel()
        dictionnary = test1.to_dict()
        self.assertAlmostEqual(dictionnary["id"], test1.id)
        self.assertAlmostEqual(dictionnary["created_at"], test1.created_at)
        self.assertAlmostEqual(dictionnary["updated_at"], test1.updated_at)
        self.assertAlmostEqual(dictionnary["__class__"], test1.__class__.__name__)
