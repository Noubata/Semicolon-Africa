number = int(input("Enter a number of 5 digits:  "))


divisor  = ""

while number > 0:
	 my_remainder = number % 10
	 divisor = str(my_remainder) + " " + divisor
	 number = number // 10

print(divisor)