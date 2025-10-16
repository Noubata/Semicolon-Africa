public class PrintPrimeNumber{
public static void main(String[]ars){

int number = 0;
int count = 0;
int count1 = 0;
while (number<100){
	number+=1;
	if (number == 1 || number == 3 || number == 5 || number == 7 || number == 11 || number == 13){
		System.out.println(number);
	}
	if (number % 2 !=0 ){
		System.out.println(number);

	}
}
}
}