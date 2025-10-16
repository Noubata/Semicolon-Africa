/*Pseudocode 4.17
	
	- Prompt the user to enter miles driven and gallons used that should be assigned to a and b;
	- Declare a variable c using decimal class and add the addition of a and b to it.
	- Print c

	*/

import java.util.Scanner;
	public class Important{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	int totalMiles = 0;
	int totalGallons = 0;

	System.out.println("Enter your miles driven");
	int trip = input.nextInt();
	while(trip != -1){
	System.out.println("Enter your gallons used");
	double gallons = input.nextInt();
	totalMiles+=trip;
	totalGallons+=gallons;

	double all = (double) trip/gallons;
	double combined = (double) totalMiles/totalGallons;

	//System.out.printf("the MPG is %.2f%n", all);
	//System.out.printf("the MPG combined is %.2f%n", combined);
	
	System.out.println("Enter your miles driven");
	trip = input.nextInt();

	if(totalGallons == 0){
	
	System.out.println("No trips recorded.");
	}else{
	//System.out.printf("your MPG combined is %.2f%n", (double)totalMiles/totalGallons);
	}
}

}

}

/*pseudocode 4.18
- Prompt the user to enter their account number, beginning balance, monthly charges, and credits, which should be assigned to a, b, c, & d, respectively.
- Create a variable e, which we will add the beginning balance to charges, and then subtract credits. Then display the e as the new balance.
- Check if e exceeds our user’s credit limit, if so display “credit limit exceeded”.

import java.util.Scanner;
	public class Ast{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	System.out.print("Enter your account number(only 8 digits):");
	int a = input.nextInt();
	System.out.print("Enter your beginning balance:");
	int b = input.nextInt();
	System.out.print("What are your charges this month:");
	int c = input.nextInt();
	System.out.print("What is your credit:");
	int d = input.nextInt();
	
	int e = b+c-d;
	System.out.printf("Your new balance is %d%n", e);
	if(e>=d){
	System.out.println("Your new balance exceeds your credit");
	}else{
	System.out.print("Credit limit exceeded.");
	}
	
}

}

*/

/*pseudocode

- Declare four variables b, c, d and e where each of the first two is equal to 0 and the last two are equal to 200 and 0.09, respectively.
- prompt the user to enter the amount the items sold, assign this variable ent;
- while ent is not equal to 1, calculate the user income by multiplying e and b then add it to d all assigned to c variable.
- print the total.

import java.util.Scanner;
	public class Ast{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	double b = 0;
	double c = 0;
	double d = 200;
	double e = 0.09;
	System.out.println("Enter the items sold");
	double ent = input.nextDouble();
	while(ent != -1){
	
	b+=ent;
	c = d+(e*b);
	System.out.println("Enter the items sold(enter -1 to get the final total)");
	ent = input.nextDouble();

	}
	System.out.printf("Your income is %.2f%n",c);
}
}
*/
