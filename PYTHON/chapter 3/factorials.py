# Pseudocode
#- prompt the user to enter a digit;
#- assign the input to a box called number;
#- Declare one variable named sum that equals 1;
#- use the iteration process to check if number is great than 0;
#- increase sum by number;
#- decrease number by one;
#- print sum.


number = int(input("Enter an number: "))

sum = 1

while number > 0:
	sum*=number
	number -=1
	
print(sum)

	