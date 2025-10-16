import java.util.Scanner;
	public class Paper{
	public static void main(String[]args){
	Scanner input = new Scanner(System.in);
	System.out.println("You are playing a game, choose a number scissor(0), rock(1), paper(2)" );
	double number = input.nextDouble();
	
	//double random = Math.random()*2;
	if(number==1){
	System.out.println("Omo no be lie, You guessed right! The computer is paper. You are rock, you win am.");
	}
	if(number==0){
	System.out.println("The computer it is a paper, you are a paper! It is draw.");
	}
	if(number==2){
	System.out.println("Opps! Oga, you failed am oo.");
	}
	
}

}