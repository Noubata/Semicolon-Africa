import java.util.Scanner;
	public class ContinuousInput{
		public static void main(String[]args){
		Scanner input = new Scanner(System.in);

		System.out.print("Enter a number: ");
		int userInput = input.nextInt();

		int positiveNumbers = 0;
		int negativeNumbers = 0;
		int zero = 0;

		while(userInput != -1){

		System.out.print("Enter a number(you can enter -1 to stop): ");
		userInput = input.nextInt();

		if (userInput >= 1){
		positiveNumbers += 1;
		}else if(userInput<=-1){
		negativeNumbers +=1;
		}else{
		zero +=1;
		}
	
		}
		System.out.printf("There are %d positive numbers, %d negatives numbers, and %d zeros", positiveNumbers, negativeNumbers, zero);
		}
	}