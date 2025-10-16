def my_discount(price, pourcentage):
	discount = price*pourcentage/100
	my_price = price-discount
	return my_price
print(my_discount(150, 15))