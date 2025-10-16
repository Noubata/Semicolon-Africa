#pseudocode
#prompt the user to enter his father's age and his own age, assign them to each to father age and my age, respectively;
#check if the two ages are greater than 80 or less than 0, if so display your age should be between 1 to 80;
#declare my age2 variable that equals to my age multiplied by 2;
#declare years variable that equals to father age minus my age2;
#check if years is greater than or equal to 0, display your father was your age  years(the answer got) years ago;
#check if years is less than or 0, display your father will be your age  in years(the answer got). make sure the result remains positive;

father_age = int(input("Enter your father's age: "))
my_age = int(input("Enter your age: "))

my_age2 = my_age * 2
years = father_age - my_age2
times = years*(-1)

if father_age or my_age > 0:
	print(" ")
else:
	print("Your age should be between 1 to 80")

if years >= 0:
	print("Your father  was twice as old as you", years, "years ago")
if years < 0:
	print("Your father will be twice as old than you  in", times, "years")