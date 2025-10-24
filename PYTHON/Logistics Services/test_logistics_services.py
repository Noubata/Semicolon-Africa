import unittest
from logistics_services import delivery

class TestLogisticsServices(unittest.TestCase):

	def test_that_the_function_only_takes_integer(self):

		try:
			delivery(" ", 0.0)
			print("Only numbers are allowed")
		except:
			print("allowed")
	def test_that_the_function_returns_calculated_amount_when_less_than_50_percentage(self):
	
		actual_amount = delivery(40)
		expected_amount = 11400
		self.assertEqual(actual_amount, expected_amount)
	
	def test_that_the_function_returns_calculated_amount_when_between_50_and_59_percentage(self):
	
		actual_amount = delivery(50)
		expected_amount = 15000
		self.assertEqual(actual_amount, expected_amount)

	def test_that_the_function_returns_calculated_amount_when_between_60_and_69_percentage(self):
	
		actual_amount = delivery(60)
		expected_amount = 20000
		self.assertEqual(actual_amount, expected_amount)

	def test_that_the_function_returns_calculated_amount_when_greater_than_or_equal_to_70_percentage(self):
	
		actual_amount = delivery(70)
		expected_amount = 40000
		self.assertEqual(actual_amount, expected_amount)





