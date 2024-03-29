#!/usr/bin/python3
"""testing cases ( basemodel )"""

from models.base_model import BaseModel
from models import storage
import unittest
import os
import models


class testcases(unittest.TestCase):
    """testing cases"""
    def testcase1(self):
        """testing save"""
        test1 = BaseModel()
        old = test1.updated_at
        test1.save()
        new = test1.updated_at
        self.assertTrue(old != new)
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))


    def testcase2(self):
        """testing __dict__"""
        test1 = BaseModel()
        x = test1.__class__.__name__
        dictionnary = test1.__dict__.copy()
        testdictionnary = test1.to_dict()
        self.assertAlmostEqual(dictionnary["id"], test1.id)
        self.assertAlmostEqual(dictionnary["created_at"], test1.created_at)
        self.assertAlmostEqual(dictionnary["updated_at"], test1.updated_at)
        self.assertAlmostEqual(testdictionnary["__class__"], x)

    def testcase3(self):
        """testing __str__"""
        test1 = BaseModel()
        string = str(f"[{test1.__class__.__name__}] ")
        string = string + f"({test1.id}) {test1.__dict__}"
        self.assertEqual(test1.__str__(), string)
