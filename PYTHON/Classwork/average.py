#pseudocode
#- prompt the user to enter three scores and assign each to score1, score2, and score3, respectively;
#- create 'average' variable that equals all three scores added divided by 2;
#- check if average is greater than or equal to 90 and less than or equal to 100, display 'Your average score earns you an 'A', if not
#- check if average is greater than or equal to 80 and greater than 90, display 'Your average score earns you a 'B'
#- check if average is greater than or equal to 70 and greater than 80, display 'Your average score earns you a 'C'
#- check if average is greater than or equal to 60 and greater than 70, display 'Your average score earns you a 'D'
#- check if average is greater than or equal to 0 and greater than 60, display 'Your average score earns you an 'F'

score1 = int(input('Enter first score: '))
score2 = int(input('Enter second score: '))
score3 = int(input('Enter third score: '))

average = score1 + score2 + score3

if average >= 90 and average <= 100 :
	print("Your average score earns you an 'A'")
elif average >= 80 and average > 90 :
	print("Your average score earns you a 'B'")
elif average >= 70 and average > 80 :
	print("Your average score earns you a 'C'")
elif average >= 60 and average > 70 :
	print("Your average score earns you a 'D'")
elif average >= 0 and average > 60 :
	print("Your average score earns you a 'F'")





