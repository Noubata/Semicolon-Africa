def buy_diesel (choice, amount, transactions=[]):
	
	choice = input("Liter or Amount: ").lower()
	if choice == 'liter' :
		print("Liters must be between 1-50 !!")
		quantity = int(input("How many liters of Diesel are you buying(600/L) : "))
			
		if quantity < 1 :
			print("Oga, una no hear again ?? Liters must be between 1-50 !!")
		else :
			amount = quantity * 600
					
			print("Product : Diesel")
			
			print("Amount : #",amount)

			print("Liters :",quantity,"L")

			print("Thank you for patronage")
			transactions.append(amount)

	if choice == 'amount' :
		
		print("Amount must be above a liter price !!")
		price = int(input("How much Diesel are you buying (600/L) : "))
		if price < 600 :
			print("Oga, una no hear again ?? Amount must be above a liter price")
		else :
			quantity = price/ 600
			#transactions += quantity
			if type(quantity) == float:
				exact_quantity = int(quantity)
				decimal_part = (quantity - exact_quantity)*600

				print(" ")	
				print("Product : Diesel")
				print("Amount :", price)
				print("Liters :", exact_quantity)
				print("Change :",decimal_part)
				print("Thank you for your patronage")
			else :
				print(" ")
				print("Product : Diesel")
				print("Amount :", price)
				print("Liters :", quantity)
				print("Thank you for your patronage")
		transactions.append(exact_quantity)


def buy_gas(choice, quantity, transactions=[]):
 
	choice = input("Liter or Amount: ").lower()
		
	if choice == 'liter' :
		print("Liters must be between 1-50 !!")
		quantity = int(input("How many liters of Gas are you buying(500/L) : "))
				
		if quantity < 1 :
			print("Oga, una no hear again ?? Liters must be between 1-50 !!")
		else :
			amount = quantity * 500
			print(" ")
			print("Product : Gas")
					
			print("Amount : #",amount)

			print("Liters :", quantity, "L")

			print("Thank you for patronage")
			transactions.append(exact_quantity)

	if choice == 'amount' :
		print("Amount must be above a liter price !!")
		price = int(input("How much Gas are you buying (500/L) : "))

		if price < 500 :
			print("Oga, una no hear again ?? Amount must be above a liter price")
		else :
			quantity = price/ 500
			if type(quantity) == float:
				exact_quantity = int(quantity)
				decimal_part = (quantity - exact_quantity)*500
				print(" ")
				print("Product : Gas")
				print("Amount :", price)
				print("Liters :", exact_quantity)
				print("Change :", decimal_part)
				print("Thank you for your patronage")
			else :
				print(" ")
				print("Product : Gas")
				print("Amount :", price)
				print("Liters :", quantity)
				print("Thank you for your patronage")
		transactions.append(exact_quantity)

def buy_petrol(choice,quantity, transactions=[]):
 
	choice = input("Liter or Amount: ").lower()
		
	if choice == 'liter' :
		print("Liters must be between 1-50 !!")
		quantity = int(input("How many liters of petrol are you buying(450/L) : "))
				
		if quantity < 1 :
			print("Oga, una no hear again ?? Liters must be between 1-50 !!")
		else :
			amount = quantity * 450
			print(" ")
			print("Product : petrol")
					
			print("Amount : #",amount)

			print("Liters :", quantity, "L")

			print("Thank you for patronage")
		transactions.append(exact_quantity)

	if choice == 'amount' :
		print("Amount must be above a liter price !!")
		price = int(input("How much petrol are you buying (450/L) : "))

		if price < 450 :
			print("Oga, una no hear again ?? Amount must be above a liter price")
		else :
			quantity = price/ 450
			if type(quantity) == float:
				exact_quantity = int(quantity)
				decimal_part = (quantity - exact_quantity)*450
				print(" ")
				print("Product : Petrol")
				print("Amount :", price)
				print("Liters :", exact_quantity)
				print("Change :", decimal_part)
				print("Thank you for your patronage")
			else :
				print(" ")
				print("Product : Petrol")
				print("Amount :", price)
				print("Liters :", quantity)
				print("Thank you for your patronage")
		transactions.append(exact_quantity)

def buy_kerozene(choice, quantity, transactionsc=[]):
 
	choice = input("Liter or Amount: ").lower()
		
	if choice == 'liter' :
		print("Liters must be between 1-50 !!")
		quantity = int(input("How many liters of kerozene are you buying(700/L) : "))
				
		if quantity < 1 :
			print("Oga, una no hear again ?? Liters must be between 1-50 !!")
		else :
			amount = quantity * 700
			print(" ")
			print("Product : kerozene")
					
			print("Amount : #",amount)

			print("Liters :", quantity, "L")

			print("Thank you for patronage")
		transactions.append(exact_quantity)

	if choice == 'amount' :
		print("Amount must be above a liter price !!")
		price = int(input("How much kerozene are you buying (700/L) : "))

		if price < 700 :
			print("Oga, una no hear again ?? Amount must be above a liter price")
		else :
			quantity = price/ 700
			if type(quantity) == float:
				exact_quantity = int(quantity)
				decimal_part = (quantity - exact_quantity)*700
				print(" ")
				print("Product : kerozene")
				print("Amount :", price)
				print("Liters :", exact_quantity)
				print("Change :", decimal_part)
				print("Thank you for your patronage")
			else :
				print(" ")
				print("Product : kerozene")
				print("Amount :", price)
				print("Liters :", quantity)
				print("Thank you for your patronage")
			transactions.append(exact_quantity)

def show_transaction(transactions=[]):

	if len(transactions) > 0 :
		for number in transactions:
			print(number)
	else:
		print("No transactions yet.")

