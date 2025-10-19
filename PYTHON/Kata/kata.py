"""
def is_even(number):
	if number %2 == 0:
		return True
	else:
		return False
print(is_even(24))

def is_prime(number):
	if number == 1 or number == 3 or number == 5 or number == 7 or number == 11 or number == 13:
		return True
	elif number % 1== 0 or number % 3== 0 or number % 5 == 0 or number % 7==0 or number % 11==0 or number %13 ==0:
		return False
	else:
		return True
print(is_prime(18))

def subtract(number1, number2):
	difference = number1-number2
	if difference > 0:
		return difference
	else:
		return difference*(-1)
print(subtract(12, 15))

def divide(number1, number2):
	if number2 == 0:
		return 0
	else:
		quotient = number1/number2
		return quotient
print(divide(12, 0))

def factor_of(number):
	divisor = 0
	the_number = 0
	while(the_number<=number):
		the_number+=1
		if number % the_number:
			return divisor++1
			
print(factor_of(10))

import math

def is_square(number):
	if number%math.sqrt(number)==0:
		return True
	else:
		return false

print(is_square(25))

"""

def is_palindrome(number):
	if number <0:
		return False
	number1 =0
	number2 =0
	while number !=0 :
		if number==5:
			number1= number%10
			number2= number2*10+number1
			number/=10
			return True
		
print(is_palindrome(1234))

def factorialOf(number):
	sum = 1
	while number != 0:
		sum*=number
		number-=1
	return sum
print(factorialOf(2))

def squareOf(number):
	to_calculate= math.pow(number, 2)
	return to_calculate
print (squareOf(3))







