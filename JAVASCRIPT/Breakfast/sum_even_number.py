number = 2345;
to_separate = 0;
sum =0
to_check = 0
while to_check < 5:
	to_check+=1
	to_separate = number%10
	number = (number-(number%10))//10
	if number % 2 == 0:
		sum+=number
print(sum)