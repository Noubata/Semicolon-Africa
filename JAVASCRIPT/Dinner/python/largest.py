numbers = 67530
largest = 0
number = 0
each_of_numbers =0
while number <=4:
	number+=1
	each_of_numbers = numbers%10
	numbers = (numbers-(numbers % 10))/10
	if each_of_numbers>largest:
		largest = each_of_numbers

print(largest)
