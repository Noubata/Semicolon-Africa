import math
number = 153

num1 = number//100
num2 = (number%100)//10
num3 = number % 10

num = math.pow(num1, 3) + math.pow(num2, 3) + math.pow(num3, 3)

if num == number:
	print(number," is an Armstrong number")
else:
	print(number,"is not a Armstrong number")