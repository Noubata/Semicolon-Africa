lists = ['1','2','3']
def convert_string(number):

	return int(number)

get_number = list(map(convert_string, lists))
print("This is the new list :",get_number)



lists1 = [0, 5, 10, 15]

def add_10(number):

	return number + 10

result = list(map(add_10, lists1))
print("When we add 10 to the list we get :", result)


lists3 = [1,3,4,6,9,12]
def divisible_by_3(number):

	return number % 3 == 0

result = list(filter(divisible_by_3, lists3))
print("the numbers divisible by 3 are :", result)


lists5 = [-1, -2, 0, 1, 2]
def positive_number(index):

	return index >=1
get_positive_numbers = list(filter(positive_number, lists5))
print(get_positive_numbers)


from functools import reduce
lists6 = [1,2,3,4,5]
def sum_of_numbers(number, count):
	
	for num in lists6:
		count+=number
		return count
get_sum = reduce(sum_of_numbers, lists6)
print("The sum is :",get_sum)

lists7 = [2, 3, 4]
def product(number, count):

	count*=number
	return count
get_product = reduce(product, lists7)
print("The product is: ",get_product)

lists8 =  [3, 7, 2, 9, 1]
def maximum (number, num1):
	count = 0
	num1 = lists8[0]
	for num in lists8:
		if num > num1:
			num = num1
		return num
get_max = reduce(maximum, lists8)
print(get_max)