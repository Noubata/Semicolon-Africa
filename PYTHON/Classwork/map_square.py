numbers = [1,2,3,4,5]
def get_square(square):

	return square *square



words = ['Apple', 'banana', 'cherry']
def get_length(length):
	
	return len(length)



numbers1 = [1,2,3,4,5,6]
def is_even(even_numbers):

	return even_numbers % 2 != 1



words1 = ['apple', 'banana', 'kiwi', 'cherry', 'grapes']
def characters(the_word):
	for word in words1:
		if len(the_word) > 5:
			return the_word



words2 = ['I', 'love', 'python', 'snacks']
def one_string(the_string, ee):
	count = ''
	index = 0
	for word in words2:
		count+=word + '-'
	index = count[:-1]
	return indexs



square_numbers = list(map(get_square, numbers))


each_length = list(map(get_length, words))


get_even = list(filter(is_even, numbers1))


get_characters= list(filter(characters, words1))


from functools import reduce

get_reduce = reduce(one_string,words2)


print(square_numbers)

print(each_length)

print(get_even)

print(get_characters)

print(get_reduce)