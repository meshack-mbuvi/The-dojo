__author__ = 'Meshack Mbuvi'
__version__ = '1.0'

import unittest

from dojo import Dojo
from room.room import Room, Office, LivingSpace
from person.person import Person, Staff, Fellow

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

class PersonTests(unittest.TestCase):

	def setUp(self):

		self.dojo = Dojo()
		self.person_count1 = len(self.dojo.persons)
		self.fellow = self.dojo.add_person('Meshack','Mbuvi','fellow','y')
		
		self.fellow1 = self.dojo.add_person('Meshack','Mbu34vi','fellow')
		self.person_count2 = len(self.dojo.persons)

		self.staff = self.dojo.add_person('Meshack','Mbuvii','staff')
		self.person_count3 = len(self.dojo.persons)

		self.fellow0 = self.dojo.add_person('Meshack','Mbuvi','fellow','y')

	def test_fellow_created_successfully(self):
		self.assertEqual(self.person_count2 - self.person_count1, 1, msg = "Should create new Fellow object")

	def test_fellow_is_a_Fellow(self):
		self.assertTrue(isinstance(self.fellow,Fellow))

	def test_does_not_add_existing_person(self):
		self.assertTrue(self.fellow0 == None, msg = "Should not add existing person.")


	def test_fellow_is_a_person(self):
		self.assertTrue(isinstance(self.fellow, Person))

	def test_fellow_wants_accommodation_is_set(self):
		self.assertTrue(self.fellow.wants_accom == 'y', msg = 'Should set wants_accom attribute of Fellow object.')

	def test_staff_created_successfully(self):
		self.assertEqual(self.person_count3 - self.person_count2, 1, msg = "Should create new Staff object ")

	def test_staff_is_a_Staff(self):
		self.assertTrue(isinstance(self.staff, Staff))

	def test_staff_is_a_person(self):
		self.assertTrue(isinstance(self.staff, Person))

	def test_staff_not_allocated_livingspace(self):
		self.assertTrue(self.staff.allocated_livingspace == None, msg = 'A staff cannot be allocated living space.')

	def test_does_not_create_person_whose_name_has_digits(self):
		self.assertTrue(self.fellow1 == None, msg = "Names of person must be letters only.")

	def tearDown(self):

		self.dojo = None
		self.fellow = None
		self.fellow0 = None
		self.person_count1 = None
		self.person_count2 = None
		self.staff = None


if __name__ == '__main__':
	unittest.main()