def return_new_list():
	my_list = [1, 2, 3, 4, 5, 6]
	new_list = []
	for lists in my_list:

		if lists % 2 == 0:
			new_list += [lists]
	return new_list
print(return_new_list())

def return_length():

	my_list = ['Alice', 'Bob', 'Charlie']

	the_length = []
	for only_length in my_list:
		the_length += [len(only_length)]
	return the_length
print(return_length())

def return_string():

	words = ['lamb', 'kit', 'yam', 'kings', 'dogs', 'man']
	
	new_list = []
	for the_string in words:
		if len(the_string) > 3:
			new_list += [the_string]
	return new_list
print(return_string())

def return_the_letter_e():

	count = 0
	the_word = 'shelleleeee'
	for word in the_word:
		if word == 'e':
			count+=1
	return count

print(return_the_letter_e())

def count_vowels():

	count = 0
	the_word = 'anticonstitutionnellement'
	for word in the_word:
		if word == 'e' or word == 'a' or word == 'o' or word == 'u' or word == 'i':
			count+=1
	return count

print(count_vowels())

def count_digit():

	count =0
	numbers = 123456789
	for number in numbers:
		number = numbers%10
		numbers = (numbers-(numbers%10))//10
		if number == 1 or number == 2 or number == 3 or number == 4 or number == 5 or number == 6 or number == 7 or number == 8 or number == 9:
			count+=1

	return count

print(count_digit())

def alphabet():
	
	


	


