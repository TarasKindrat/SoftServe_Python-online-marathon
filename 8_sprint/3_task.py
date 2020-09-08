import unittest
import math


def quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError
    a = float(a)
    b = float(b)
    c = float(c)

    d = b ** 2 - 4 * a * c

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    if d == 0:
        x = - b / 2 * a
        return x
    if d < 0:
        return None


class QuadraticEquationTest(unittest.TestCase):

    def test_discriminant_more_zero(self):
        expected = (1.0, -1.5)
        actual = quadratic_equation(2, 1, -3)
        self.assertEqual(expected, actual)

    def test_discriminant_zero(self):
        expected = (-1)
        actual = quadratic_equation(1, 2, 1)
        self.assertEqual(expected, actual)

    def test_discriminant_less_zero(self):
        self.assertFalse(quadratic_equation(20, 3, 9))

    def test_discriminant_less_zero_2(self):
        self.assertIsNone(quadratic_equation(20, 3, 9))




print(quadratic_equation(2, 1, -1))
try:
    quadratic_equation(0, 0, 0)
except ValueError:
   print('error')


"""
print(quadratic_equation(2, 1, -1))

(0.5, -1.0)

	

(-4.0, 2.0)
"""
