import java.util.Scanner;

	public class Palindrome{
	public static void main(String[]args){

	Scanner userInput = new Scanner(System.in);
	System.out.println("Enter a number: ");
	int number = userInput.nextInt();
	
	int total = 1;
	while(number > 0){
	
	total = total*number;
	number--;
	}
	System.out.print( total);
	}

}