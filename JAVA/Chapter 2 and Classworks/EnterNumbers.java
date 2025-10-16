/*Pseudocode
- Prompt the user to enter three numbers that should be assigned to these variables: a, b, c.
- declare a variable named largest equals to variable a;
- check if b is greater than variable largest then state that largest equals b;
- check if c is greater than variable largest then state that largest equals c;
- print largest.

import java.util.Scanner;
	public class EnterNumbers{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	System.out.println("Enter the first number:");
	int a = input.nextInt();
	System.out.println("Enter the second number:");
	int b = input.nextInt();
	System.out.println("Enter the third number:");
	int c = input.nextInt();

	int largest = b;
	if(b>largest){
	largest=b;
	} if(c>largest){
	largest=c;
	}
	System.out.printf("the largest number is %d%n", largest);
}
}

*/


/*pseudocode

- Prompt the user to enter his age that should be assigned to age
- Check if the the number is greater than or equals to 0 and lesser than or equals to 12 then print "child". if not,
- Check if the the number is greater than or equals to 13 and lesser than or equals to 19 then print "teen". if not,
- Check if the the number is greater than or equals to 20 and lesser than or equals to 59 then print "adult". if not,
- Check if the the number is greater than or equals to 60, print "senior"


import java.util.Scanner;
	public class EnterNumbers{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	System.out.println("Enter your age:");
	int age = input.nextInt();

	if(age>=0&&age<=12){
	System.out.println("Child");
	}else if(age>=13&&age<=19){
	System.out.println("Teen");
	}else if(age>=20&&age<=59){
	System.out.println("Adult");
	}else if(age>=60){
	System.out.println("Senior");
	}
}
}
*/



/*pseudocode

- Prompt the user to enter the temperature in celsius that should be assigned to temperature
- Check if the the number is lesser than 0, print "Freezing". if not,
- Check if the the number is greater than or equals to 0 and lesser than or equals to 15 then print "cold". if not,
- Check if the the number is greater than or equals to 16 and lesser than or equals to 25, print "warm". if not,
- Check if the the number is greater than 25, print "hot"


import java.util.Scanner;
	public class EnterNumbers{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	System.out.println("Enter your the temperature:");
	int temperature = input.nextInt();

	if(temperature<0){
	System.out.println("Freezing");
	}else if(temperature>=0&&temperature<=15){
	System.out.println("cold");
	}else if(temperature>=16&&temperature<=25){
	System.out.println("Warm");
	}else if(temperature>25){
	System.out.println("Hot");
	}
}
}

*/
/*pseudocode

- Prompt the user to enter a number that should be assigned to a.
- Check if the the number is divisible by 2, print "Even". if not,
- Check if the the number is not divisible by 2, print "Odd";
- print "Invalid" if the input is no a number.


import java.util.Scanner;
	public class EnterNumbers{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	System.out.println("Enter a number:");
	int a = input.nextInt();

	if(a%2==0){
	System.out.println("Even");
	}else if(a%2 !=0){
	System.out.println("Odd");
	}else{
	System.out.println("Invalid");
	}

}
}

*/


/*pseudocode

- Prompt the user to enter a grade between A to F that should be assigned to a.
- Check if the the grade is between A to D, print "Passed". if not,
- Check if the grade is F, print "Failed";
- print "Invalid" if the input is not between the range.


import java.util.Scanner;
	public class EnterNumbers{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	System.out.println("Enter a grade between A to F:");
	char a = input.next().charAt(0);
	

	if(a>='A'&&a<='D'){
	System.out.println("Passed");
	}else if(a=='F'){
	System.out.println("failed");
	}else{
	System.out.println("Invalid");
	}

}
}

*/

/*pseudocode

- Prompt the user to enter the number of hours and hourly rate that should be assigned to a and b.
- declare a variable total that is equals to 0;
- Check if the the number is over 40, call total that should be equals to a times b times 1.5, print "total pay". if not,
- Multiply a and b assign it to total, print "total pay".


import java.util.Scanner;
	public class EnterNumbers{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	System.out.println("Enter the number of hours:");
	double a = input.nextDouble();
	System.out.println("Enter the houry rate:");
	double b = input.nextDouble();
	double total =0;

	if(a>40){
	total = a*1.5*b;
	System.out.printf("Total pay: %.2f%n", total);
	}else{
	total= a*b;
	System.out.printf("Total pay: %.2f%n", total);
	}

}
}
*/
/*pseudocode

- Prompt the user to Enter attendance percentage and average score that should be assigned to a and b.
- Check if the the a and b are greater than or equals to 75, print Elegible. if not,
- print "Not eligible".


import java.util.Scanner;
	public class EnterNumbers{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	System.out.println("Enter your attendance percentage:");
	int a = input.nextInt();
	System.out.println("Enter your average score:");
	int b = input.nextInt();

	if(a+b>=75){
	System.out.println("Eligible");
	}else{
	System.out.println("Not eligible");
	}

}
}

*/
/*pseudocode

- Prompt the user to enter a number that should be assigned to a.
- Check if the the number is divisible by 2 equals 0 and a greater than 0, print "positive even". if not,
- Check if the the number is divisible by 2 not equals 0 and a greater than 0, print "positive odd". if not,
- Check if the the number is divisible by 2 not equals 0 and a lesser than 0, print "Negative odd". if not,
- Check if the the number is not divisible by 2, print "Odd";
- print "Negative even".


import java.util.Scanner;
	public class EnterNumbers{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	System.out.println("Enter a number:");
	int a = input.nextInt();

	if(a%2==0&&a>0){
	System.out.println("Positive even");
	}else if(a%2!=0&&a>0){
	System.out.println("Positive odd");
	}else if(a%2!=0&&a<0){
	System.out.println("Negative odd");
	}else{
	System.out.println("Negative even");
	}

}
}
*/

/*pseudocode

- Prompt the user to enter his bank account balance that should be assigned to a.
- Check if the the number is lesser than 100, print "Low";
- Check if the the number is greater than or equals to 100 and lesser than or equals to 1000,print "Medium";
- check if the number is greater than 1000, print "High".


import java.util.Scanner;
	public class EnterNumbers{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	System.out.println("Enter your bank account balance:");
	int a = input.nextInt();

	if(a<100){
	System.out.println("Low");
	}else if(a>=100&&a<=1000){
	System.out.println("Medium");
	}else if(a>1000){
	System.out.println("High");
	}

}
}
*/

/*pseudocode

- Prompt the user to enter a number that should be assigned to a.
- Check if the the number is divisible by 3 and divisible 5, print "Divisible by both". if not,
- Check if the the number is divisible by 3, print "divisible by 3";
- Check if the the number is divisible by 5, print "divisible by 5";
- Check if the the number is not divisible by 3 and not divisible 5, print "not divisible";


import java.util.Scanner;
	public class EnterNumbers{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	System.out.println("Enter a number:");
	int a = input.nextInt();


	if(a%3==0&&a%5==0){
	System.out.println("Divisible by both");
	}else if(a%3==0){
	System.out.println("Divisible by 3");
	}else if(a%5==0){
	System.out.println("Divisible by 5");
	}else{
	System.out.println("Not divisible");
	
	}

}
}
*/

	 public class EnterNumbers {
   public static void main(String[] args) {
	System.out.println("Enter -1 if you want to stop");
       int x = 0;
       int total = 0;
       int y = 0;
       while (x <= -1) {
          x++;
         total += y;
         System.out.printf("Y is: %d and total is %d\n", y, total);
      }// end while 
  }// end main  
 } //

