amount = 0

difference = 0
def deposit(): 
	
	while True:
		print("minimum deposit: 10")
		to_back = print('0.back')
		amount = float(input("Enter deposit amount: "))
		account_balance = 0
		print("")
		if amount >= 10:
			account_balance+=amount
			print(f'Deposited: {amount}||New balance: {account_balance}')
		elif amount == 0:
			break
		else:
			print("Invalid!! Enter an amount above 10")
		
	return amount

def withdraw(amount):
	while True:
		print("minimum withdraw: 5")
		to_withdraw = float(input("Enter withdrawal amount: "))
		print("")
		if amount >= 5:
			difference = amount - to_withdraw
			print(f'Withdrew: {to_withdraw} || New balance: {difference}')
			to_back = int(input("0.Back: "))
		elif amount == 0:
			break
		else:
			print("Invalid!! Enter an amount above 5")
	
def transactions(amount):
	print("Transaction so far: ")
	print(f'Deposited: {amount} || New balance: {amount}')
	print(f'Withdrew: {amount} || New balance: {difference}')

def exit(amount):
	amount = 0
	print("")
	print(f'final balance: {amount}')
	print("Thanks for using Log App!")
	return ""
