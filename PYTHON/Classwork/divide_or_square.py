import math
def divide_or_square():
	number = int(input('Enter a number: '))
	
	if number%5==0:
		return math.sqrt(number)
	elif number%5!=0:
		return number%5
	elif number < 0:
		print('Invalid number')
result = divide_or_square()
print(f'{result}')
