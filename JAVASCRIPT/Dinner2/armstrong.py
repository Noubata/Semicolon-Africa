import math
number = 153

divisor = []
count = 0
sum =0
for num in range(1, 1001, 1):
	count = number%10
	number = (number-(number%10))//10
	divisor = [math.pow(num, 2)]
	print(sum)