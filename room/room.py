class Room(object):

	"""
	Create general features of a general room
	Each room has a certain capacity depending on its type(an office or a living room)
	"""

	def __init__(self):
		self.capacity = '';


class Office(Room):

	"""
	Add specific features to make a room an office.
	An office has a name and a space for maximum of 4 people.
	"""

	def __init__(self, rname):

		super(Office,self).__init__()
		self.name = rname #office name
		self.capacity = 4 #number of spaces per office
		self.occupants = [] #list to hold people allocated the room

class LivingSpace(Room):

	"""
	Add specific features to make a room a livingspace.
	An office has a name and a space for maximum of 6 people.
	"""

	def __init__(self, rname):
		
		super(LivingSpace,self).__init__()
		self.name = rname #office name
		self.capacity = 6 #number of spaces per office	
		