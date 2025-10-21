import unittest
from log_app import *

transactions = []
class test_log_app(unittest.TestCase):

	def test_that_returns_sum(self):
	
		actual = deposit(200, 200, [])
		expected = 400
		self.assertEqual(actual, expected)

	def test_that_withdrawal_returns_output(self):
		
		actual = withdraw(400, 200, [])
		expected = 200
		self.assertEqual(actual, expected)

	def test_transactions(self):
		
		result = transaction(transactions)
		self.assertIsNone(result)
	
	def test_exit(self):

		final_output = exit(transactions)
		self.assertIsNone(final_output)