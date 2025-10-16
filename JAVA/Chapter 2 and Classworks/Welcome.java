import java.util.Scanner;

public class CircleCalculations {
public static void main(String[] args) {
Scanner input = new Scanner(System.in);
// Prompt user for radius
System.out.print("Enter the radius of the circle: ");
int radius = input.nextInt();
// Print diameter (as integer)
System.out.printf("Diameter: %d%n", 2 * radius);
// Print circumference using Math.PI
System.out.printf("Circumference: %.2f%n", 2 * Math.PI * radius);
// Print area using Math.PI
System.out.printf("Area: %.2f%n", Math.PI * radius * radius);
}
}
