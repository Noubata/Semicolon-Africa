import java.util.Scanner;
public class Coco{
public static void main(String[]args){
Scanner input = new Scanner(System.in);

System.out.println("Enter your name");
String name = input.nextLine();

System.out.println("Age: ");
int age = input.nextInt();

System.out.println("How do you feel today? :");
System.out.println("1-Happy;");
System.out.println("2-Sad;");
System.out.println("3-Excited;");
System.out.println("4-Tired;");
System.out.print("Enter your choice(number only): \n");
int choice = input.nextInt();

System.out.println("Guess a number between 1 to 10");
int guess = input.nextInt();

System.out.println("Want suggestion?");
System.out.println("1-Yes");
System.out.println("2-No");
System.out.println("Choose by entering 1 or 2");
int suggt = input.nextInt();

System.out.println("Hello " + name);

if(age<13){
System.out.println("You are a young explorer!");
}else if(age>=13&&age<=19){
System.out.println("Teen life is fun, Enjoy it!");
}else if(age>=20&&age<=59){
System.out.println("Adulting can be challenging, stay strong!");
}else if(age>=60){
System.out.println("Wisdom looks good on you!");
}else{
System.out.println("Enter a valid age");
}

if(choice==1){
System.out.println("Keep smiling!");
}else if (choice==2){
System.out.println("Cheer up! Tomorrow it's a new day.");
}else if (choice==3){
System.out.println("Awesome! Enjoy your energy!");
}else if (choice==4){
System.out.println("Rest well and recharge!");
}

if(guess==4){
System.out.println("Wow! You guessed it!");
}else{
System.out.println("Try again next time!");
}


if(suggt==1){
System.out.println("Here is a suggestion today: Apart of English, learn French. It will help you travel across the globe!");
}else if (suggt==2){
System.out.println("No worries! I get it bro, have a great day!");
}else{
System.out.print("Please choose a number between 1 or 2");
}

}
}