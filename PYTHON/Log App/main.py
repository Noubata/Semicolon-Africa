from log_app import *
def main():
	account = 0
	transactions = []

	menu = 0
	while menu != 0:

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
				deposit(amount, account_balance, transactions = [])
			case 2:
				prompt = int(input("Enter your amount: "))
				withdraw(amount, account_balance, transactions = [])
			case 3:
				transaction(transactions=[])
			case 4:
				exit()
	return 
print(main())