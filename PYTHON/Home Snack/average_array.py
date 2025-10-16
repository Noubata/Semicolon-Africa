def average_array():

	my_list = [5, 12, 30, 76, 2]
	
	sum =0
	for numbers in my_list:
		sum+=numbers
	return sum/len(my_list)
print(average_array())
