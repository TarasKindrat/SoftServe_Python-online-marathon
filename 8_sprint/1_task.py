"""
Write the programm that calculate total price with discount by the products.

Use class Product(name, price, count) and class Cart. In class Cart you can add the products.

Discount depends on count product:


count 	discount
2 	0%
5 	5%
7 	10%
10 	20%
20 	30%
more than 20 	50%

Write unittest with class CartTest and test all methods with logic
"""

import unittest


class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:
    def __init__(self):
        self.products_list = []

    def add_product(self, product):
        self.products_list.append(product)

    def discount_calculating(self) -> float:
        total_price = 0
        for item in self.products_list:
            if item.count < 5:
                total_price = total_price + item.price
            elif 5 <= item.count < 7:
                total_price = total_price + item.price * (1 - 0.05)
            elif 7 <= item.count < 10:
                total_price = total_price + item.price * (1 - 0.1)
            elif 10 <= item.count < 20:
                total_price = total_price + item.price * (1 - 0.2)
            elif 20 <= item.count:
                total_price = total_price + item.price * (1 - 0.5)
        return total_price


class CartTest(unittest.TestCase):
    def setUp(self) -> None:
        self.ob1 = Product("apple", 7, 7)
        self.ob2 = Product("whatermello", 19, 5)
        self.car = Cart()
        self.car.add_product(self.ob1)
        self.car.add_product(self.ob2)

    def test_check_total_price_correct(self):
        expected = 24.35
        actual = self.car.discount_calculating()
        self.assertEqual(expected, actual)

    def test_check_total_price_in_correct(self):
        expected = 15
        actual = self.car.discount_calculating()
        self.assertNotEqual(expected, actual)

    def tearDown(self) -> None:
        self.ob1 = None
        self.ob2 = None
        self.car = None
# print(count_tests > 0)
# print(failures)
# print(errors)
# print(assertEqual)
