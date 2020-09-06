import unittest


def divide(num_1, num_2):
    return float(num_1) / num_2


class DivideTest(unittest.TestCase):
    def test_divide_biggest_on_smallest_True(self):
        expected = 15
        actual = divide(30, 2)
        self.assertEqual(expected, actual)

    def test_divide_biggest_on_smallest_False(self):
        expected = 10
        actual = divide(30, 2)
        self.assertNotEqual(expected, actual)

    def test_divide_zero_on_number(self):
        expected = 0
        actual = divide(0, 2)
        self.assertEqual(expected, actual)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            x = divide(1, 0)



