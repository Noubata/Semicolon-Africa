import random

correct_number = random.randrange(1, 1000)
print('welcome to GUESS THE NUMBER!')
next_guess = 0
while next_guess != 0:
	next_guess+=1

	the_guess = int(input('Guess my number between 1 to 1000 with fewest guesses: '))

	if the_guess == 0:
		break
	elif the_guess != correct_number and the_guess > correct_number:
		print('Too high. Try again')
	elif the_guess != correct_number and the_guess < correct_number:
		print('Too low. Try again')
	elif the_guess == correct_number:
		print('Congratulations. You guessed the number!')
	else:
		print('Enter a valid number please.')