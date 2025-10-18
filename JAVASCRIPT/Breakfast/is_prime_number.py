number = 0
count = 0
count1 = 0
count2 = 0
while number<100:
	number+=1
	if number == 2 or number == 3 or number == 5 or number == 7 or number == 11 or number == 13 or number == 17 or number == 19:
		count+=1
	elif number % 2 != 0 or number % 3 != 0 or number % 5 != 0 or number % 7 != 0 or number % 11 != 0 or number % 13 != 0 or number % 17 != 0 or number % 19 !=0:
		count1+=1
	else :
		count2+=1
print(count+count1+count2)