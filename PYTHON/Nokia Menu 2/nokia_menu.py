choice = 0
while choice != 14:
	print ('Welcome to this Nokia menu map ')
	print('1 - Phone book')
	print('2 - Messages')
	print('3 - Chat')
	print('4 - Call register')
	print('5 - Tones')
	print('6 - Settings')
	print('7 - Call divert')
	print('8 - Games')
	print('9 - Calculator')
	print('10 - Reminders')
	print('11 - Clock')
	print('12 - Profiles')
	print('13 - SIM services')
	print('14 - Back')
	choice = int(input('Enter your option: '))
	
	match choice:

		case 1:
			first_choice = 0
			while first_choice != 11:	
				print("====Phone book====")
				print("1. Search")
				print("2. Service Nos")
				print("3. Add name")
				print("4. Erase")
				print("5. Edit")
				print("6. Assign Tone")
				print("7. Send b' card")
				print("8. Options")
				print("9. Speed dials")
				print("10. Voice tags")
				print("11. back")
				first_choice = int(input("Enter your choice: "))	
				
				match first_choice :
				
					case 1:
						under_first_choice = 0
						while under_first_choice != 2:
							print("1. Search")
							print("2. Back")
							under_first_choice = int(input("Enter 2 to quit: "))
							if under_first_choice == 2:
								break
							
					case 2:
						under_second_choice = 0
						while under_second_choice != 3:
							print("2. Service Nos")
							print("3. Back")
							under_second_choice = int(input("Enter 3 to quit: "))
							if under_second_choice ==3:
								break
					case 3:
						under_third_choice = 0
						while under_third_choice != 4:
							print("3. Add name")
							print("4. Back")
							under_third_choice = int(input("Enter 4 to quit: "))
							if under_third_choice == 4:
								break
					case 4:
						under_fourth_choice = 0
						while under_fourth_choice != 5:
							print("4. Erase")
							print("5. Back")
							under_fourth_choice = int(input("Enter 5 to quit: "))
							if under_fourth_choice == 5:
								break
					case 5:
						under_fifth_choice = 0
						while under_fifth_choice != 6:
							print("5. Edit")
							print("6. Back")
							under_fifth_choice = int(input("Enter 6 to quit: "))
							if under_fifth_choice == 6:
								break
					case 6:
						under_sixth_choice = 0
						while under_sixth_choice != 7:
							print("6. Assign Tone")
							print("7. Back")
							under_sixth_choice = int(input("Enter 7 to quit: "))
							if under_sixth_choice == 7:
								break
					case 7:
						under_seventh_choice = 0
						while under_seventh_choice != 8:
							print("7. Send b' card")
							print("8. Back")
							under_seventh_choice = int(input("Enter 8 to quit: "))
							if under_seventh_choice == 8:
								break
					case 8:
						under_eightth_choice = 0
						while under_eightth_choice != 9:
							print("8. Options")
							print("1. Type of view")
							print("2. Memory status")
							print("9. Back")
							under_eightth_choice = int(input("Enter your choice: "))
							if under_eightth_choice == 9:
								break
							match under_eightth_choice:
								case 1:
									under_eight1 = 0
									while under_eight1 != 2:
										print("1. Type of view")
										under_eight1 = int(input("Enter 2 to quit: "))
										if under_eight1 == 2:
											break
								case 2:
									under_eight2 = 0
									while under_eight2 != 3:
										print("2. Memory status")
										under_eight2 = int(input("Enter 3 to quit: "))
										if under_eight2 == 3:
											break
					case 9:
						under_nineth_choice = 0
						while under_nineth_choice != 10:
							print("9. Speed dials")
							print("10. Back")
							under_nineth_choice = int(input("Enter 10 to quit: "))
							if under_nineth_choice == 10:
								break
					case 10:
						under_tenth_choice = 0
						while under_tenth_choice != 11:
							print("10. Voice tags")
							print("11. Back")
							under_tenth_choice = int(input("Enter 11 to quit: "))
							if under_tenth_choice == 11:
								break
						break

		case 2:
			second_choice = 0
			while second_choice != 11:
				print("====Messages====")
				print("1. Write messages")
				print("2. Inbox")
				print("3. Outbox")
				print("4. Picture messages")
				print("5. Templates")
				print("6. Smileys")
				print("7. Messages settngs")
				print("8. Info service")
				print("9. Voice mailbox number")
				print("10. Service command editor")
				print("11. Back")
				second_choice = int(input("Enter your choice: "))
				match second_choice:
					case 1:
						under_one = 0
						while under_one !=2:
							print("1. Write messages")
							print("2 Back: ")
							under_one = int(input("Enter 2 to quit: "))
							if under_one == 2:
								break
					case 2:
						under_two = 0
						while under_two !=3:
							print("2. Inbox")
							print("3 Back: ")
							under_two = int(input("Enter 3 to quit: "))
							if under_two == 3:
								break
					case 3:
						under_three = 0
						while under_three !=4:
							print("3. Outbox")
							print("4 Back: ")
							under_three = int(input("Enter 4 to quit: "))
							if under_three == 4:
								break
					case 4:
						under_four = 0
						while under_four !=5:
							print("4. Picture messages")
							print("5 Back: ")
							under_four = int(input("Enter 5 to quit: "))
							if under_four == 5:
								break
					case 5:
						under_five = 0
						while under_five !=6:
							print("5. Templates")
							print("6 Back: ")
							under_five = int(input("Enter 6 to quit: "))
							if under_five == 6:
								break
					case 6:
						under_six = 0
						while under_six !=7:
							print("6. Smileys")
							print("7 Back: ")
							under_six = int(input("Enter 7 to quit: "))
							if under_six == 7:
								break
					case 7:
						under_seven = 0
						while under_seven !=8:
							print("7. Messages settngs")
							#print("8 Back: ")
							print("1. Set 1")
							print("2. Common")
							match under_seven:
								case 1:
									under_seven1 = 0
									while under_seven1 != 4:
										print("Set 1")
										print("1. Message centre number")
										print("2. Message sent as")
										print("3. Message validity")
										print("4. Back")
										under_seven1 = int(input("Enter your choice: "))
										if under_seven1 == 4:
											break
									
								case 2:
									under_seven2 = 0
									while under_seven2 != 4:
										print("Common")
										print("1. Delivery reports")
										print("2. Reply via same centre")
										print("3. Character support")
										print("4. Back")
										under_seven2 = int(input("Enter your choice: "))
										if under_seven2 == 4:
											break
							under_seven = int(input("Enter 8 to quit: "))
							if under_seven == 8:
								break
					case 8:
						under_eight = 0
						while under_eight !=9:
							print("8. Info service")
							print("9 Back: ")
							under_eight = int(input("Enter 9 to quit: "))
							if under_eight == 9:
								break
					case 9:
						under_nine = 0
						while under_nine !=10:
							print("9. Voice mailbox number")
							print("10 Back: ")
							under_nine = int(input("Enter 10 to quit: "))
							if under_nine == 10:
								break
					case 10:
						under_ten = 0
						while under_ten !=11:
							print("10. Service command editor")
							print("11. Back: ")
							under_ten = int(input("Enter 11 to quit: "))
							if under_ten == 11:
								break
						break
		case 3:
			print("Chat")
		case 4:
			fourth_choice = 0
			while fourth_choice != 9:
				print("====Call register====")
				print("1. Missed calls")
				print("2. Received calls")
				print("3. Dialled numbers")
				print("4. Erase recent call lists")
				print("5. Show call duration")
				print("6. Show call cost")
				print("7. Call cost settings")
				print("8. Prepaid credit")
				print("9. Back")
				fourth_choice = int(input("Enter 9 to quit: "))
				match fourth_choice:
					case 1:
						under_fourth1 = 0
						while under_fourth1 != 2:
							print("1. Missed calls")
							print("2. Back")
							under_fourth1 = int(input("Enter 2 to quit: "))
							if under_fourth1 == 2:
								break
					case 2:
						under_fourth2 = 0
						while under_fourth2 != 3:
							print("2. Received calls")
							print("3. Back")
							under_fourth2 = int(input("Enter 3 to quit: "))
							if under_fourth2 == 3:
								break
					case 3:
						under_fourth3 = 0
						while under_fourth3 != 4:
							print("3. Dialled numbers")
							print("4. Back")
							under_fourth3 = int(input("Enter 4 to quit: "))
							if under_fourth3 ==4:
								break
					case 4:
						under_fourth4 = 0
						while under_fourth4 != 5:
							print("4. Erase recent call lists")
							print("5. Back")
							under_fourth4 = int(input("Enter 5 to quit: "))
							if under_fourth4 == 5:
								break
					case 5:
						under_fourth5 = 0
						while under_fourth5 != 6:
							print("5. Show call duration")
							print("1. Last call duration")
							print("2. All call's duration")
							print("3. Received call's duration")
							print("4. Dialled call's duration")
							print("5. Clear timers")
							print("6. Back")
							under_fourth5 = int(input("Enter 6 to quit: "))
							if under_fourth5 == 6:
								break
							match under_fourth5:
								case 1:
									under_fourth51 = 0
									while under_fourth51 != 2:
										print("1. Last call duration")
										print("2. Back")
										under_fourth51 = int(input("Enter 2 to quit: "))
										if under_fourth51 == 2:	
											break
								case 2:
								
									under_fourth52 = 0
									while under_fourth52 != 2:
										print("1. All call's duration")
										print("2. Back")
										under_fourth52 = int(input("Enter 2 to quit: "))
										if under_fourth52 == 2:	
											break
								case 3:
								
									under_fourth53 = 0
									while under_fourth53 != 2:
										print("1. Received call's duration")
										print("2. Back")
										under_fourth53 = int(input("Enter 2 to quit: "))
										if under_fourth53 == 2:	
											break
								case 4:
								
									under_fourth54 = 0
									while under_fourth54 != 2:
										print("1. Dialled call's duration")
										print("2. Back")
										under_fourth54 = int(input("Enter 2 to quit: "))
										if under_fourth54 == 2:	
											break
								case 5:
								
									under_fourth55 = 0
									while under_fourth55 != 2:
										print("1. Clear timers")
										print("2. Back")
										under_fourth55 = int(input("Enter 2 to quit: "))
										if under_fourth55 == 2:	
											break					
					case 6:
						under_fourth6 = 0
						while under_fourth6 != 7:
							print("6. Show call cost")
							print("1. Last call's cost")
							print("2. All call's cost")
							print("3. Clear counters")
							print("7. Back")
							under_fourth6 = int(input("Enter 7 to quit: "))
							if under_fourth6 == 7:
								break
							match under_fourth6:
								case 1:
									under_fourth61 = 0
									while under_fourth61 != 2:
										print("1. Last call's cost")
										print("2. Back")
										under_fourth61 = int(input("Enter 2 to quit: "))
										if under_fourth61 == 2:
											break
								case 2:	
									under_fourth62 = 0
									while under_fourth62 != 2:
										print("2.All call's cost")
										print("2. Back")
										under_fourth62 = int(input("Enter 2 to quit: "))
										if under_fourth62 == 2:
											break
								case 3:
									under_fourth63 = 0
									while under_fourth63 != 2:
										print("3. Clear counters")
										print("2. Back")
										under_fourth63 = int(input("Enter 2 to quit: "))
										if under_fourth63 == 2:
											break
					case 7:
						under_fourth7 = 0
						while under_fourth7 != 8:
							print("7. Cost call settings")
							print("1. Call cost limit")
							print("2. Show cost in")
							print("8. Back")
							under_fourth7 = int(input("Enter 8 to quit: "))
							if under_fourth7 == 8:
								break
							match under_fourth7:
								case 1:
									under_fourth71 = 0
									while under_fourth71 != 2:
										print("1. Call cost limit")
										print("2. Back")
										under_fourth71 = int(input("Enter 2 to quit: "))
										if under_fourth71 == 2:
											break
								case 2:
									under_fourth72 = 0
									while under_fourth72 != 2:
										print("1. Show cost in")
										print("2. Back")
										under_fourth72 = int(input("Enter 2 to quit: "))
										if under_fourth72 == 2:
											break
					case 8:
						under_fourth8 = 0
						while under_fourth8 != 9:
							print("8. Prepaid credit")
							print("9. Back")
							under_fourth8 = int(input("Enter 9 to quit: "))
							if under_fourth8 == 9:
								break
						break
		case 5:
			fifth_choice = 0
			while fifth_choice != 10:
				print("====Tones====")
				print("1. Ringing tone")
				print("2. Ringing volume")
				print("3. Incoming call alert")
				print("4. Composer")
				print("5. Message alert tone")
				print("6. Keypad tones")
				print("7. Warning and game tones")
				print("8. Vibrating alert")
				print("9. Screen saver")
				print("10. Back")
				fifth_choice = int(input("Enter 10 to quit: "))
				if fifth_choice == 10:
					break
				match fifth_choice:
					case 1:
						fifth_choice1 = 0
						while fifth_choice1 != 2:
							print("1. Ringing Tone")
							print("2. Back")
							fifth_choice1 = int(input("Enter 2 to quit"))
							if fifth_choice1 == 2:
								break
					case 2:
						fifth_choice3 = 0
						while fifth_choice3 != 2:
							print("1. Ringing volume")
							print("2. Back")
							fifth_choice3 = int(input("Enter 2 to quit"))
							if fifth_choice3 == 2:
								break
					case 3:
						fifth_choice3 = 0
						while fifth_choice3 != 2:
							print("1. Incoming call alert")
							print("2. Back")
							fifth_choice3 = int(input("Enter 2 to quit"))
							if fifth_choice3 == 2:
								break
					case 4:
						fifth_choice4 = 0
						while fifth_choice4 != 2:
							print("1. Composer")
							print("2. Back")
							fifth_choice4 = int(input("Enter 2 to quit"))
							if fifth_choice4 == 2:
								break
					case 5:
						fifth_choice5 = 0
						while fifth_choice5 != 2:
							print("1. Message alert tone")
							print("2. Back")
							fifth_choice5 = int(input("Enter 2 to quit"))
							if fifth_choice5 == 2:
								break
					case 6:
						fifth_choice6 = 0
						while fifth_choice6 != 2:
							print("1. Keypad tones")
							print("2. Back")
							fifth_choice6 = int(input("Enter 2 to quit"))
							if fifth_choice6 == 2:
								break
					case 7:
						fifth_choice7 = 0
						while fifth_choice7 != 2:
							print("1. Warning and game tones")
							print("2. Back")
							fifth_choice7 = int(input("Enter 2 to quit"))
							if fifth_choice7 == 2:
								break
					case 8:
						fifth_choice8 = 0
						while fifth_choice8 != 2:
							print("1. Vibrating alert")
							print("2. Back")
							fifth_choice8 = int(input("Enter 2 to quit"))
							if fifth_choice8 == 2:
								break
					case 9:
						fifth_choice9 = 0
						while fifth_choice9 != 2:
							print("1. Screen saver")
							print("2. Back")
							fifth_choice9 = int(input("Enter 2 to quit"))
							if fifth_choice9 == 2:
								break
						break
		case 6:
			sixth_choice = 0
			while sixth_choice != 9:
				print("====Settings====")
				print("1. Call settings")
				print("2. Phone settings")
				print("3. Security settings")
				print("4. Rsetore factory settings")
				sixth_choice = int(input("Enter 9 to quit: "))
				if sixth_choice == 9:
					break
				match sixth_choice :
					case 1:
						sixth_choice1 = 0
						while sixth_choice1 != 7:
							print("Call settings")
							print("1. Automatic redial")
							print("2. Speed dialing")
							print("3. Call waiting action")
							print("4. Own number sending")
							print("5. Phone line in use")
							print("6. Automatic answer")
							print("7. Back")
							sixth_choice1 = int(input("Enter your choice: "))
							match sixth_choice1 :
								case 1:
									sixth_choice11 = 0
									while sixth_choice11 != 2:
										print("1. Automatic redial")
										print("2. Back")
										sixth_choice11 = int(input("Enter 2 to quit: "))
										if sixth_choice11 == 2:
											break
								case 2:
									sixth_choice12 = 0
									while sixth_choice12 != 2:
										print("1. Speed dialing")
										print("2. Back")
										sixth_choice12 = int(input("Enter 2 to quit: "))
										if sixth_choice12 == 2:
											break
								case 3:
									sixth_choice13 = 0
									while sixth_choice13 != 2:
										print("1. Call waiting options")
										print("2. Back")
										sixth_choice13 = int(input("Enter 2 to quit: "))
										if sixth_choice13 == 2:
											break
								case 4:
									sixth_choice14 = 0
									while sixth_choice14 != 2:
										print("1. Own number sending")
										print("2. Back")
										sixth_choice14 = int(input("Enter 2 to quit: "))
										if sixth_choice14 == 2:
											break
								case 5:
									sixth_choice15 = 0
									while sixth_choice15 != 2:
										print("1. Phone line in use")
										print("2. Back")
										sixth_choice15 = int(input("Enter 2 to quit: "))
										if sixth_choice15 == 2:
											break
								case 6:
									sixth_choice16 = 0
									while sixth_choice16 != 2:
										print("1. Automatic answer")
										print("2. Back")
										sixth_choice16 = int(input("Enter 2 to quit: "))
										if sixth_choice16 == 2:
											break
								
							
					case 2:
						sixth_choice2 = 0
						while sixth_choice2 != 7:
							print("Phone settings")
							print("1. Language")
							print("2. Cell info display")
							print("3. Welcome note")
							print("4. Network selection")
							print("5. Lights")
							print("6. Condirm SIM service actions")
							print("7. Back")
							sixth_choice2 = int(input("Enter your choice: "))
							match sixth_choice2 :
								case 1:
									sixth_choice21 = 0
									while sixth_choice21 != 2:
										print("1. Language")
										print("2. Back")
										sixth_choice21 = int(input("Enter 2 to quit: "))
										if sixth_choice21 == 2:
											break
								case 2:
									sixth_choice22 = 0
									while sixth_choice22 != 2:
										print("1. Cell info display")
										print("2. Back")
										sixth_choice22 = int(input("Enter 2 to quit: "))
										if sixth_choice22 == 2:
											break
								case 3:
									sixth_choice23 = 0
									while sixth_choice23 != 2:
										print("1. Welcome Note")
										print("2. Back")
										sixth_choice23 = int(input("Enter 2 to quit: "))
										if sixth_choice23 == 2:
											break
								case 4:
									sixth_choice24 = 0
									while sixth_choice24 != 2:
										print("1. Network selection")
										print("2. Back")
										sixth_choice24 = int(input("Enter 2 to quit: "))
										if sixth_choice24 == 2:
											break
								case 5:
									sixth_choice25 = 0
									while sixth_choice25 != 2:
										print("1. Lights")
										print("2. Back")
										sixth_choice25 = int(input("Enter 2 to quit: "))
										if sixth_choice25 == 2:
											break
								case 6:
									sixth_choice26 = 0
									while sixth_choice26 != 2:
										print("1. Confirm SIM service actions")
										print("2. Back")
										sixth_choice26 = int(input("Enter 2 to quit: "))
										if sixth_choice26 == 2:
											break
					case 3:
						sixth_choice3 = 0
						while sixth_choice3 != 7:
							print("Security settings")
							print("1. PIN code request")
							print("2. Call barring service")
							print("3. Fixed dialing")
							print("4. Closed user group")
							print("5. Phone security")
							print("6. Change access codes")
							print("7. Back")
							sixth_choice3 = int(input("Enter your choice: "))
							match sixth_choice3 :
								case 1:
									sixth_choice31 = 0
									while sixth_choice31 != 2:
										print("1. PIN code request")
										print("2. Back")
										sixth_choice31 = int(input("Enter 2 to quit: "))
										if sixth_choice31 == 2:
											break
								case 2:
									sixth_choice32 = 0
									while sixth_choice32 != 2:
										print("1. Call barring service")
										print("2. Back")
										sixth_choice32 = int(input("Enter 2 to quit: "))
										if sixth_choice32 == 2:
											break
								case 3:
									sixth_choice33 = 0
									while sixth_choice33 != 2:
										print("1. Fixed dialing")
										print("2. Back")
										sixth_choice33 = int(input("Enter 2 to quit: "))
										if sixth_choice33 == 2:
											break
								case 4:
									sixth_choice34 = 0
									while sixth_choice34 != 2:
										print("1. Closed user group")
										print("2. Back")
										sixth_choice34 = int(input("Enter 2 to quit: "))
										if sixth_choice34 == 2:
											break
								case 5:
									sixth_choice35 = 0
									while sixth_choice35 != 2:
										print("1. Phone security")
										print("2. Back")
										sixth_choice35 = int(input("Enter 2 to quit: "))
										if sixth_choice35 == 2:
											break
								case 6:
									sixth_choice36 = 0
									while sixth_choice36 != 2:
										print("1. Change access code")
										print("2. Back")
										sixth_choice36 = int(input("Enter 2 to quit: "))
										if sixth_choice36 == 2:
											break
					case 4:
						sixth_choice4 = 0
						while sixth_choice4 != 1:
							print("Rsetore factory settings")
							print("1. Back")
							sixth_choice4 = int(input("Enter 1 to quit: "))
							if sixth_choice4 == 1:
								break
						break
		case 7:
			seven_choice = 0
			while seven_choice != 2:
				print("1. Call divert")
				print("2. Back")
				eight_choice = int(input("Enter 2 to quit: "))
				if seven_choice == 2:
					break
		case 8:
			eight_choice = 0
			while eight_choice != 2:
				print("1. Games")
				print("2. Back")
				eight_choice = int(input("Enter 2 to quit: "))
				if eight_choice == 2:
					break
		case 9:
			nine_choice = 0
			while nine_choice != 2:
				print("1. Calculator")
				print("2. Back")
				nine_choice = int(input("Enter 2 to quit: "))
				if nine_choice == 2:
					break
		case 10:
			ten_choice = 0
			while ten_choice != 2:
				print("1. Reminders")
				print("2. Back")
				ten_choice = int(input("Enter 2 to quit: "))
				if ten_choice == 2:
					break
		case 11:
			eleventh_choice = 0
			while eleventh_choice != 7:
				print("====Clock====")
				print("1. Alarm clock")
				print("2. Clock settings")
				print("3. Date settings")
				print("4. Stopwatch")
				print("5. Countdown timer")
				print("6. Auto update of date and time")
				print("7. Back ")
				eleventh_choice = int(input("Enter your choice"))
				match eleventh_choice:
					case 1:
						eleventh_choice1 = 0
						while eleventh_choice1 != 2:
							print("1. Alarm clock")
							print("2. Back")
							eleventh_choice1 = int(input("Enter 2 to quit: "))
							if eleventh_choice1 == 2:
								break
					case 2:
						eleventh_choice2 = 0
						while eleventh_choice2 != 2:
							print("1. Clock settings")
							print("2. Back")
							eleventh_choice2 = int(input("Enter 2 to quit: "))
							if eleventh_choice2 == 2:
								break
					case 3:
						eleventh_choice3 = 0
						while eleventh_choice3 != 2:
							print("1. Date settings")
							print("2. Back")
							eleventh_choice3 = int(input("Enter 2 to quit: "))
							if eleventh_choice3 == 2:
								break
					case 4:
						eleventh_choice4 = 0
						while eleventh_choice4 != 2:
							print("1. Stopwatch")
							print("2. Back")
							eleventh_choice4 = int(input("Enter 2 to quit: "))
							if eleventh_choice4 == 2:
								break
					case 5:
						eleventh_choice5 = 0
						while eleventh_choice5 != 2:
							print("1. Countdown timer")
							print("2. Back")
							eleventh_choice5 = int(input("Enter 2 to quit: "))
							if eleventh_choice5 == 2:
								break
					case 6:
						eleventh_choice6 = 0
						while eleventh_choice6 != 2:
							print("1. Auto update of date and time")
							print("2. Back")
							eleventh_choice6 = int(input("Enter 2 to quit: "))
							if eleventh_choice6 == 2:
								break

						break
		case 12:
			twelfth_choice = 0
			while twelfth_choice != 2:
				print("1. Profiles")
				print("2. Back")
				twelfth_choice = int(input("Enter 2 to quit: "))
				if twelfth_choice == 2:
						break
		case 13:
			thirtennth_choice = 0
			while thirtennth_choice != 2:
				print("1. SIM services")
				print("2. Back")
				thirtennth_choice = int(input("Enter 2 to quit: "))
				if thirtennth_choice == 2:
					break
		case _:
			print("Au revoir!!!")
