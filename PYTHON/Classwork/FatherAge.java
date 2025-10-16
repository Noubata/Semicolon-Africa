/*pseudocode
prompt the user to enter his father's age and his own age, assign them to each to father age and my age, respectively;
check if the two ages are greater than 80 or less than 0, if so display your age should be between 1 to 80;
declare my age2 variable that equals to my age multiplied by 2;
declare years variable that equals to father age minus my age2;
check if years is greater than or equal to 0, display your father was your age  years(the answer got) years ago;
check if years is less than or 0, display your father will be your age  in years(the answer got). make sure the result remains positive;

*/

import java.util.Scanner;
	public class FatherAge{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	System.out.println("Enter your father's age: ");
	int papaAge = input.nextInt();
	System.out.println("Enter your age: ");
	int myAge = input.nextInt();
	
	int myAge2 = myAge * 2;
	int years = papaAge - myAge2;
	int times = years*(-1);

	if (papaAge || myAge > 0){
	System.out.println(" ");
	}else{
	System.out.println("Your age should be between 1 to 80");
	}

	if (years >= 0){
	System.out.printf("Your father  was twice as old as you %d years ago\n", years );
	}
	if (years < 0){
	System.out.printf("Your father will be twice as old than you  in %d", times);
	}
}
}




