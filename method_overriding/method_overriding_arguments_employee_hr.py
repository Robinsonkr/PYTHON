#method overriding

class Employee:
	def salary(self,basic,allowance):
		print("salary from base class",basic + allowance)


class HR(Employee):
	def salary(self,basic,allowance,bata):
		Employee.salary(self,basic,allowance)
		# super().salary(basic,allowance)
		print("salary from child class",basic + allowance + bata)


em = HR()
em.salary(10000,500,200)
