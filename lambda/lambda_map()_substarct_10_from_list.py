#substact 10 from each value from list
numbers = [50,100,150,40,200]

subten = list(map(lambda a :a-10,numbers))
print(subten)


"""

numbers = [50,100,150,40,200]

def subTen(n):
	return n-10

subten = list(map(subTen,numbers))
print(subten)

"""