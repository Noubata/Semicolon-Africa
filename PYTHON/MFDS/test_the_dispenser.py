import unittest
from the_dispenser import *

transactions = []

class TestTheDispenser(unittest.TestCase):
	def test_buy_diesel_amount(self):
		result = buy_diesel('amount', 1800, transactions)
		self.assertIsNone(result)

	def test_buy_gas_amount(self):
		result = buy_gas('amount', 2500, transactions)
		self.assertIsNone(result)

	def test_buy_petrol_amount(self):
		result = buy_petrol('amount', 1350, transactions)
		self.assertIsNone(result)

	def test_buy_kerozene_amount(self):
		result = buy_kerozene('amount', 2100, transactions)
		self.assertIsNone(result)

	def test_show_transaction(self):
		result = show_transaction(transactions)
		self.assertIsNone(result)
