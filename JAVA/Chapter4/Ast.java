import java.util.Scanner;
	public class Ast{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	double num1 = 0;
	double num2 = 0;
	double num3 = 0;
	System.out.println("Hey citizen 1! What is your earning this year?:");
	double a = input.nextDouble();

	System.out.println("Hey citizen 2! What is your earning this year?:");
	double b = input.nextDouble();

	System.out.println("Hey citizen 3! What is your earning this year?:");
	double c = input.nextDouble();

	if(a<=30000){
	num1 = a*0.15;
	System.out.printf("Your total tax is %.2f",num1);
	}if(a<=30000){
	num2 = b*0.15;
	System.out.printf("Your total tax is %.2f",num2);
	num2 = b*0.15;
	System.out.printf("Your total tax is %.2f",num2);

}
	


}
}