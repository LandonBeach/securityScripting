from student_info import Student

# Create three students.
s1 = Student("Anakin", "Skywalker", 1111)
s2 = Student("Obi-Wan", "Kenobi", 2222)
s3 = Student("Han", "Solo", 3333)

# Set the attributes of the first student.
s1.set_status("Active")
s1.set_year("Junior")
s1.set_courses("Anger Management", "Chaos", "Pride")
s1.set_major("Dark-side")
s1.set_minor("Light-side", "Force-choke")
s1.set_age(25)

# Print the attributes of the first student.
print(s1.get_full_name())
print(s1.get_ID())
print(s1.get_status())
print(s1.get_year())
print(s1.get_courses())
print(s1.get_major())
print(s1.get_minor())
print(s1.get_age())
print("")

# Set the attributes of the second student.
s2.set_status("inactive")
s2.set_year("Senior")
s2.set_courses("Lightsaber Making", "Training Jedi")
s2.set_major("Light-side", "Mind-tricks")
s2.set_minor("lightsabers")
s2.set_age(40)

# Print the attributes of the second student.
print(s2.get_full_name())
print(s2.get_ID())
print(s2.get_status())
print(s2.get_year())
print(s2.get_courses())
print(s2.get_major())
print(s2.get_minor())
print(s2.get_age())
print("")

# Set the attributes of the third student.
s3.set_status("Pending")
s3.set_year("Freshman")
s3.set_courses("Flying", "Bargaining")
s3.set_major("Pilot", "Cons")
s3.set_minor("Gun Shooting", "Charming")
s3.set_age(35)

# Print the attributes of the third student.
print(s3.get_full_name())
print(s3.get_ID())
print(s3.get_status())
print(s3.get_year())
print(s3.get_courses())
print(s3.get_major())
print(s3.get_minor())
print(s3.get_age())
