import unittest
from book import suggest_books

class TestBook(unittest.TestCase):

	def test_that_suggest_books_is_not_empty (self):

		actual_number = suggest_books(1)
		expected_output = 1
		self.assertEqual(actual_number, expected_output)
	
	def  test_that_t