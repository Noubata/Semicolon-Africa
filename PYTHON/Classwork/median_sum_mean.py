number1 = int(input('enter first number: '))
number2 = int(input('enter second number: '))
number3 = int(input('enter third number: '))
number4 = int(input('enter fourth number: '))

sum = number1+number2+number3+number4
print('the sum of numbers is', sum)
min = number1

if number2 < min:
	min = number2
if number3 < min:
	min = number3
if number4 < min:
	min = number4
print('The minimum number is', min)

max = number1

if number2 > max:
	max = number2
if number3 > max:
	max = number3
if number4 > max:
	max = number4
print('The maximum number is', max)

total = min+max

median = (sum-total)/2

print('the total is', total)

mean= (number1+number2+number3+number4)/4

print('the mean is', mean)