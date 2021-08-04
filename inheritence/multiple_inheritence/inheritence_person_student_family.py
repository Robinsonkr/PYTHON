# multi level inheritence 
#This follows MRO METHOD RESOLUTION ORDER 
#that is priory is from left to right

class Person:
	def __init__(self):
		print("Init of first")


class Student():
	def __init__(self):
		print("Init of second")


class Family(Person,Student):
	def __init__(self):
		super().__init__()
		print("Init of third")

stu = Family()


