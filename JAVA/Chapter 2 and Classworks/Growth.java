import java.util.Scanner;

public class Growth {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Prompt user inputs
        System.out.print("Enter current world population (: ");
        double currentPopulation = sc.nextDouble();

        System.out.print("Enter annual growth rate: ");
        double growthRatePercent = sc.nextDouble();

        double growthRate = growthRatePercent / 100.0;

        System.out.println("\nEstimated World Population Over the Next 5 Years:");
        for (int year = 1; year <= 5; year++) {
            currentPopulation = currentPopulation * (1 + growthRate);
            System.out.printf("After %d year%s: %.2f billion%n",
                              year, year == 1 ? "" : "s",
                              currentPopulation / 1_000_000_000.0);
        }

    }
}
