from random import choice

from room.room import Office,LivingSpace
from person.person import Fellow, Staff


class Dojo():

	"""
	Provides implementation sequence for the application
	"""

	def __init__(self, name = 'Andela Nairobi'):
		self.name = name
		Dojo.rooms = []
		Dojo.persons = []


	def valid_name(self, room_name):
		#Check that the first three characters are not digits/numerals
		if len(room_name) < 3:
			return False 
		
		for char in room_name[:3]:
				if char.isdigit():
					print("{} is not a valid name" . format(room_name))
					return False

		#Also check that room with name room_name does not exist in the system
		for room in Dojo.rooms:
	    		if room.name == room_name:
	    			print("{} already exists in the system." . format(room_name))
	    			return False


		return True

	def valid_type(self, room_type):
		room = room_type.lower()

		#check that room_type is an office or a livingspace
		if room == 'office' or room == 'livingspace':
			return True

		print("A room can only be an office or a LivingSpace")
		return False

	def is_alpha(self, string):
		'''check that string contains letters only
		'''
		if string.isalpha():

			return True

		print('{} not a valid name.' . format(string))
		return False

	def is_valid(self, person_type):
		#check whether person_type is either a fellow or a staff

		if person_type.lower() == 'fellow' or person_type.lower() == 'staff':
			return True

		return False

	def create_room(self, room_type, room_name):
		'''
		creates a new room; an office or livingspace and gives it a name = room_name
		'''

		if self.valid_name(room_name) and self.valid_type(room_type):
			new_room = None
			if room_type.lower() =='office':
				new_room = Office(room_name)
				print("An office called {} has been successfully created!" . format(room_name))

			else:
				new_room = LivingSpace(room_name)
				print("A livingspace called {} has been successfully created!" . format(room_name))

			#Add the new_room to list holding all rooms in dojo
			Dojo.rooms.append(new_room)
			return new_room

	def allocate_room(self, person, room_type):
		#room_type == 'office', get allocate an office if its available
		if room_type.lower() == 'office':
			#get available offices
			avail_offices = [office for office in Dojo.rooms if len(office.occupants) < 4]
			if (len(avail_offices) > 0):
				office = choice(avail_offices)
				office.occupants.append(person)
				person.allocated_office = office.name

				print('{} has been allocated the office {}' . format(person.first_name, office.name) )
			else:
				print('No available office to allocate {}.' .format(person.first_name))


	def in_system(self, first_name, second_name):
		#get list of existing people from system
		in_system = [(person.first_name,person.second_name) for person in Dojo.persons]

		if (first_name,second_name) in in_system:
			return True

		return False


	def add_person(self,first_name, second_name,person_type, w = 'N'):
		'''Create a person object whose name is first_name second_name.
		w -> an optional argument, specifys whether the person wants accommodation allocation.
		person_type -> specifies whether person is a staff or a fellow
		'''

		#proceed if person names contain letters only and person_type is valid type
		if self.is_alpha(first_name) and self.is_alpha(second_name) and self.is_valid(person_type):
			if not (self.in_system(first_name, second_name)):
				if person_type.lower() == 'fellow':
				    #get reference to Fellow model
				    fellow = Fellow() 
				    #assign values to attributes of the reference
				    fellow.first_name = first_name
				    fellow.second_name = second_name
				    fellow.wants_accom = w

				    #Add the object to the list of persons
				    Dojo.persons.append(fellow)
				    print('Fellow {} {} has been successfully added.' . format(first_name, second_name))

				    #Allocate office
				    self.allocate_room(fellow,'office')

				    #allocate livingspace too
				    if (w.lower() == 'y'):
				    	self.allocate_room(fellow,'livingspace')

				    return fellow

				else:
					staff = Staff()
					staff.first_name = first_name
					staff.second_name = second_name
					Dojo.persons.append(staff)

					print('Staff {} {} has been successfully added.' . format(first_name, second_name))

					self.allocate_room(staff,'office')
					return staff
				print('{} {} already in system.' . format(first_name, second_name))
			


