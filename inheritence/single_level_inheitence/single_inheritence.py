#SINGLE LEVEL INHERITENCE
class First:
	def A(self):
		print("Iam from First class")


class Second(First):

	def B(self):
		print("Iam from second class")


fir = First()
fir.A()


sec = Second()
sec.A()
sec.B()