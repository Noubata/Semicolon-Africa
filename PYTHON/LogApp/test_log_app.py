from log_app import deposit, withdraw, transactions, exit
while True:
	account_balance = 0
	amount = float(input("Enter deposit amount: "))
	amount = 0
	print("""
	Welcome to Transaction Log App
		1 -> Deposit
		2 -> Withdraw
		3 -> Show Transactions
		4 -> Exit
		""")
	print("")

	prompt = int(input("Enter your choice: "))
		
	match prompt:
		case 1:deposit()
		case 2:withdraw(amount)
		case 3:transactions(amount)
		case 4:exit(amount)
	


#print(log_app())