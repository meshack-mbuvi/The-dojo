class Person(object):

	"""
	Model general characteristics of a person. A person has a first and second names.Both types of Person have an allocated office space.
	"""

	def __init__(self):
		self.first_name = ''
		self.second_name = ''
		self.allocated_office = ''


class Staff(Person):

	def __init__(self):
		super(Person, self).__init__()
		self.allocated_livingspace = None
		

class Fellow(Person):
	'''subclasses a Person to model a fellow
	'''

	def __init__(self):
		super(Fellow, self).__init__()
		self.wants_accom = '' 
		self.allocated_livingspace = ''
