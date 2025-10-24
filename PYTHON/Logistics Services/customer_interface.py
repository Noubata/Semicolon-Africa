from logistics_services import delivery

while True:

	dashboard = """
	--------------------------------
	|Collection rate|Amount_|BasePay|
	|		|	|	|
	|Less than 50%__|____160|___5000|
	|		|       |	|
	|50-59%_________|____200|___5000|
	|		|       |	|
	|60-69%_________|____250|___5000|
	|		  |	|	|
	|Greater than 70%_|__500|___5000|

	"""
	print(dashboard)
	prompt = int(input("Enter 1 to calculate the wage for the day or 2 to exit: "))
	
	match prompt :
		
		case 1:
			try:
				number = int(input("Enter successful delivery: "))
				print(" ")

				result = delivery(number)	
				print(f"The wage for the day is {result}")

			except ValueError:
				print("Only integer is allowed")
		case 2:
			print(" ")
			print("Thank you for working with us.")
			break