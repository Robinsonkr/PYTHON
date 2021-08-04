#method overriding3with super function

class Father:
	def phone(self):
		print("father have nokia phone")

class Son(Father):
	def phone(self):
		super().phone()
		print("son have iphone")

fa = Son()
fa.phone()