from the_dispenser import *
transactions = []
quantity = 0
amount = 0
while True:
	print("""
	Welcome to NGONE NGAR, your favorite Chadian Station in Naija
		1 -> Buy petroleum
		2 -> Show Transactions History
	""")
	choice = int(input("Enter your choice: "))
	
	match choice:

		case 1 : 
			print("""
			1 . Diesel --- 600/liter
			2 . Gas --- 500/liter
			3 . petrol --- 450/liter
			4 . kerozene --- 700/liter
			""")
			choix = int(input('Enter your choice: '))
			if choix != int:
				raise ValueError("Only numbers are accepted")
		
			match choix:
				case 1:
					buy_diesel (choice,amount, transactions)
				case 2:
					buy_gas(choice,quantity, transactions)
				case 3:
					buy_petrol (choice,quantity, transactions)
				case 4:
					buy_kerozene (choice,quantity, transactions)

		case 2 :
			show_transaction(transactions)
			break