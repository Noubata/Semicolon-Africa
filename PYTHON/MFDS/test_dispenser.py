from dispenser import buy, transaction_history
print("""
Welcome to NGONE NGAR, your favorite Chadian Station in Naija
	1 -> Buy petroleum
	2 -> Show Transactions History
""")
choice = int(input("Enter your choice: "))

match choice:

	case 1 : 
		buy()
	case 2 :
		transaction_history()