def my_floats(a, b):
	if type(a) and type(b) == float:
		return 2
	if type(a) and type(b) != float:
		return 0
	if type(a) or type(b) == float:
		return 1
	
print(my_floats(12, 23))