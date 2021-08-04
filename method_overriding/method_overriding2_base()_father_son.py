#method overriding2 with calling base

class Father:
	def phone(self):
		print("father have nokia phone")

class Son(Father):
	def phone(self):
		Father.phone(self)
		print("son have iphone")

fa = Son()
fa.phone()