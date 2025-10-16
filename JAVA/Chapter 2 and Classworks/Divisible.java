public class Divisible{
	public static void main (String[]args){
	int a = 1;
	int b = 0;

	while(a<=30){
	a++;
	if(a%3==0){
	b+=a;
	}
}
	System.out.printf("The total is %d", b);
}
}