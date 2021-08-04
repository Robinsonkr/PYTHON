#Multiple inheritence
class First:
	def A(self):
		print("Iam from first class")


class Second:
	def B(self):
		print("Iam from second class")


class Third(First,Second):
	def C(self):
		print("Iam from third class")


thi = Third()
thi.A()
thi.B()
thi.C()

