class Student():
	''' A model for a student '''
	def __init__(self, first_name, last_name, id_num):
		# Set the default values for all of the attributes.
		self.set_first_name(first_name)
		self.set_last_name(last_name)
		self.set_id_num(id_num)
		self.year = None
		self.courses = None
		self.status = None
		self.age = None
		self.major = None
		self.minor = None
		
	def set_first_name(self, first_name):
		''' This method takes a string and sets the first name of the student. '''
		try:
			# If the .lower() function doesn't work, it'll raise an AttributeError. This means first_name wasn't a string.
			self.f_name = first_name.lower()
		except AttributeError:
			# Tell the user that they didn't pass a string agrument and keep the original value.
			print("ERROR: first_name argument is not a string.")
			print("\tfirst_name is unchanged.")
		
	def set_last_name(self, last_name):
		''' This method takes a string and sets the last name of the student. '''
		try:
			# If the .lower() function doesn't work, it'll raise an AttributeError. This means last_name wasn't a string.
			self.l_name = last_name.lower()
		except AttributeError:
			# Tell the user that they didn't pass a string agrument and keep the original value.
			print("ERROR: last_name agrument is not a string.")
			print("\tlast_name is unchanged.")
	
	def set_id_num(self, id_num):
		''' This method takes an ID number as either an integer or string and set the ID number of the student. '''
		# Check to see if id_num is either an integer or string. If so, set the id_num of the student.
		if isinstance(id_num, int) or isinstance(id_num, str):
			self.id_num = id_num
		# We recieved an invalid argument. Notify the user and return, keeping the original value.
		else:
			print("ERROR: id_num argument is not an integer or string.")
			return
		
	def set_courses(self, *courses):
		''' This method sets the list of courses the student is currently taking. '''
		self.courses = list(courses)
		
	def set_status(self, status):
		''' This method sets the current status of the student. Status must be either "active", "inactive", or "pending". '''
		try:
			# If the .lower() function doesn't work, it'll raise an AttributeError. This means the status wasn't a string.
			# If the status is not "active", "inactive", or "pending" then notify the user and keep the original value.
			if status.lower() not in ('active', 'inactive', 'pending'):
				print("Invalid status for %s" % self.get_full_name())
				print("\tstatus is unchanged.")
			else:
				# We recieved valid arguments. Set the status.
				self.status = status.lower()
		except AttributeError:
			# Tell the user that they didn't pass a string agrument and keep the original value.
			print("ERROR: status argument is not a string.")
			print("\tstatus is unchanged.")
		
	def set_year(self, year):
		''' This method sets the year of the student. The year must be either "freshman", "sophomore", "junior", or "senior". '''
		try:
			# If the .lower() function doesn't work, it'll raise an AttributeError. This means the year wasn't a string.
			# If the status is not "freshman", "sophomore", "junior", or "senior" then notify the user and keep the original value.
			if year.lower() not in ('freshman', 'sophmore', 'junior', 'senior'):
				print("Invalid year for %s" % self.get_full_name())
				print("\tyear is unchanged.")
			else:
				# We recieved valid arguments. Set the year.
				self.year = year.lower()
		except AttributeError:
			# Tell the user that they didn't pass a string agrument and keep the original value.
			print("ERROR: year argument is not a string.")
			print("\tyear is unchanged.")
			
	def set_age(self, age):
		''' This method sets the current age of the student. The age must be between 0 and 150. '''
		try:
			# Check to see if the age argument is an integer. If not, raise a TypeError.
			if not isinstance(age, int):
				raise TypeError
		except TypeError:
			# The age argument was not an integer. Notify the user and keep the original value.
			print("ERROR: age agrument is not an integer.")
			print("\tage is unchanged.")
			return
		
		# Check to see if the age is between 0 and 150.
		if age < 0 or age >= 150:
			# Notify the user that the age is invalid. Keep the original value.
			print("Invaid age for %s" % self.get_full_name())
			print("Age cannot be less than 0 or greater than 150.")
			print("\tage is unchanged.")
		else:
			# We recieved a valid agrument. Set the age.
			self.age = age
		
	def set_major(self, *major):
		''' This method sets a list of majors. '''
		self.major = list(major)
		
	def set_minor(self, *minor):
		''' This method sets a list of minors. '''
		self.minor = list(minor)
		
	def get_first_name(self):
		''' This method returns the first name of the student as a string. '''
		return self.f_name
		
	def get_last_name(self):
		''' This method returns the last name of the student as a string. '''
		return self.l_name
		
	def get_courses(self):
		''' This method returns a list of currently enrolled courses. '''
		return self.courses
		
	def get_status(self):
		''' This method returns the status of the student as a string. '''
		return self.status
		
	def get_year(self):
		''' This method returns the year of the student as a string. '''
		return self.year
		
	def get_age(self):
		''' This method returns the age of the student. '''
		return self.age
		
	def get_major(self):
		''' This method returns a list of majors. '''
		return self.major
		
	def get_minor(self):
		''' This method returns a list of minors. '''
		return self.minor
		
	def get_ID(self):
		''' This method returns the student ID number. '''
		return self.id_num
		
	def get_full_name(self):
		''' This method returns the first and last name of the student in a string. '''
		return self.f_name.title() + " " + self.l_name.title()

