reverse = 234

times = 0
for number in range(3):
	times = reverse%10
	reverse = (reverse-(reverse%10))//10
	print(times, end='')