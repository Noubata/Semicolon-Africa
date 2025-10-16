import java.util.Scanner;

public class Pyramid {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input prompts
        System.out.print("Enter estimated number of stones used: ");
        double stones = sc.nextDouble();

        System.out.print("Enter average weight per stone (in metric tons): ");
        double weightPerStone = sc.nextDouble();

        System.out.print("Enter number of years taken to build (years): ");
        double years = sc.nextDouble();

        // Calculations
        double totalWeightTons = stones * weightPerStone;
        double weightPerYear = totalWeightTons / years;
        double hoursPerYear = 365 * 24;
        double weightPerHour = totalWeightTons / (years * hoursPerYear);
        double weightPerMinute = weightPerHour / 60;

        // Output results
        System.out.printf("%nTotal weight of pyramid: %.2f million tons%n", totalWeightTons / 1_000_000);
        System.out.printf("Estimated mass built per year: %.2f tons/year%n", weightPerYear);
        System.out.printf("Estimated mass built per hour: %.2f tons/hour%n", weightPerHour);
        System.out.printf("Estimated mass built per minute: %.2f tons/minute%n", weightPerMinute);

       
    }
}
