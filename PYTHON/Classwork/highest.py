number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
number3 = int(input('Enter third number: '))


highest = number1

if number2 > highest:
	highest = number2
if number3 > highest:
	highest = number3

print('the highest number is', highest)



second_largest = highest

if second_largest == number1 and number1 > number2 and number2 > number3:
	second_largest = number2
if second_largest == number1 and number1 > number3 and number3 > number2:
	second_largest = number3
if second_largest == number2 and number2 > number3 and number3 > number2:
	second_largest = number3
if second_largest == number2 and number2 > number1 and number1 > number3:
	second_largest = number2
if second_largest == number3 and number3 > number1 and number1 > number2:
	second_largest = number1
if second_largest == number3 and number3 > number2 and number2 > number1:
	second_largest = number2


print('the second largest number is', second_largest)


