import unittest
import numpy as np
from calculator_function import date1, date2

# define the unit tests
class my_unit_tests(unittest.TestCase):
    def test_date_difference(self):
        # test the difference between two dates
        expected_difference = (np.datetime64(date1) - np.datetime64(date2)).astype(int)

        actual_difference = (date1 - date2).astype(int)
        self.assertEqual(actual_difference, expected_difference)    

# run the tests 
if __name__ == "__main__":
    unittest.main()

