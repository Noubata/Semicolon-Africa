def longest_string(*list_of_strings):
	
	longest = list_of_strings[0]
	for my_string in list_of_strings:
		if len(my_string) > len(longest):
			longest = my_string 
	return  longest, len(longest)
print(longest_string('longest', 'analphabete', 'anticonstitutionnellement'))


def minimum_numbers(*list_of_numbers):
	
	minimum = list_of_numbers[0]
	for the_number in list_of_numbers:
		if the_number < minimum:
			minimum = the_number 
	return   minimum
print(minimum_numbers(0, 8, 90, 3, -1, -78, 1000000))


def maximum_numbers(*list_of_numbers):
	
	maximum = list_of_numbers[0]
	for the_number in list_of_numbers:
		if the_number > maximum:
			maximum = the_number 
	return   maximum
print(maximum_numbers(0, 8, 90, 3, -1, -78, 1000000))


import math
def list_as_parameter(*numbers):

	square = 0
	sum = 0
	for num in numbers:
		square = math.pow(num, 2)
		sum+=square
	return sum
print(list_as_parameter(2, 4, 6, 8))



def list_squared():
	numbers = [2, 4, 6, 8]
	for number in range(len(numbers)):
		numbers[number] **=2
		square = numbers
	return square
print(list_squared())

def repeated_string(*the_list):
	
	for the_string in the_list:
		if type(the_list[1])==float:
			return the_list[0]
		else:
			to_repeat = the_list[0]*the_list[1]
	return to_repeat
print(repeated_string('come', 7.0,))


def first_and_last_characters():

	contains_string = ['semicolon']
	length = 0
	word = contains_string[0]
	length = len(contains_string[0])
	if length >=2:
		the_word = word[:2] + word[-2:]
		return the_word
	else:
		return ""
print(first_and_last_characters())














