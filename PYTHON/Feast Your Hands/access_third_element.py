def access_third_element():

	nums = [10, 20, 30, 40, 50]

	third_index = nums[2]
	return third_index
print(access_third_element())


print(' ')

def change_last_color():

	colors = ['red', 'green', 'blue']

	colors[2] = 'yellow'
	return colors
print(change_last_color())

print(' ')

def append_an_element():

	colors = ['red', 'green', 'blue']
	to_append = colors.append('purple')
	return colors
print(append_an_element())

print(' ')

def remove_element():

	my_list = [1, 2, 3, 4, 5]
	to_remove = my_list.remove(3)
	return my_list
print(remove_element())

print(' ')








def sort_a_list():

	my_list = [4, 1, 3, 9, 2]
	to_sort = my_list.sort()
	return my_list
print(sort_a_list())

print(' ')

def return_new_list(*numbers):

	new_list = []
	for number in numbers:
		if number % 2 == 0:
			new_list = numbers[number]
			return new_list
	
print(return_new_list(1, 2, 4, 5, 7))

print(' ')

def combine_lists():

	a = [1, 2, 3]
	b = [4, 5, 6]
	new_list = a + b
	return new_list
print(combine_lists())

print(' ')

def new_list_of_strings():

	my_list = ['Femi', 'Ebuka', 'Me']





