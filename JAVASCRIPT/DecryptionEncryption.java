import java.util.Scanner;

public class DecryptionEncryption{
public static void main(String[]args){
Scanner collectInput = new Scanner(System.in);

System.out.print("Enter first encrypted digit: ");
double userInputOne = collectInput.nextDouble();

System.out.print("Enter second encrypted digit: ");
double userInputTwo = collectInput.nextDouble();

System.out.print("Enter third encrypted digit: ");
double userInputThree = collectInput.nextDouble();

System.out.print("Enter fourth encrypted digit: ");
double userInputFour = collectInput.nextDouble();

double toReplaceOne = (userInputOne * 10)-7;
double toReplaceTwo = (userInputTwo * 10)-7;
double toReplaceThree = (userInputThree *10)-7;
double toReplaceFour = (userInputFour * 10)-7;

userInputOne = toReplaceThree;
userInputTwo = toReplaceFour;
userInputThree = toReplaceOne;
userInputFour = toReplaceTwo;


System.out.printf("the encrypt data in digit is: %.0f-%.0f-%.0f-%.0f", userInputOne, userInputTwo, userInputThree, userInputFour);




}

}