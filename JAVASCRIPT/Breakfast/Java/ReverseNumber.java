public class ReverseNumber{
public static void main(String[]args){

int reverse = 234;
int times = 0;

for(int number = 0; number <=2; number++){
times = reverse%10;
reverse = (reverse-(reverse%10))/10;
System.out.print(times);
}
}

}