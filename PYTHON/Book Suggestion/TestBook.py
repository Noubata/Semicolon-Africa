import unittest
from Book import suggest_books

class TestBook(unittest.TestCase):

	def test_that_it_keeps_suggesting (self):
	
		actual = suggest_books('')
		expected = suggest_books(str)
		self.assertEqual(actual, expected)