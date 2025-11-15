import unittest
from book import *

class TestBook(unittest.TestCase):

	def test_that_suggest_books_is_not_empty (self):

		actual = suggest_books()
		expected_output = ("le livre d'Afrique", "Poor Dad Rich Dad", "Java-How to program-Deitel", "JavaScript-Eloquent")
		self.assertEqual(actual, expected_output)

	def test_that_books_can_be_added_to_suggest_books(self):

		a_book = "art of flirting"

		actual = add_books(["key of the world"], a_book)
		expected_output = ["key of the world", "art of flirting"]
		self.assertEqual(actual, expected_output)

	def test_that_books_can_be_removed(self):

		book = "love it"
		book1 = "Book for naija"

		my_list = []

		actual = add_books(my_list, book)
		actual1 = add_books(actual, book1)
		actual2 = remove_books(actual1, book1)
		expected = ["love it"]
		self.assertEqual(actual2, expected)