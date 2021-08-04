class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def person_details(self):
		print(self.name + self.age)

p1 = Person("Robin","23")
p1.person_details()
