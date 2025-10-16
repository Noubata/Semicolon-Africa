def deposit():
	choice1 = 0
	sum = 0
	while choice1 !=0:
		print("minimum deposit: 10")
		amount = float(input("Enter deposit amount: "))
		print("")
		if amount >= 10:
			sum+=amount
			print(f'Deposited: {sum}||New balance: {sum}')
			to_back = int(input("0.Back: "))
		else:
			print("Enter an amount above 10")
def withdraw():
	choice = 0
	while choice !=-1:
		print("minimum withdraw: 5")
		to_withdraw = float(input("Enter withdrawal amount: "))
		print("")
		if amount >= 5:
			difference = amount - to_withdraw
			print(f'Withdrew: {to_withdraw}||New balance: {difference}')
			to_back = int(input("0.Back: "))
		else:
			print("Enter an amount above 5")
	
def transactions():
	print("Transaction so far: ")
	print(f'Deposited: {amount}||New balance: {amount}')
	print(f'Withdrew: {amount}||New balance: {difference}')

def exit():
	amount = 0
	print("")
	print(f'final balance: {amount}')
	print("Thanks for using Log App!")
	return ""
