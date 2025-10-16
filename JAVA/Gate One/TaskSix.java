public class TaskSix{
public static void main(String[]args){

	int number = 0;
	int number1 = 0;
	int number2 = 0;
	int number3 = 0;
	int number4 = 0;

	while(number < 10){
	number++;

	if (number % 4 == 0){
	
	
	number1 = number*number;
	number2 = number1*number;
	number3 = number2*number;
	number4 = number3*number;
	
	System.out.printf("%d %d %d %d %d%n", number, number1, number2, number3, number4);
	}
	
	
	}

	
}
}