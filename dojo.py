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

		return string.isalpha()

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

	def add_person(self,first_name, second_name,person_type, w = 'N'):
		'''Create a person object whose name is first_name second_name.
		w -> an optional argument, specifys whether the person wants accommodation allocation.
		person_type -> specifies whether person is a staff or a fellow
		'''

		#proceed if person names contain letters only and person_type is valid type
		if self.is_alpha(first_name) and self.is_alpha(second_name) and self.is_valid(person_type):
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
				return fellow

			else:
				staff = Staff()
				staff.first_name = first_name
				staff.second_name = second_name

				Dojo.persons.append(staff)

				print('Staff {} {} has been successfully added.' . format(first_name, second_name))
				return staff


