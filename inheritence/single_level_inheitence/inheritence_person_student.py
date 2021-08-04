#inheritence

class Person:
	def __init__(self,fname,lname):
		self.firstname = fname
		self.lastname = lname

	def person_details(self):
		print(self.firstname + self.lastname)

class Student(Person):
	pass

p1 = Student("robinson","KR")
p1.person_details()

