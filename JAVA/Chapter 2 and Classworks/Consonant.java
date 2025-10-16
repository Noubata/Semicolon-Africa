import java.util.Scanner;
	public class Consonant{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	System.out.println("Enter a letter(It should be in uppercase): ");
	char letter = input.next().charAt(0);
	
	char alpha1 = 'A';
	char alpha2 = 'E';
	char alpha3 = 'I';
	char alpha4 = 'O';
	char alpha5 = 'U';
	if (letter == alpha1||letter == alpha2||letter == alpha3||letter == alpha4||letter == alpha5){
	System.out.printf("%c is a vowel", letter);
	}else{
	System.out.printf("%c is a consonant", letter);
	}
}

}