from log_app import deposit, withdraw, transactions, exit
def log_app(amount, balance=0, transactions=[]):
	
	print("""
	Welcome to Transaction Log App

	
		1 -> Deposit
		2 -> Withdraw
		3 -> Show Transactions
		4 -> Exit
		""")
	print("")
	the_choice = 0
	while the_choice !=-1:
		the_choice+=1
		prompt = int(input("Enter your choice: "))
		
		match prompt:
			case 1:deposit()
			case 2:withdraw()
			case 3:transactions()
			case 4:exit()
	


print(log_app(2500))