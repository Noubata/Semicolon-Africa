def find_smallest():
	
	my_list = [12, 30, 67, 0, -1]
	
	smallest = 0
	for numbers in my_list:
		smallest = my_list[0]
		if numbers < smallest:
			smallest = numbers
	return smallest
print(find_smallest())

def average_array():

	my_list = [5, 12, 30, 76, 2]
	
	sum =0
	for numbers in my_list:
		sum+=numbers
	return sum/len(my_list)
print(average_array())

def count_occurence():

	my_list = [1, 3, 0, 1, 7, 3]

	add = 0
	for numbers in my_list:
		if numbers==0:
			add+=1
	return add
print(count_occurence())

def contains_element():
	
	my_list = [0, 3, 2, 0, 7, 1]
	for numbers in my_list:
		if numbers == 1:
			return True
print(contains_element())

def get_first_element(*number):

	#for numbers in number:
	if len(number)==0:
		return 0
	else:
		return number[0]
print(get_first_element(2.8, 87, 0))

def get_first_element():

	my_list = []
	if len(my_list)==0:
		return 0
	else:
		return my_list[0]
print(get_first_element())

def get_last_element(*number):

	sum =0
	for numbers in number:
		sum+=1
	return sum
print(get_last_element(0, 8, 8, 0, 90))






