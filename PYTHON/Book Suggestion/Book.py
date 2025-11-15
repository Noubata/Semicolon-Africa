import random

def suggest_books():
	
	my_books = ("le livre d'Afrique", "Poor Dad Rich Dad", "Java-How to program-Deitel", "JavaScript-Eloquent")

	suggest_it = random.choice(my_books)
	page = random.randrange(1, 90)
	
	print("Book of the day: ", suggest_it)
	
	print("Page: ",page)

	return my_books


def add_books(my_books, a_book):

	my_books.append(a_book)

	return my_books

def remove_books(my_books, book):

	my_books.remove(book)

	return my_books