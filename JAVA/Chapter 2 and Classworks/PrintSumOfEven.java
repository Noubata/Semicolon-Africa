import java.util.Scanner;
public class PrintSumOfEven{
public static void main(String[]args){
Scanner userInput = new Scanner(System.in);
int sum = 0;
int[] score = new int [10];

for(int numbers=0; numbers<10; numbers++){
System.out.print("Enter number: ");
score[numbers] = userInput.nextInt();
}
for(int i =0; i<10; i++){

if(score[i]%2==0){
sum+=score[i];
}
}
System.out.println(sum);
}
}