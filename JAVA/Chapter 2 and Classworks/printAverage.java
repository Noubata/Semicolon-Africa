import java.util.Scanner;
public class PrintAverage{
public static void main(String[]args){
Scanner userInput = new Scanner(System.in);
int sum = 0;
int[] score = new int [10];

for(int numbers=0; numbers<10; numbers++){
System.out.print("Enter number: ");
score[numbers] = userInput.nextInt();
}
for(int i =0; i<10; i++){
sum+=score[i];
}
System.out.print(sum/score.length);

}
}