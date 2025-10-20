transactions_container = []

def save_transaction(product, price, quantity):
	transactions_container.append({
	"product": 'product',
	price : 20,
	quantity : 1200
})

def buy():
	
	print("""
	1 -> Diesel --- 600/liter
	2 -> Gas --- 500/liter
	""")
	user_input = int(input("Enter your choice: "))
	
	match user_input :

		case 1 : 
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


			if choice == 'amount' :
			
				print("Amount must be above a liter price !!")
				price = int(input("How much Diesel are you buying (550/L) : "))

				if price < 600 :
					print("Oga, una no hear again ?? Amount must be above a liter price")
				else :
					quantity = price/ 600
					if type(quantity) == float:
						exact_quantity = int(quantity)
						decimal_part = quantity - exact_quantity
						
						print("Product : Diesel")
						print("Amount :", price)
						print("Liters :", exact_quantity)
						print("Change :",decimal_part)
						print("Thank you for your patronage")
					else :
						print("Product : Diesel")
						print("Amount :", price)
						print("Liters :", quantity)
						print("Thank you for your patronage")





		case 2 :
		 
			choice = input("Liter or Amount: ").lower()
			
			if choice == 'liter' :
				print("Liters must be between 1-50 !!")
				quantity = int(input("How many liters of Gas are you buying(500/L) : "))
				
				if quantity < 1 :
					print("Oga, una no hear again ?? Liters must be between 1-50 !!")
				else :
					amount = quantity * 500
					
					print("Product : Gas")
					
					print("Amount : #",amount)

					print("Liters :", quantity, "L")

					print("Thank you for patronage")


			if choice == 'amount' :
				print("Amount must be above a liter price !!")
				price = int(input("How much Gas are you buying (500/L) : "))

				if price < 500 :
					print("Oga, una no hear again ?? Amount must be above a liter price")
				else :
					quantity = price/ 500
					if type(quantity) == float:
						exact_quantity = int(quantity)
						decimal_part = quantity - exact_quantity
						
						print("Product : Diesel")
						print("Amount :", price)
						print("Liters :", exact_quantity)
						print("Change :", decimal_part)
						print("Thank you for your patronage")
					else :
						print("Product : Diesel")
						print("Amount :", price)
						print("Liters :", quantity)
						print("Thank you for your patronage")


	return user_input



def transaction_history():

	print("\n=== All transactions ===")

	if len(transactions_container) == 0:
		print("Oga, no transactions naww.")
	else:
		to_iterate = 0
		while to_iterate < len(transactions_container):
			index = transactions_container[to_iterate]
			print(str(to_iterate + 1) + ". Product: " + index["product"] + ", Liters: " + str(index["price"]) + ", Amount: ₦" + str(index["quantity"]))
		sum = sum + 1
	print("============================\n")
	

buy()



