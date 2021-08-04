class Phone:
	def make_call(self):
		print("calling")

	def play_game(self):
		print("playing game")

	def set_color(self,color):
		self.color = color

	def show_color(self):
		print(self.color)

p1 = Phone()
p1.set_color("RED")
p1.show_color()

p1.make_call()
p1.play_game()