def find_largest():
	
	my_list = [12, 30, 67, 0, -1]
	
	largest = 0
	for numbers in my_list:
		largest = my_list[0]
		if numbers > largest:
			largest = numbers
	return smallest
print(find_largest())
