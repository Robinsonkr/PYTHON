#sum of all items in a list
from functools import reduce

numbers = [50,100,150,40,200]

total_list = reduce(lambda a,b:a+b,numbers)

print(total_list)


"""
from functools import reduce
numbers = [50,100,150,40,200]

def Total(a,b):
	return a+b

total_list = reduce(Total,numbers)
print(total_list)

"""

