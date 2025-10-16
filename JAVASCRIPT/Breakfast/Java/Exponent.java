import math .
public class Exponent{
public static void main	(String[]args){
int base = 5;
int number = 0;
int theExponent = 0;
while (number <=1){
	number+=1;
	theExponent = Math.pow(base, 2);
}
System.out.print(theExponent);
}
}