public class CupCakes{
public static int getSmallest(int number1, int number2, int number3, int number4, int number5){

	int [] numbers = {number1, number2, number3, number4, number5};

	int smallest = numbers[0];
	for(int check = 0; check<=4; check++){
	if(numbers[check]<smallest){
	smallest= numbers[check];
	}
	}
	return smallest;
}

public static double averageArray(double number1, double number2, double number3, double number4, double number5){

	double [] numbers = {number1, number2, number3, number4, number5};
	
	int average =0;
	for(int toGet= 0; toGet<=4; toGet++){
	average +=numbers[toGet]/numbers.length;
	}
	return average;
} 

public static int countOccurrence(int number1, int number2, int number3, int number4, int number5){
	
	int sum = 0;
	int [] numbers = {number1, number2, number3, number4, number5};
	for(int toCompare = 0; toCompare<=4; toCompare++){
	if(numbers[toCompare]==1){
	sum+=1;
	}
	}
	return sum;
}

public static boolean containsElement(int number1, int number2, int number3, int number4, int number5 ){

	int [] arrayContainer = {number1, number2, number3, number4, number5};

	//for(int element = 0; element<=4; element++){
	if(arrayContainer[0]==2){
	return true;
	}else if(arrayContainer[1]==2){
	return true;
	}else if(arrayContainer[2]==2){
	return true;
	}else if(arrayContainer[3]==2){
	return true;
	}else if(arrayContainer[4]==2){
	return true;
	}else{
	return false;
	}
}

public static int getFirstElement(int number1, int number2, int number3){

	int [] theBox = {number1, number2, number3};
	int toReturn1 = 0;
	for (int theNumber=0; theNumber<=2; theNumber++){
	if(theBox[theNumber]==0){
	toReturn1 = 0;
	}
	if(theBox[0]>=1){
	toReturn1 = theBox[0];
	}
	}
	return toReturn1;
}

public static int getLastElement(int number1, int number2, int number3){

	int [] theBox = {number1, number2, number3};
	int toReturn1 = 0;
	for (int theNumber=0; theNumber<=2; theNumber++){
	if(theBox[theNumber]==0){
	toReturn1 = 0;
	}
	if(theBox[0]>=1){
	toReturn1 = theBox[2];
	}
	}
	return toReturn1;
 
}

public static int arrayLength(int number1, int number2, int number3, int number4){

	int [] numbers = {number1, number2, number3, number4};
	int counter = 0;
	for(int theLength = 0; theLength <3; theLength++){
	counter = numbers[theLength];
	}
	return counter;
}

public static int getMiddleElement(int number1, int number2, int number3, int number4){

	int [] numbers = {number1, number2, number3, number4};
	
	int toAssign = 0;
	for(int middleNumber=0; middleNumber<=3; middleNumber++){
	if(numbers.length%2==0){
	return toAssign=numbers[1];
	}else{
	return toAssign=numbers[1];
	}
	}
	return toAssign=numbers[1];
}

public static int swapFirstAndLast(int number1, int number2, int number3, int number4){

	int [] numbers = {number1, number2, number3, number4};
	int swap = 0;
	for(int theChange = 0; theChange<3; theChange++){
	swap = numbers[theChange];
	}
	return swap;
}
}



