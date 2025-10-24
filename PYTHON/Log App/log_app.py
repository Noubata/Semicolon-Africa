def deposit(amount, account_balance, transactions = []):
	
	account_balance += amount
	transactions.append(f"Deposited:{amount} | New Balance:{account_balance}")
	
	transactions.append(amount)
	return account_balance

def withdraw(amount, account_balance, transactions = []):
	if amount <= account_balance :
		account_balance = account_balance - amount
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
	
	print(f"Your final balance: {account_balance}")
	print("Thank you for using Transaction LOG APP")