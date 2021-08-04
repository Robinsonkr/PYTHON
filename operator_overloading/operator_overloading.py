# name = "Robin"
# age = 22
# age2 = 3


# print(age+age2)
# print(int.__add__(age,age2))

# print(type(name))
# print(type(age))



class User_salary:
	def __init__(self,salary):
		self.salary = salary

	def __add__(self,other):
		return self.salary + other.salary

a = User_salary(5000)
b = User_salary(2000)

c = a + b
print(c)






