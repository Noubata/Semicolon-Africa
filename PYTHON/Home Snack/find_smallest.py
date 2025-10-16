def find_smallest():
	
	my_list = [12, 30, 67, 0, -1]
	
	smallest = 0
	for numbers in my_list:
		smallest = my_list[0]
		if numbers < smallest:
			smallest = numbers
	return smallest
print(find_smallest())
