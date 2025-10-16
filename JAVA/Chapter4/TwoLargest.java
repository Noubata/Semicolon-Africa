/*Pseudocode

- Declare two variables counter and largest that each equals to 0;
- declare number variable which will store the user's input;
- Use an iteration process to check that counter is less than or equal to 10;
- increase counter by 1;
- Prompt the user to enter number that should be assigned to the box number;
- check if number is greater than largest then largest equals number;
- print largest
*/

import java.util.Scanner;
	public class TwoLargest{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	
	int number = 0;
	int counter = 1;
	int largest = 0;
	int sum = 0;
	int secondLargest = 0;

	while(counter<=10){
	counter++;
	System.out.println("Enter number of units: ");
	number = input.nextInt();

	
	
	if(number > largest){
	largest = number;
	}
	

	if(secondLargest != number){
	secondLargest = largest ;
	}	
	
	}
	//System.out.printf("%d%n", sum);
	System.out.printf("The two largest numbers are %d and %d%n", secondLargest, largest);
	
}
}