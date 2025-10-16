question = int(input('Enter an integer: '))

sum = 0

product = 1

average = 0

smallest = 0

largest = 0

for integer in range(3):
	integer = int(input('Enter an integer: '))
	sum+=integer
	average+=integer/2
	product*=integer
	smallest = question
	largest = question
	if integer < smallest:
		smallest = integer
	if integer > largest:
		largest = integerx
print('The sum is', sum)
print('The product is', product)
print('The average is', average)
print('the smallest number is', smallest)
print('the largest number is', largest)


