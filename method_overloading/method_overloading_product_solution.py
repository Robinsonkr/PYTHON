class Parent:

	def product(self,a=None,b=None,c=None):
		if a!= None and b!= None and c!=None:
			result = a * b* c
			print(result)

		elif a!=None and b!=None:
			result = a + b 
			print(result)


x = Parent()

x.product(10,20,10)