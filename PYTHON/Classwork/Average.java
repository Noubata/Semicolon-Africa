/*pseudocode
- prompt the user to enter three scores and assign each to score1, score2, and score3, respectively;
- create 'average' variable that equals all three scores added divided by 2;
- check if average is greater than or equal to 90 and less than or equal to 100, display 'Your average score earns you an 'A', if not
- check if average is greater than or equal to 80 and greater than 90, display 'Your average score earns you a 'B'
- check if average is greater than or equal to 70 and greater than 80, display 'Your average score earns you a 'C'
- check if average is greater than or equal to 60 and greater than 70, display 'Your average score earns you a 'D'
- check if average is greater than or equal to 0 and greater than 60, display 'Your average score earns you an 'F'
*/

import java.util.Scanner;

	public class Average{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	System.out.println("Enter first score: ");
	int score1 = input.nextInt();
	System.out.println("Enter second score: ");
	int score2 = input.nextInt();
	System.out.println("Enter third score: ");
	int score3 = input.nextInt();

	int average = score1 + score2 + score3;

	if (average >= 90 && average <= 100){
	System.out.println("Your average score earns you an 'A'");
	}else if (average >= 80 && average > 90){
	System.out.println("Your average score earns you an 'B'");
	}else if (average >= 70 && average > 80){
	System.out.println("Your average score earns you an 'C'");
	}else if (average >= 60 && average > 70){
	System.out.println("Your average score earns you an 'D'");
	}else if (average >= 0 && average > 60){
	System.out.println("Your average score earns you an 'F'");
	}
}
}
