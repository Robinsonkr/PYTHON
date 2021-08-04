#method overriding

class Father:
	def phone(self):
		print("father have nokia phone")

class Son(Father):
	def phone(self):
		print("son have iphone")

fa = Son()
fa.phone()