import java.util.Scanner;
public class NokiaMenu{
public static void main(String[]args){

	String theHead = """
	Welcome to this Nokia menu map
	
		1 - Phone book
		2 - Messages
		3 - Chat
		4 - Call register
		5 - Tones
		6 - Settings
		7 - Call divers
		8 - Games
		9 - Calculator
		10 - Voice tags

	""";

	System.out.println(theHead);
	Scanner gettingIn = new Scanner(System.in);
	System.out.println("Enter your choice");
	int userInput = gettingIn.nextInt();

		switch(userInput){
		
		case 1 : { System.out.println("Phone book");
			System.out.println("1. Search");
			System.out.println("2. Services Nos");
			System.out.println("3. Add name");
			System.out.println("4. Erase");
			System.out.println("5. Edit");
			System.out.println("6. Assign Tone");
			System.out.println("7. Send b'card");
			System.out.println("8. Options:");

					{
					System.out.println("	1. Type of view");
					System.out.println("	2. Memory status");
					}

			System.out.println("9. Speed dials");
			System.out.println("10. Voice tags");
			System.out.println("11. Clock");
			System.out.println("12. Profiles");
			System.out.println("13. SIM services");
		break;}

		case 2 : { System.out.println("Messages");
			System.out.println("1. Write messages");
			System.out.println("2. Inbox");
			System.out.println("3. Outbox");
			System.out.println("4. Pictures");
			System.out.println("5. Templates");
			System.out.println("6. Smileys");
			System.out.println("7. Messages settings");
				{
				System.out.println("	1. Set 1");
					{
					System.out.println("		1. Message centre number");
					System.out.println("		2. Message sent as");
					System.out.println("		3. Message validity");
					}

				System.out.println("	2. Common");
					{
					System.out.println("		1. Delivry reports");
					System.out.println("		2. Reply via same centre");
					System.out.println("		3. Character support");
					}

				}
			System.out.println("8. Infos service");
			System.out.println("9. Voice mailbox number");
			System.out.println("10. Service command editor");
		break;}

		case 3 : { System.out.println("Chat");break;}
		case 4 : { System.out.println("Call register");

			System.out.println("1. Missed calls");
			System.out.println("2. Received calls");
			System.out.println("3. Dialled numbers");
			System.out.println("4. Erase recent call lists");
			System.out.println("5. Show all duration");

				{
				System.out.println("	1. Last call duration");
				System.out.println("	2. All call duration");
				System.out.println("	3. Received calls' duration");
				System.out.println("	4. Dialled calls' duration");
				System.out.println("	5. Clears timers");
				}

			System.out.println("6. Show call cost");

				{
				System.out.println("	1. Last calls' cost");
				System.out.println("	2. All calls' cost");
				System.out.println("	3. Clear counters");
				}

			System.out.println("7. call cost settings");

				{
				System.out.println("	1. Call cost limit");
				System.out.println("	2. Show cost in");
				}
			System.out.println("8. Prepaid credit");


		break;}

		case 5 : { System.out.println("Tones");

				{
				System.out.println("	1. Ringing tone");
				System.out.println("	2. Ringing volume");
				System.out.println("	3. Incoming call alert");
				System.out.println("	4. Composer");
				System.out.println("	5. Messages alert Tones");
				System.out.println("	6. Keyboard Tones");
				System.out.println("	7. Warning and games tones");
				System.out.println("	8. Vibrating alert");
				System.out.println("	9. Screen saver");
				}
		break;}
		case 6 : { System.out.println("Settings");

				{
				System.out.println("	1. Call settings");

					{
					System.out.println("	1. Authomatic radial");
					System.out.println("	2. Speed dialling");
					System.out.println("	3. Call waiting sending");
					System.out.println("	4. Own number sending");
					System.out.println("	5. Phone line in use");
					System.out.println("	6. Authomtic Answer");
					}
				System.out.println("	2. All calls' cost");

					{
					System.out.println("	1. Language");
					System.out.println("	2. Cell info display");
					System.out.println("	3. Welcome note");
					System.out.println("	4. Network selection");
					System.out.println("	5. Lights");
					System.out.println("	6. Confirm SIM services actions");
					}

				System.out.println("	3. Clear counters");

					{
					System.out.println("	1. PIN code requeat");
					System.out.println("	2. Call barring service");
					System.out.println("	3. Fixed dialing");
					System.out.println("	4. Close user group");
					System.out.println("	5. Phone Security");
					System.out.println("	6. Change access codes");
					}

				System.out.println("	4. Clear counters");
					}
		break;}
		case 7 : { System.out.println("Call divert");break;}
		case 8 : { System.out.println("Games");break;}
		case 9 : { System.out.println("Calculator");break;}
		case 10 : { System.out.println("Reminders");break;}
		case 11 : { System.out.println("Clock");

				{
				System.out.println("Alarm clock");
				System.out.println("Clock setting");
				System.out.println("Date setting");
				System.out.println("Stopwatch");
				System.out.println("Countdown timer");
				System.out.println("Auto updatw of date and time");
				}
		break;}
		case 12 : { System.out.println("Profiles");break;}
		case 13 : { System.out.println("SIM services");break;}
	}
}
}