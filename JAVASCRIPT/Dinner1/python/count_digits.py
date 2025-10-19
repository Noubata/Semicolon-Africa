number = 2345;
to_separate = 0;
count =0
to_check = 0
while to_check < 5:
	to_check+=1
	to_separate = number%10
	number = (number-(number%10))/10
	count+=1
print(count)