# test_add.py

import unittest
from simplemath import add

class TestAdd(unittest.TestCase):
	def test_add_positive_numbers(self):
		self.assertEqual(add(3, 3), 6)

if __name__ == '__main__':
	unittest.main()

