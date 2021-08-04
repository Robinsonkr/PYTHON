class Parent:

	def product(self,a,b):
		result = a * b
		print(result)

	def product(self,a,b,c):
		result = a * b* c
		print(result)



x = Parent()
# x.product(10,20)  not work 
x.product(10,20,30)