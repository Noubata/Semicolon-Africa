/*Pseudocode
- declare a variable called number that equals to 0;
- use iteration process to check if number is less than or equals to 5;
- increase number by 1;
- use iteration process to check if number is less than or equals to 25;
- multiply number by 2;
- use iteration process to check if number is less than or equals to 125;
- multiply number by 3;
- use iteration process to check if number is less than or equals to 125;
- multiply number by 3;
- use iteration process to check if number is less than or equals to 625;
- multiply number by 4;
*/

import java.util.Scanner;
	public class Tabular{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	
	int number = 0;

	while(number<5){
	number++;
	System.out.println(number);
	}
	while(number<5){
	number*=2;
	System.out.println(number);
	}
	
}
}