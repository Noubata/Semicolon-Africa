import java.util.Scanner;

public class Comparing {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int positive = 0;
        int negative = 0;
        int zero = 0;

        System.out.print("Enter first number: ");
        int n1 = sc.nextInt();
        if (n1 > 0) { positive++; System.out.println(n1 + " is positive"); }
        else if (n1 < 0) { negative++; System.out.println(n1 + " is negative"); }
        else { zero++; System.out.println(n1 + " is zero"); }

        System.out.print("Enter second number: ");
        int n2 = sc.nextInt();
        if (n2 > 0) { positive++; System.out.println(n2 + " is positive"); }
        else if (n2 < 0) { negative++; System.out.println(n2 + " is negative"); }
        else { zero++; System.out.println(n2 + " is zero"); }

        System.out.print("Enter third number: ");
        int n3 = sc.nextInt();
        if (n3 > 0) { positive++; System.out.println(n3 + " is positive"); }
        else if (n3 < 0) { negative++; System.out.println(n3 + " is negative"); }
        else { zero++; System.out.println(n3 + " is zero"); }

        System.out.print("Enter fourth number: ");
        int n4 = sc.nextInt();
        if (n4 > 0) { positive++; System.out.println(n4 + " is positive"); }
        else if (n4 < 0) { negative++; System.out.println(n4 + " is negative"); }
        else { zero++; System.out.println(n4 + " is zero"); }

        System.out.print("Enter fifth number: ");
        int n5 = sc.nextInt();
        if (n5 > 0) { positive++; System.out.println(n5 + " is positive"); }
        else if (n5 < 0) { negative++; System.out.println(n5 + " is negative"); }
        else { zero++; System.out.println(n5 + " is zero"); }

        // Print summary
        System.out.println("\nSummary:");
        System.out.println("Positive numbers: " + positive);
        System.out.println("Negative numbers: " + negative);
        System.out.println("Zeros: " + zero);

        sc.close();
    }
}
