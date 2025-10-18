my_list = [1, 2, 3, 4, 5, 6]

new = 0
for word in my_list:
	if word % 2 == 0:
		new += word
print(new)