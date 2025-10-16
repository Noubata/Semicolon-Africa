import java.util.Scanner;
	public class Geometry{
        public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        System.out.println("Enter a digit");
	int digit = input.nextInt();
	
	int num1 = digit/1000000000;
	int num2 = (digit%1000000000)/100000000;
	int num3 = (digit%100000000)/10000000;
	int num4 = (digit%10000000)/1000000;
	int num5 = (digit%1000000)/100000;
	int num6 = (digit%100000)/10000;
	int num7 = (digit%10000)/1000;
	int num8 = (digit%1000)/100;
	int num9 = (digit%100)/10;
	int num0 = digit%10;

	
	
	int even = 0; 
	int odd = 0;
	if (num1 % 2 == 0) even = even + num1; else odd = odd + num1;
        if (num2 % 2 == 0) even = even + num2; else odd = odd + num2;
        if (num3 % 2 == 0) even = even + num3; else odd = odd + num3;
        if (num4 % 2 == 0) even = even + num4; else odd = odd + num4;
        if (num5 % 2 == 0) even = even + num5; else odd = odd + num5;
	if (num6 % 2 == 0) even = even + num6; else odd = odd + num6;
	if (num7 % 2 == 0) even = even + num7; else odd = odd + num7;
	if (num8 % 2 == 0) even = even + num8; else odd = odd + num8;
	if (num9 % 2 == 0) even = even + num9; else odd = odd + num9;
	if (num0 % 2 == 0) even = even + num0; else odd = odd + num0;



	System.out.printf("Even sum = %d%n", even);
	System.out.printf("Odd sum = %d%n", odd);
}
}
