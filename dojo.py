from room.room import Room,Office,LivingSpace


class Dojo():

	"""
	Provides implementation sequence for the application
	"""

	def __init__(self, name = 'Andela Nairobi'):
		Dojo.rooms = []

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

	