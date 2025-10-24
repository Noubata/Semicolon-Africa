from log_app import *

account_balance = 0
transactions = []
while True:

	print("""
	Welcome to Transaction LOG APP
	
	1. Deposit money
	2. Withdraw
	3. Transaction Histoty
	4. Exit
	
	""")
	choice = int(input("Enter your choice: "))
	match choice :

		case 1:
			prompt = int(input("Enter your amount: "))
			account_balance = deposit(prompt, account_balance, transactions)
			print(f"New balance{account_balance}")
		case 2:
			prompt = int(input("Enter your amount: "))
			account_balance = withdraw(prompt, account_balance, transactions)
			print(f"New balance{account_balance}")
		case 3:
			transaction(transactions)
		case 4:
			exit()
			break