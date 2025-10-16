public class SumEvenNumber{
public static void main (String[]args){

int number = 2345;
int toSeparate = 0;
int sum =0;
int toCheck = 0;
while (toCheck < 5)
	toCheck+=1;
	toSeparate = number%10;
	number = (number-(number%10))/10;
	if (number % 2 == 0){
		sum+=number;
	}
System.out.print(sum);
}
}