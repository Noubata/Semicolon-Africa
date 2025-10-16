def sum_up_odd_numbers():

	my_list = [5, 9, 0, 6, 7, 3, 8]
	sum = 0
	for number in my_list:
		if number % 2 ==1:
			sum+=number
	return sum
print(sum_up_odd_numbers())