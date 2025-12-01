import unittest
import convert_minutes

class testConvertMinutesFunction(unittest.TestCase):
    def test_that_convert_minutes_exist(self):
        convert_minutes.convert_minutes(5)

    def test_that_convert_minutes_function_is_divisible_by_sixty(self):
        actual = convert_minutes.convert_minutes(70)
        expected = True
        self.assertEqual(actual, expected)

    def test_that_convert_minutes_function_is_divisible_by_sixty(self):
        actual = convert_minutes.convert_minutes(40)
        expected = False
        self.assertEqual(actual, expected)
