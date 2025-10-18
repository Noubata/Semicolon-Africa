number = 12323
to_change = number
count = 0
while number >0:
	digit = number%10
	count = count*10+digit
	number = number//10
if to_change == count:
	print("Palindrome number")
else: 
	print("Not a palindrome number")