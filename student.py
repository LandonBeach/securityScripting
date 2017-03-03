class Student():
	''' A model for student '''
	def __init__(self, first_name, last_name, id_num):
		self.f_name = None
		self.l_name = None
		self.id_num = None
		self.year = None
		self.courses = None
		self.status = None
		self.age = None
		self.major = None
		self.minor = None
		set_first_name(first_name)
		set_last_name(last_name)
		set_id_num(id_num)
		
		
	def set_first_name(self, first_name):
		try:
			self.f_name = first_name.lower()
		except AttributeError:
			print("ERROR: first_name argument is not a string.")
		
	def set_last_name(self, last_name):
		try:
			self.l_name = last_name.lower()
		except AttributeError:
			print("ERROR: last_name agrument is not a string.")
	
	def set_id_num(self, id_num):
		try:
			self.id_num = id_num if not isinstance(id_num, int) else raise TypeError
		except TypeError:
			print("ERROR: id_num argument is not an integer")
		
	def set_courses(self, *courses):
		''' Set the enrolled courses. '''
		self.courses = list(courses)
		
	def set_status(self, status):
		''' Set the current status. '''
		try:
			if status.lower() not in ('active', 'inactive', 'pending'):
				print("Invalid status for %s" % self.get_full_name())
			else:
				self.status = status
		except AttributeError:
			print("ERROR: status argument is not a string.")
		
	def set_year(self, year):
		''' Set the year. '''
		try:
			if year.lower() not in ('freshman', 'sophmore', 'junior', 'senior')
				print("Invalid year for %s" %s self.get_full_name())
			else:
				self.year = year
		except AttributeError:
			print("ERROR: year argument is not a string.")
		
	def set_age(self, age):
		''' Set the age '''
		try:
			if not isinstance(id_num, int):
				raise TypeError
		except TypeError:
			print("ERROR: age agrument is not an integer.")
			return
			
		if age < 0 or age >= 150:
			print("Invaid age for %s" % self.get_full_name())
			print("Age cannot be less than 0 or greater than 150.")
		else:
			self.age = age
			
		
	def set_major(self, *major):
		''' Set the major '''
		self.major = list(major)
		
	def set_minor(self, *minor):
		''' Set the minor '''
		self.minor = list(minor)
		
	def get_first_name(self):
		''' Return the first name '''
		return self.f_name
		
	def get_last_name(self):
		''' Return the last name '''
		return self.l_name
		
	def get_courses(self):
		''' Return a list of enrolled courses '''
		return self.courses
		
	def get_status(self):
		''' Return the status. '''
		return self.status
		
	def get_year(self):
		''' Return the year. '''
		return self.year
		
	def get_age(self):
		''' Return the age. '''
		return self.age
		
	def get_major(self):
		''' Return the major. '''
		return self.major
		
	def get_minor(self):
		''' Return the minor. '''
		return self.minor
		
	def get_ID(self):
		''' Return the ID '''
		return self.id_num
		
	def get_full_name(self):
		''' Return the first and last name together. '''
		return self.f_name.title() + " " + self.l_name.title()
	
