import java.util.Scanner;
	public class UserInput{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);

	int count = 0;

	System.out.println("Enter a number: ");
	count = input.nextInt();

	while(count !=1 && count !=2){
	System.out.println("Enter a number: ");
	count = input.nextInt();

	}
	System.out.println("You won");
}
}