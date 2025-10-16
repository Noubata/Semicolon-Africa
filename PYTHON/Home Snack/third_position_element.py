def third_position_element():
	the_list = [1, 7, 9, 3]
	multiply = 0
	for number in the_list:
		multiply = the_list[2]*the_list[2]
	return multiply
print(third_position_element())