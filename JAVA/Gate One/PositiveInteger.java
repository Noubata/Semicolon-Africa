/* Pseudocode

- prompt the user to enter a number that will be stored in a container named number1;
- use the iteration process to check if number is less than or equals to 0, then print 'enter a positive number', if not
- check if number equals 2 and others odd numbers from 3 to 13 except 9. print number it is a prime number, if not
- check if those same numbers their remainder equals 0, if so print number it is a prime number.
- check that other numbers than those ones are prime numbers.


*/

import java.util.Scanner;
	public class PositiveInteger{
		public static void main(String[]args){
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a positive number: ");
		int number = input.nextInt();

	if(number <= 0){
		System.out.print("Enter a positive number");
	else if(number == 2 || number == 3 || number == 5 || number == 7 || number == 11 || number == 13){
		System.out.printf("%d is a prime number", number);
	}else if(number % 2 == 0 || number % 3 == 0 || number % 5 == 0 || number % 7 == 0 || number % 11 == 0 || number % 13 == 0){
		System.out.printf("%d is not a prime number", number);
	}else{
		System.out.printf("%d is a prime number", number);
	}
	
		}
	}