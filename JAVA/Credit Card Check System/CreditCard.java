import java.util.*;
import java.math.BigInteger;
public class CreditCard{

	public static ArrayList<Integer> getEachSecondDigit(long cardNumber){

		ArrayList<Integer> separatedDigitPackage = new ArrayList<>();
		String toString = String.valueOf(cardNumber);
		for(int check = toString.length() - 2; check > 0; check-=2){
			char eachDigit = toString.charAt(check);
			int digitValue = Character.getNumericValue(eachDigit); 
			separatedDigitPackage.add(digitValue);
		}
	return separatedDigitPackage;
	}

	public static ArrayList<Integer> DoubleSecondDigit (ArrayList<Integer> separatedDigitPackage){

		ArrayList<Integer> doubled = new ArrayList<>();
		for(int check = 0; check < separatedDigitPackage.size(); check++){
			doubled.add(separatedDigitPackage.get(check) * 2);
		
		}
		return doubled;
	}

	public static ArrayList<Integer> getEachSingleDigit(ArrayList<Integer> doubled){

		ArrayList<Integer> newList = new ArrayList<>();
		for(int number = 0; number < doubled.size(); number++){
			if (doubled.get(number) <= 9 ){
			newList.add(doubled.get(number));
			}else{
			int digit1 = doubled.get(number) % 10;
			int digit2 = doubled.get(number) /10;	
			int sumOfMyDigits = digit1+digit2;
			newList.add(sumOfMyDigits);
			}
		}
		
		return newList;

	}

	public static int addUpAllElements(ArrayList<Integer> newList){

		int sumOfAllNumbers = 0;
		for(int check = 0; check < newList.size(); check++){
			sumOfAllNumbers +=newList.get(check);
	
		}
		return sumOfAllNumbers;
	}

	public static int addUpAllOddNumbersFromTheInput(long cardNumber){

		String toString = String.valueOf(cardNumber);
		int sumOfOddNumbers = 0;
		for(int check = toString.length() - 1; check > 0; check-=2){
			char eachDigit = toString.charAt(check);
			int digitValue = Character.getNumericValue(eachDigit); 
			sumOfOddNumbers+=digitValue;
		}
	return sumOfOddNumbers;
	}

	public static int sumOfSums(int sumOfAllNumbers, int sumOfOddNumbers){

		int theSum = sumOfAllNumbers + sumOfOddNumbers;
				
		return theSum;
	}

	public static boolean checkValidation(int theSum){

		if(theSum%10==0){
		return true;
		}else{		
		return false;
		}
	}


}