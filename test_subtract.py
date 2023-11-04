# test_subtract.py

import unittest
from simplemath import subtract

class TestSubtract(unittest.TestCase):
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(7, 5), 2)

if __name__ == '__main__':
    unittest.main()

