total_miles = 0
total_gallons = 0
total = 0
gallons = 0	
while gallons != -1:

	gallons = float(input("Enter the gallons used(enter -1 to end): "))
	if gallons == -1:
		break
	miles = float(input("Enter the miles driven: "))	
	total_miles+=miles
	total_gallons+=gallons
	
	total = total_miles/total_gallons

	if total_gallons == 0:
	
		print("No trips recorded.")
	else:
		print("your combined total is", total)
	gallons
	
	
	
