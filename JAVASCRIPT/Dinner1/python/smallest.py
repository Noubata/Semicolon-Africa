numbers = 67530
smallest = 0
number = 0
each_of_numbers =0
while number <=4:
	number+=1
	each_of_numbers = numbers%10
	numbers = (numbers-(numbers % 10))/10
	if each_of_numbers<smallest:
		smallest = each_of_numbers

print(smallest)
