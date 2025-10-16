/*Pseudocode
- Prompt the user to enter three-digit numbers;
- check if the input is equal to three numbers, if not, display "Invalid"
- Assign the input to the variable num;
- Declare three variables, among which num1, num2, and num3 all equal to 0;
- Declare three other variables b, c, and d all equal to 1;
- Separate each number from the others, assign them to num1, num2, and num3 already declared, and 
  Divide the input by 100 that should belong to num1. 
- Print the numbers separated.
- While num1 is greater than or equal to 1, call c that should be equal to c multiplied by num1, and then decrement num1 by 1;
- While num2 is greater than or equal to 1, call b that should be equal to b multiplied by num2, and then decrement num2 by 1;
- While num3 is greater than or equal to 1, call d that should be equal to d multiplied by num3, and then decrement num3 by 1;
- Declare a variable e that the sum of c, b, and d should be assigned to.
- Print e;

*/
import java.util.Scanner;
	public class Mul{
		public static void main(String[]args){
		Scanner input = new Scanner(System.in);
		System.out.print("Enter three digit numbers:");
		int num = input.nextInt();
		

		int num1 =0;
		int num2 =0;
		int num3 =0;
		int b = 1;
		int c = 1;
		int d = 1;
		int e = 0;
		if (num>999){
		System.out.println("Invalid");
		}else{
		num1 = num/100;
		num2 = (num%100)/10;
		num3 = num%10;

		System.out.printf("%d %d %d%n", num1, num2, num3);
	

		while(num1>=1){
		c = c*num1;
		num1--;
		
		}
		while(num2>=1){
		b = b*num2;
		num2--;
		}
		while(num3>=1){	
		d = d*num3;
		num3--;
		}
		e = c+b+d;

		System.out.println(e);
		}
		if (e>num){
		System.out.printf("%d is greater than %d, so it is strong number", e, num);
		}else{
		System.out.printf("%d it is not a strong number", num);
		}
	}
}