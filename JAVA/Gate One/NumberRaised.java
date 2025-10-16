/*Pseudocode

- prompt the user to enter numbers that will be stored in two different containers, number1 and number2;
- declare two boxes(variables), total and sum, that equal 0 and 1, respectively.
- use the iteration processnto check if total is less than number2;
- increase total by 1;
- increase sum  by number1
- print sum.

*/


import java.util.Scanner;
	public class NumberRaised{
		public static void main(String[]args){
		Scanner input = new Scanner(System.in);
		System.out.print("Enter your number: ");
		int number1 = input.nextInt();
		System.out.println("Enter second number: ");
		int number2 = input.nextInt();
		
		int total = 0;
		int sum = 1;
		while(total < number2){

		total++;
		sum *=number1;
				
		}
		System.out.print(sum);
		}
	}