def arbitrary_argument_list(*numbers):
	product = 1
	for list_of_numbers in numbers:
		product*=list_of_numbers
	return product
print(arbitrary_argument_list(2, 6, 2))
print(arbitrary_argument_list(2, 6, 3, 2))
print(arbitrary_argument_list(0, 6, 2))