/*Pseudocode

- create correctGuess variable that equals to 1;
- create sum1 variable that equals to 0;
- create sum2 variable that equals to 0;
- prompt the user to enter a number which should be assigned to 'guess' variable;
- use an iteration process to check that guess is lesser than 3
- prompt the user to enter a number which should be assigned to 'guess' variable;
- check if guess equals to correctGuess, if so,
- increase sum1 by correctGuess;
- if not, increase sum2 by correctGuess;
- prompt the user to enter a second number which should be assigned to 'secondGuess' variable;
- check if secondGuess is equals to correctGuess. if so, 
- increase sum1 by correctGuess;
- display woow, you won!
- if not, increase sum2 by correctGuess;
- display woow, the computer won!
*/

import java.util.Scanner;
public class Continuous1{
public static void main(String[]args){
Scanner input = new Scanner(System.in);
	int correctGuess = 1;
	int sum1 = 0;
	int sum2 = 0;
	System.out.println("Enter a number: ");
	int guess = input.nextInt();

	while(guess<3){
	
	System.out.println("Enter a number: ");
	int guess1 = input.nextInt();
	
	if (guess == correctGuess){
	sum1+=correctGuess;
	}else{
	sum2+=correctGuess;
	}

	System.out.println("Enter a second number: ");
	int secondGuess = input.nextInt();
	


	if (secondGuess == correctGuess){
	sum1+=correctGuess;
	System.out.println("Woow! You won: ");
	}else{
	sum2+=correctGuess;
	System.out.println("You filed! the cumputer won ");
	}
}
	
}
}


