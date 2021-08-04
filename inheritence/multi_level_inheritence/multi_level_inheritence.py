#MULTI LEVEL LEVEL INHERITENCE
class First:
	def A(self):
		print("Iam from first class")

class Second(First):
	def B(self):
		print("Iam from second class")

class Third(Second):
	def C(self):
		print("Iam from third class")



thi = Third()
thi.A()
thi.B()
thi.C()

sec = Second()
sec.A()
sec.B()

fir = First()
fir.A()

