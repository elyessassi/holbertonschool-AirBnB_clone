#!/usr/bin/python3
"""testing cases ( place )"""

from models.place import Place
import unittest


class testcases(unittest.TestCase):
	def testcase1(self):
		x = Place()
		self.assertTrue(isinstance(x.city_id, str))
		self.assertTrue(isinstance(x.user_id, str))
		self.assertTrue(isinstance(x.name, str))
		self.assertTrue(isinstance(x.description, str))
		self.assertTrue(isinstance(x.number_rooms, int))
		self.assertTrue(isinstance(x.number_bathrooms, int))
		self.assertTrue(isinstance(x.max_guest, int))
		self.assertTrue(isinstance(x.price_by_night, int))
		self.assertTrue(isinstance(x.latitude, float))
		self.assertTrue(isinstance(x.longitude, float))
		self.assertTrue(isinstance(x.amenity_ids, list))
