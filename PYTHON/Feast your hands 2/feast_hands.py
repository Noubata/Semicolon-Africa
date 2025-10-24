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

	return index*(-1)
get_positive_numbers = list(filter(positive_number, lists5))
print(get_positive_numbers)