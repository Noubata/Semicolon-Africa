import java.util.Scanner;
public class PizzaWahala{
public static void main(String[]args){
Scanner userInput = new Scanner(System.in);

String head1 = "Pizza size";
String head2 = "Number of slides";
String head3 = "Price of box";

String column1 = "Sapa size";
String column2 = "Small money";
String column3 = "Big boys";
String column4 = "Odogwu";

int numberSlides1 = 4;
int numberSlides2 = 6;
int numberSlides3 = 8;
int numberSlides4 = 12;

int priceBox1 = 2500;
int priceBox2 = 2900;
int priceBox3 = 4000;
int priceBox4 = 5200;

System.out.printf("%-15s %-20s %-20s%n", head1, head2, head3);
System.out.println(" ");
System.out.printf("%-15s %-20d %-20d%n", column1, numberSlides1, priceBox1);
System.out.println(" ");
System.out.printf("%-15s %-20d %-20d%n", column2, numberSlides2, priceBox2);
System.out.println(" ");
System.out.printf("%-15s %-20d %-20d%n", column3, numberSlides3, priceBox3);
System.out.println(" ");
System.out.printf("%-15s %-20d %-20d%n", column4, numberSlides4, priceBox4);
System.out.println(" ");

System.out.print("Number of people: ");
int peopleNumber = userInput.nextInt();
System.out.println(" ");
System.out.println("Type of pizza: ");
System.out.println("1. Sapa Size ");
System.out.println("2. Small money");
System.out.println("3. Big boys");
System.out.println("4. Odogwu");
System.out.println(" ");
System.out.print("Please choose a number: ");
int pizzaType = userInput.nextInt();

int boxes =0;
int difference = 0;
int boxesPlus = 0;
int total = 0;
int leftOver = 0;
if(pizzaType==1){
boxes = peopleNumber/4;
if(peopleNumber%4==0 && peopleNumber>=4){
boxes = peopleNumber/4;
total = boxes*2500;
System.out.printf("The number of boxes to buy = %d boxes\n", boxes);
System.out.printf("Price = %d", total);
}else{
boxesPlus = boxes+1;
difference = boxesPlus*4;
leftOver = difference - peopleNumber;
total = boxesPlus*2500;
System.out.printf("The number of boxes to buy =  %d boxes\n", boxesPlus);
System.out.printf("Number left over slices after serving = %d slides\n", leftOver);
System.out.printf("Price = %d", total);
}
}

int boxes1 =0;
int difference1 = 0;
int boxesPlus1 = 0;
int total1 = 0;
int leftOver1 = 0;
if(pizzaType==2){
boxes1 = peopleNumber/6;
if(peopleNumber%6==0 && peopleNumber>=6){
boxes1 = peopleNumber/6;
total1 = boxes1*2900;
System.out.printf("The number of boxes to buy = %d boxes\n", boxes1);
System.out.printf("Price = %d", total1);
}else{
boxesPlus1 = boxes1+1;
difference1 = boxesPlus1*6;
total1 = boxesPlus1*2900;
leftOver1 = difference1 - peopleNumber;
System.out.printf("The number of boxes to buy =  %d boxes\n", boxesPlus1);
System.out.printf("Number left over slices after serving = %d slides\n", leftOver1);
System.out.printf("Price = %d", total1);
}
}

int boxes2 =0;
int difference2 = 0;
int boxesPlus2 = 0;
int total2 = 0;
int leftOver2 = 0;
if(pizzaType==3){
boxes2 = peopleNumber/8;
if(peopleNumber%8==0 && peopleNumber>=8){
boxes2 = peopleNumber/8;
total = boxes1*4000;
System.out.printf("The number of boxes to buy = %d boxes\n", boxes2);
System.out.printf("Price = %d", total2);
}else{
boxesPlus2 = boxes2+1;
difference2 = boxesPlus2*8;
total2 = boxesPlus2*4000;
leftOver2 = difference2 - peopleNumber;
System.out.printf("The number of boxes to buy =  %d boxes\n", boxesPlus2);
System.out.printf("Number left over slices after serving = %d slides\n", leftOver2);
System.out.printf("Price = %d", total2);
}
}

int boxes3 =0;
int difference3 = 0;
int boxesPlus3 = 0;
int total3 = 0;
int leftOver3 = 0;
if(pizzaType==4){
boxes3 = peopleNumber/12;
if(peopleNumber%12==0 && peopleNumber>=12){
boxes3 = peopleNumber/12;
total3 = boxes3*5200;
System.out.printf("The number of boxes to buy = %d boxes\n", boxes3);
System.out.printf("Price = %d", total3);
}else{
boxesPlus3 = boxes3+1;
difference3 = boxesPlus3*12;
total3 = boxesPlus3*5200;
leftOver3 = difference3 - peopleNumber;
System.out.printf("The number of boxes to buy =  %d boxes\n", boxesPlus3);
System.out.printf("Number left over slices after serving = %d slides\n", leftOver3);
System.out.printf("Price = %d", total3);
}
}


}
}



