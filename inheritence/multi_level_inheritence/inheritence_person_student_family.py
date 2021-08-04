# multi level inheritence

class Person:
	def __init__(self):
		print("Init of first")


class Student(Person):
	def __init__(self):
		super().__init__()
		print("Init of second")


class Family(Student):
	pass

stu = Student()


