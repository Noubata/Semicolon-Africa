import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import java.util.*;
import java.math.BigInteger;

public class TestCreditCard{

	@Test
	public void testThatEverySecondDigitIsSeparated(){

	CreditCard user = new CreditCard ();

	ArrayList<Integer> actual = user.getEachSecondDigit(8544552412234987L);
	
	ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(8, 4, 2, 1, 2, 5, 4));

	assertEquals(expected, actual);
	}

	@Test
	public void testThatEverySecondDigitSeparatedisDoubled(){

	CreditCard user = new CreditCard ();
	
	ArrayList<Integer> toPass = new ArrayList<>();	

	toPass.add(1);
	toPass.add(2);
	toPass.add(3);
	toPass.add(4);
	

	ArrayList<Integer> actual = user.DoubleSecondDigit(toPass);
	
	ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(2, 4, 6, 8));

	assertEquals(expected, actual);
	}

	@Test
	public void testThatGetEachSingleDigitNumber(){

	CreditCard user = new CreditCard ();

	ArrayList<Integer> singleDigit = new ArrayList<>();	

	singleDigit.add(6);
	singleDigit.add(10);
	singleDigit.add(22);
	singleDigit.add(27);

	ArrayList<Integer> actual = user.getEachSingleDigit(singleDigit);
	
	ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(6, 1, 4, 9));

	assertEquals(expected, actual);
	}
	

	@Test
	public void testThatAllDoubledDigitAreAddedTogether(){

	CreditCard user = new CreditCard ();

	ArrayList<Integer> toSumUp = new ArrayList<>();	

	toSumUp.add(6);
	toSumUp.add(8);
	toSumUp.add(-5);
	toSumUp.add(2);

	int actual = user.addUpAllElements(toSumUp);
	
	int expected = 11;

	assertEquals(expected, actual);
	}

	@Test
	public void testThatEveryEveryOddDigitIsAddedUp(){

	CreditCard user = new CreditCard ();

	int actual = user.addUpAllOddNumbersFromTheInput(8544552412234987L);
	
	int expected = 39;

	assertEquals(expected, actual);
	}

	@Test
	public void testToAddUpAllSumOfOddsAndSumOfDoubledDigit(){

	CreditCard user = new CreditCard ();

	int actual = user.sumOfSums(13, 22);
	
	int expected = 35;

	assertEquals(expected, actual);
	}

	@Test
	public void testThatTheInputIsValid(){

	CreditCard user = new CreditCard ();

	boolean actual = user.checkValidation(40);
	
	boolean expected = true;

	assertEquals(expected, actual);
	}

}