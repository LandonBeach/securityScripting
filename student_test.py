from student import Student

s1 = Student("Anakin", "Skywalker", 1111)
s2 = Student("Obi-Wan", "Kenobi", 2222)
s3 = Student("Han", "Solo", 3333)

s1.set_status("Active")
s1.set_year("Senior")
s1.set_courses("Math1", "Python2", "Biology")
full_name = s1.get_full_name()
student_id = s1.get_ID()
