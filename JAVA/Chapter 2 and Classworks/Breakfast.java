import java.util.Scanner;
	public class Breakfast{
	public static void main(String[]args){

	Scanner input = new Scanner(System.in);

	System.out.println("Enter first student name: ");
	String name1 = input.nextLine();
	System.out.print("Enter student Score: ");
	int Score1 = input.nextInt();

	
	System.out.println("Enter Second student name: ");
	String name2 = input.next();
	System.out.print("Enter student Score: ");
	int Score2 = input.nextInt();

	System.out.println("Enter third student name: ");
	String name3 = input.next();
	System.out.println("Enter student Score: ");
	int Score3 = input.nextInt();

	int highest = Score1;
	if (Score2>highest){
	highest=Score2;
	} if (Score3>highest){
	highest = Score3;
	}

	int smallest = Score1;
	if (Score2<smallest){
	smallest=Score2;
	} if (Score3<smallest){
	smallest = Score3;
	}


	System.out.println("The smallest score is "+ smallest);
	System.out.println("The highest score is "+ highest);
	
}
}