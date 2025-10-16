def sum_up_even_numbers():

	my_list = [2, 9, 0, 6, 7, 4, 8]
	sum = 0
	for number in my_list:
		if number % 2 ==0:
			sum+=number
	return sum
print(sum_up_even_numbers())