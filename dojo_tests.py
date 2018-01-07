__author__ = 'Meshack Mbuvi'
__version__ = '1.0'

import unittest

from room.room import Room, Office, LivingSpace
from dojo import Dojo

class DojoTests(unittest.TestCase):

	def setUp(self):
		self.dojo = Dojo()
		self.office = self.dojo.create_room('office','Blue')
		self.office2 = self.dojo.create_room('office', '123bhk')
		self.livingspace = self.dojo.create_room('livingspace','Black')
		self.livingspace2 = self.dojo.create_room('livingspace', '123bhk')

	def test_dojo_creates_new_office(self):
		self.assertTrue(isinstance(self.office, Office), msg = "Should actually create an office")

	def test_rooms_added_to_system(self):
		self.assertTrue(self.office in self.dojo.rooms)

	def test_office_is_a_room(self):
		self.assertTrue(isinstance(self.office, Room), msg = "Should create an office of type Room")

	def test_office_has_a_name_blue(self):
		self.assertEqual(self.office.name,'Blue', msg = "should create an office called Blue")

	def test_office_capacity_is_4(self):
		self.assertEqual(self.office.capacity, 4, msg = "An office can only hold a maximum of 4 staffs or fellows or both")

	def test_office_not_a_livingspace(self):
		self.assertFalse(self.office is LivingSpace, msg = "An office cannot be a LivingSpace.")

	def test_office_name_does_not_start_with_numbers(self):
		self.assertTrue(self.office2 == None, msg = "First three characters of Room names should not be numerals")

	def test_dojo_creates_new_livingspace(self):
		self.assertTrue(isinstance(self.livingspace, LivingSpace), msg = "Should actually create a LivingSpace")

	def test_livingspace_is_a_room(self):
		self.assertTrue(isinstance(self.livingspace, Room), msg = "Should create an livingspace of type Room")

	def test_livingspace_has_a_name_black(self):
		self.assertEqual(self.livingspace.name,'Black', msg = "should create an livingspace called Black")

	def test_livingspace_capacity_is_6(self):
		self.assertEqual(self.livingspace.capacity, 6, msg = "A livingspace can only hold a maximum of 6 staffs or fellows or both")

	def test_livingspace_not_an_office(self):
		self.assertFalse(self.livingspace is Office, msg = "A livingspace cannot be an Office.")

	def test_livingspace_name_does_not_start_with_numbers(self):
		self.assertTrue(self.livingspace2 == None, msg = "First three characters of Room names should not be numerals")

	def tearDown(self):
		self.office = None
		self.office2 = None
		self.livingspace = None
		self.livingspace2 = None
		self.dojo = None


if __name__ == '__main__':
	unittest.main()