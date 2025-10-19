public class Nested{
public static void main(String[]args){

count = 0;
count1 = 0;
number = 1900;
while (number <= 2025){
	number ++;
	if (number % 4 == 0 && number % 100 != 0){
		count +=1;
	}
	if (number % 4 == 0 && number % 100 == 0 && number % 400 == 0){
		count1 +=1;
	}
System.out.print(count+count1);

}
}
}