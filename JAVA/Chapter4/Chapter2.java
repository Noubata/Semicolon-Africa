/*
4.10- The similarity between if single selection statement and while irritation statement is that both of them use conditional expression to execute a code. 	Also,  they control flow of a condition. But the difference is that while if single selection statement execute a code at once if the condition is 	true or false, the while irritation statement execute code repeatedly as long as the condition remains true.
4.11- To avoid the outcome of dividing integer by another one we use the data type double which can contain decimal number.
4.12- The two ways in which control statements can be combined are control statement stacking and control statement nesting. Control statement stacking 	consists of connecting the exit state point of 	one diagram to the entry state point of the next diagram. and the control statement nesting is a 	control in which one control appears inside another such as if...else inside another if...else.
4.13-  Type of repetition that would be appropriate for obtaining an input from the user until the user indicates there is no more input to provide is called 	sentinel value. This lets the user the amount of the input he wants until himself decides to stop it. The user can stop a statement by using a special 	value called sentinel or signal value. And the type that would be appropriate for calculating
 	the factorial of 5 is counter controlled irritation. this control statement fixes a number of time a number should be calculated in advance.
4.14-  If integers x and y are set to 7 and 3, the value of x is 3 after x = y++ and 4 x = ++y
4.15-  Identify and correct the errors in each of the following pieces of code. [Note: There may be
 	more than one error in each piece of code].

a) 	if (age >= 65);
	System.out.println("Age is greater than or equal to 65");
 	else
	System.out.println("Age is less than 65)"; 
	in this code the string is outside of the close parenthese and all the method System.out. should be inside curly braces this will not work unless we 	put just after 65.just like:
	 if (age >= 65){
   	System.out.println("Age is greater than or equal to 65");
 	else
   	System.out.println("Age is less than 65"); 
	}

b)	int x == 1, total == 0;
 	while (x <= 10) {
    	total ++x;
    	System.out.println(x);
 	} 
	this code will have a syntax error because the x and the variable are declared the wrong way. here is the right way to do it.
	int x = 1;
	int total = 0;
 	while (x <= 10) {
    	total = ++x;
    	System.out.println(x);
 	} 

c)	while (x <= 100)
   	total += x;
   	++x;
	this lack the output that should be print, we have not declare any variable that should assigned to total and x. 

	int total = 0;
	int x = 0;
	while (x <= 100){
   	total = ++x;
   	System.out.println(x);
	}

d)	while (y =! 0){ 
	System.out.println (y);
	}
	this code need a variable declaration and curly braces
	int y= 1;
	while (y != 0){ 
	y+=y;
	System.out.println (y);
	}

4.16-  What does the following program print?

       public class EnterNumbers {
       public static void main(String[] args) {
       int x = -2;
       int total = 0;
 
       while (x <= 10) {
          int y = x + 2;
          x++;
         total += y;
       System.out.printf("Y is: %d and total is %d\n", y, total);
      }
      }
      } 
      This code prints the value of Y and total. it repeat gradually from 0 to 12 for Y and for total, it adds each value to the existing one from 0 to 13

4.17- For Exercise 4.17 through Exercise4.20, perform each of the following steps:
*/
	/*Pseudocode
	
	- Prompt the user to enter miles driven and gallons used that should be assigned to a and b;
	- Declare a variable c using decimal class and add the addition of a and b to it.
	- Print c

	*/
import java.util.Scanner;

public class Chapter2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int mile = 0;
        int gallons = 0;
        int miles = 0;

        System.out.println("Enter -1 for miles to stop.");
	System.out.print("Enter your miles driven: ");
            miles = input.nextInt();
        while (miles != -1) {
            

            if (miles == -1) {
                if (gallons == 0) {
                    System.out.println("No trips recorded.");
                } else {
                    double combined=  mile / gallons;
                    System.out.printf("Final combined MPG: %.2f%n", combined);
                }
                
            }

            System.out.print("Enter your gallons used: ");
            int gallon = input.nextInt();

            mile += miles;
            gallons += gallon;

            double mpg =  miles / gallon;
            double combined = (double) mile / gallons;

            System.out.printf("MPG for this trip: %.2f%n", mpg);
            System.out.printf("Combined MPG: %.2f%n", combined);
        }
    }
}

/*pseudocode

- prompt the user to enter his account number, assigned it to a variable;
- prompt the user to enter his balance at the beginning of the month, assigned it to b variable;
- declare a c variable which is equals to 0;
- 
*/



import java.util.Scanner;
	public class EnterNumbers{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	System.out.println("Enter a number:");
	int a = input.nextInt();

