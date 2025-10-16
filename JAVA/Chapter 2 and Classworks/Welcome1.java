import java.util.Scanner;

//write an addition

public class Welcome1{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
		System.out.println("Entrer le radius du cercle");
		int radius = input.nextInt();
		
// print diameter, circumference, and area

int diameter = 2*radius;
double circumference = 2*Math.PI*radius;
double area = Math.PI*(radius)*2;

System.out.printf("Ton diameter est de %d%n", + diameter);
System.out.printf("Ton circumference est de %f%n ", circumference);
System.out.printf("Ta zone est de %f%n", area);
}

}