num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))

total = num1+num2+num3
print('The sum of', num1, ",", num2, 'and', num3, 'is', total)
print('The average of', num1, ",", num2, 'and', num3, 'is', str(total/2))
print('The product of', num1, ",", num2, 'and', num3, 'is', str(num1*num2*num3))

largest = num1 

if num2>largest:
	largest=num2
if num3>largest:
	largest=num3

smallest = num1

if num2<smallest:
	smallest=num2
if num3<smallest:
	smallest=num3
 
print('The largest number is', largest)
print('The smallest number is', smallest)