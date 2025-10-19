for number in range(1900, 2026, 1):
	if number % 4 == 0 and number % 100 != 0:
		print(number)
	if number % 4 == 0 and number % 100 == 0 and number % 400 == 0:
		print(number)