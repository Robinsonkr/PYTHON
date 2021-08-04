#single level inheritence with calling base class

class Person:
	def __init__(self,fname,lname):
		self.firstname = fname
		self.lastname = lname

	def person_details(self):
		print(self.firstname + self.lastname)

class Student(Person):
	def __init__(self,fname,lname,year):
		Person.__init__(self,fname,lname)
		self.graduation_year = year

	def full_details(self):
		print(self.firstname + self.lastname +self.graduation_year)

p1 = Student("robinson","KR","2018")
p1.person_details()

