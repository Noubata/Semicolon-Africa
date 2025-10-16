number = int(input("Enter a number: "))
passes = 0
failures = 0

while number != 1 and number != 2:
	number = int(input("Enter a number: "))
	failures = failures + 1
number+=1

if number == 1 or number == 2:
	passes = passes + 1
print(f'passed: {passes}')
print(f'failed: {failures}')