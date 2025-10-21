number = int(input("Enter your number: "))

count = 0;
sum = 0;
divisor = 0
for num in range(1, number):
	divisor+=1
	if number % num == 0 :
		sum+=divisor
print(sum)