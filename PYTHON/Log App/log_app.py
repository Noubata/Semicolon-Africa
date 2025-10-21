def deposit(amount, account_balance, transactions = []):
	
	account_balance += amount
	transactions.append(f"Deposited:{amount} | New Balance:{account_balance}")
	
	#transactions.append(account_balance)
	return account_balance

def withdraw(amount, account_balance, transactions = []):

	difference = account_balance - amount
	if amount > account_balance :
		 transactions.append(f"Withdrew: ₦{amount} | New Balance: ₦{account_balance}")
	else:
		 "Withdrawal failed: insufficient funds"
	return account_balance
	
def transaction(transactions=[]):
	if len(transactions) > 0 :
		for number in transactions:
			print(number)
	else:
		print("No transactions yet.")

def exit(transactions = []):
	
	print(f"Your final balance: {transactions}")
	print("Thank you for using Transaction LOG APP")