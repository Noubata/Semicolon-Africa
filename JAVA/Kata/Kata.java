public class Kata{

	public static boolean isEven(int number){

	if (number % 2 == 0){
	return true;
	}else{
	return false;
	}
	}

	public static boolean isPrime(int number){

	if (number == 1 || number == 3 || number == 5 || number == 7 || number == 11 || number == 13){

		return true;
	}else if (number % 1 == 0 || number % 3 == 0 || number % 5 == 0 || number % 7 == 0 || number % 11 == 0 || number % 13 == 0){
		return false;
	}else{
		return true;
	}

	}
	
	public static long factorialOf(int number){
	long total = 1;
	while(number > 0){
	
	total = total*number;
	number--;
	}
	return total;
	}

	public static boolean isPalindrome(int number){
	
	if(number < 0){
	return false;
	}
	int divisor = 0;
	int toStore = 0;
	while(number != 0){
	divisor = number%10;
	toStore = toStore*10+divisor;
	number/=10;
	}
	return true;
	}

	public static long squareOf(int number){
	
	return (long) Math.pow(number, 2);
	}
	
	public static int subtract(int number1, int number2){
	
	int difference = number1-number2;
	
	if (difference > 0){
	return difference;
	}else{
	return difference*(-1);
	}
	}

	public static int factorOf(int number){

	int count = 0;
	int nobetheDivisor = 0;
	while(nobetheDivisor <= number){
	nobetheDivisor++;
	if(number % nobetheDivisor == 0){
	count++;
	}
	}
	return count;
	}

	public static boolean isSquare(int number){
	
	if(number%Math.sqrt(number)==0){
	return true;
	}else{
	return false;
	}
	
	}

	public static float divide(int number1, int number2){

	int count = 0;
	if(number2==0){
	return 0;
	}
	int result = 0;
	result = number1/number2;
	return result;
	}
}



