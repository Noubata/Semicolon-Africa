/* Pseudocode
- prompt the user to enter a digit;
- assign the input to a a box called number;
- Declare one variable named sum that equals 1;
- use the iteration process to check if number is greathan 0;
- increase sum by number;
- decrease number by one;
- print sum.

*/
import java.util.Scanner;
	public class FactorialValue{
		public static void main(String[]args){
		Scanner input = new Scanner(System.in);
		System.out.print("Enter an digit: ");
		int number = input.nextInt();

		int sum = 1;

		while (number > 0){
		sum*=number;
		number --;
	
		}
		System.out.println(sum);

		}
	}