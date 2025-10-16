import java.util.Scanner;

public class Beny {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("BMI Calculator");
        System.out.println("Choose unit system: ");
        System.out.println("1. Pounds & Inches");
        System.out.println("2. Kilograms & Meters");
        int choice = sc.nextInt();

        double bmi = 0;

        if (choice == 1) {
            System.out.print("Enter weight in pounds: ");
            double weightInPounds = sc.nextDouble();

            System.out.print("Enter height in inches: ");
            double heightInInches = sc.nextDouble();

            bmi = (703 * weightInPounds) / (heightInInches * heightInInches);

        } else if (choice == 2) {
            System.out.print("Enter weight in kilograms: ");
            double weightInKg = sc.nextDouble();

            System.out.print("Enter height in meters: ");
            double heightInMeters = sc.nextDouble();

            bmi = weightInKg / (heightInMeters * heightInMeters);
        } else {
            System.out.println("Invalid choice.");
            return;
        }

        // Print BMI
        System.out.printf("Your BMI is: %.2f\n", bmi);

        // Print category
        if (bmi < 18.5) {
            System.out.println("Category: Underweight");
        } else if (bmi < 25) {
            System.out.println("Category: Normal weight");
        } else if (bmi < 30) {
            System.out.println("Category: Overweight");
        } else {
            System.out.println("Category: Obesity");
        }

        // Display official categories
        System.out.println("\nBMI Categories (NHLBI):");
        System.out.println("Underweight: less than 18.5");
        System.out.println("Normal:      18.5 – 24.9");
        System.out.println("Overweight:  25 – 29.9");
        System.out.println("Obesity:     30 or greater");

    }
}
