def appending_a_tuple():

	numbers = (1,2,3,4,5)

	numbers += (6,)
	return numbers
print(appending_a_tuple())

def change_third_element():

	numbers = (1, 2, [3, 4], 5)

	numbers[2][1] = 99
	return numbers
print(change_third_element())


def convert_a_tuple_of_strings ():

	words =  ('apple', 'banana', 'cherry')

	the_strings = [each_element for each_element in words]

	the_strings.append("mango")
	words = tuple(the_strings)
	
	
	return words
print(convert_a_tuple_of_strings())


def sum_of_inner_list():

	numbers = [ [2, 3, 4],  [1, 5, 7],  [4, 6, 8] ]

	numbers[0] = numbers[0][0] + numbers[0][1] + numbers[0][2]
	numbers[1] = numbers[1][0] + numbers[1][1] + numbers[1][2]
	numbers[2] = numbers[2][0] + numbers[2][1] + numbers[2][2]

	return numbers
print(sum_of_inner_list())

def even_numbers(number):
	if number % 2 == 0:

		return number
		
get_even_numbers = list(filter(even_numbers, range(1, 22)))
print(get_even_numbers)


lists = ['cat', 'elephant', 'tiger', 'lion']
def extract(element):

	if len(element) > 5:
		return element
extract_elements = list(filter(extract, lists))
print(extract_elements)

from functools import reduce
numbers = [3, 5, 9, 2, 8]
def maximum(number1, number2):

	if number1 > number2:
		return number1
	else:
		return number2
get_maximum = reduce(maximum, numbers)
print(get_maximum)

def sum_of_numbers(number1, number2):

	return number1 + number2
get_sum =  reduce(sum_of_numbers, range(1, 51))

print(get_sum)


def find_square (number) :

	return number * number
get_square = list(map(find_square, range(1, 11)))
print(get_square)

prices = [100, 200, 300]
def add_tax (number):

	for element in prices:
		element = number + (number * 10)/100
		return element
get_tax = list(map(add_tax, prices))

print(get_tax)

lists1 = ['python', 'java', 'c++']
def convert_strings(word):

	for element in lists1 :
		element = word.upper()
	return element
converted = list(map(convert_strings, lists1))
print(converted)


def divisible (number):

	if number % 5 == 0 and number % 3 == 0:
		return number
get_result = list(filter(divisible, range(1, 52)))
print(get_result)

from functools import reduce
numbers = [1, 2, 3, 4]
def square_and_product(number):

	for element in numbers:
		element = number * number
	return element 
	for each in numbers:
		each = element * element
	return each
		 
get_square = list(map(square_and_product, numbers))
print("the square is :",get_square, end='')
get_product = reduce(lambda number1, number2:number1 * number2 , get_square)
print(" and their product is:",get_product)


words = ['I', 'love', 'Python'] 

get_single_string = reduce(lambda word1, word2: word1 + ' ' + word2, words)

print(get_single_string)

names = ['john', 'mary', 'steve']
def capitalize_letters(name):

	for word in words:
		