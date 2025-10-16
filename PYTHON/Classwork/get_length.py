import string
def get_time(number):
	
	secondes = number*60
	hour = number/60
	return (secondes, hour)

print(get_time(30))



def get_length(the_word):
	
	to_addd = 0
	for bb in the_word:
		to_addd+=1
	return to_addd

print(get_length('blue'))