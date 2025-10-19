count = 0
count1 = 0
for number in range(1900, 2026, 1):
	if number % 4 == 0 and number % 100 != 0:
		count +=1
	if number % 4 == 0 and number % 100 == 0 and number % 400 == 0:
		count1 +=1
print(count+count1)