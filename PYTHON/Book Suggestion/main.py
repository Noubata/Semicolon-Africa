from book import *
my_books = []
#a_book = 0
while True:

	print("""

	=== Welcome to the Book Suggestion System ===

		 1. Get Suggestions
 		 2. Add Book
 		 3. Remove Book
 		 4. Update book 
		 5. Show all books

	""")
	choice = int(input("Enter your choice: "))

	match choice:

		case 1:
			suggest_books()
		case 2:
			a_book = input("Add a book: ")
			add_books(my_books, a_book)