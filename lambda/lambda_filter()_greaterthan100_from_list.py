#get values greater then 100 from list
my_list = [50,100,150,40,200]



result = list(filter(lambda n:n>100,my_list))
print(result)

"""
def graterTen(n):
	return n>100

result = list(filter(graterTen,my_list))
print(result)


"""