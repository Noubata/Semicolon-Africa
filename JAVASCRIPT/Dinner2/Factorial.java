import java.util.Scanner;
	public class Factorial{
		public static void main(String[]args){
		Scanner collectorInput = new Scanner(System.in);
		System.out.print("Enter a number:");
		int number = collectorInput.nextInt();

	int count = 1;
	int multiply = 0;	
	while(multiply >0){
	multiply++;
	count*=number;
	number-=1;
	}
	System.out.printf("the factorial of %d is %d", number, count);

	}
}