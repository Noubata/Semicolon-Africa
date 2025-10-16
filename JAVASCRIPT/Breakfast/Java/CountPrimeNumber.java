public class CountPrimeNumber{
public static void main(String[]args){

int number = 0;
int count = 0;
int count1 = 0;
while (number<100){
	number+=1;
	if (number == 1 || number == 3 || number == 5 || number == 7 || number == 11 || number == 13){
		count+=1;
	}
	if (number % 2 !=0 ){
		count1+=1;
	}
}
System.out.print(count+count1);

}
}