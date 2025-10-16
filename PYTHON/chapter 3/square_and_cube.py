number = 0
square = 1
cube = 0

while number < 5:
	number+=1
		
	square = number**2
	cube = number**3
	
	print(f' {number:>2} {square:>4} {cube:>4}')