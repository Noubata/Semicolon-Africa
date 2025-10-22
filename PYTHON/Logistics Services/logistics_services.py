def delivery(successful_delivery):

	if type(successful_delivery) != int:
		raise TypeError("Only integers are allowed")
	elif successful_delivery < 50:
		return successful_delivery * 160 + 5000
	elif successful_delivery >= 50 and successful_delivery <= 59:
		return successful_delivery * 200 + 5000
	elif successful_delivery >= 60 and successful_delivery <= 69:
		return successful_delivery * 250 + 5000
	elif successful_delivery >= 70:
		return successful_delivery * 500 + 5000
	