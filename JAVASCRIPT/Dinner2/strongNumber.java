
import java.util.Scanner;
	public class StrongNumber{
		public static void main(String[]args){
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a number:");
		int number = input.nextInt();
		

		int number1 =0;
		int number2 =0;
		int number3 =0;
		int count1 = 1;
		int count2 = 1;
		int count3 = 1;
		int count4 = 0;
		if (number>999){
		System.out.println("Invalid");
		}else{
		number1 = number/100;
		number2 = (number%100)/10;
		number3 = number%10;

		//System.out.printf("%d %d %d%n", number1, number2, number3);
	

		while(number1>=1){
		count3 = count1*number1;
		number1--;
		
		}
		while(number2>=1){
		count2 = count2*number2;
		number2--;
		}
		while(number3>=1){	
		count4 = count4*number3;
		number3--;
		}
		count1 = count3+count2+count4;

		//System.out.println(count1);
		}
		if (count1>number){
		System.out.printf("%d is greater than %d, so it is strong number", count1, number);
		}else{
		System.out.printf("%d is not a strong number", number);
		}
	}
}