import java.util.Scanner;

// create an input that is separated by space

public class Separate {
public static void main(String[]args){
// collect user's digit
	Scanner input = new Scanner(System.in);
	System.out.println("Entrez votre numero!");
	int digit = input.nextInt();
	
	// Display the digit
int num1 = digit / 10000;
int num2 = (digit % 10000)/1000;
int num3 = (digit % 1000)/100;
int num4 = (digit % 100)/10;
int num5 = digit % 10;
	System.out.printf("%d %d %d %d %d%n", num1, num2, num3, num4, num5);
}
} 