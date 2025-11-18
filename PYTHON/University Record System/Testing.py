import unittest
from functions import *

class Testing(unittest.TestCase):

	def test_that_the_function_returns_a dictionary(self):

		actual = infos_collection("Beny", 2, "Math", "City", "Zipcode")
		expected = {"name": "Beny", "age": 4, "course": "Math", "Address": {"city": "lagos", "zipcode" : "semicolon-12-a"}
	self.assertEquals(actual, expected)



