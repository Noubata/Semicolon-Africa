import java.util.Scanner;

public class EncryptionDecryption{
public static void main(String[]args){
Scanner collectInput = new Scanner(System.in);

System.out.print("Enter first digit: ");
double userInputOne = collectInput.nextDouble();

System.out.print("Enter second digit: ");
double userInputTwo = collectInput.nextDouble();

System.out.print("Enter third digit: ");
double userInputThree = collectInput.nextDouble();

System.out.print("Enter fourth digit: ");
double userInputFour = collectInput.nextDouble();

double toReplaceOne = (userInputOne + 7)/10;
double toReplaceTwo = (userInputTwo + 7)/10;
double toReplaceThree = (userInputThree + 7)/10;
double toReplaceFour = (userInputFour + 7)/10;

userInputOne = toReplaceThree;
userInputTwo = toReplaceFour;
userInputThree = toReplaceOne;
userInputFour = toReplaceTwo;


System.out.printf("the encrypt data in digit is: %.1f-%.1f-%.1f-%.1f", userInputOne, userInputTwo, userInputThree, userInputFour);




}

}