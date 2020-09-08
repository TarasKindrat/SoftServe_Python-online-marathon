"""
Create class Worker with fields name and salary. If salary negative raise ValueError

Create a method get_tax_value() that calculate tax from salary .
Tax must be calculate like "progressive tax" with next step:

    less then 1000 - 0%
    1001 - 3000 - 10%
    3001 - 5000 - 15%
    5001 - 10000 - 21%
    10001 - 20000 - 30%
    20001 - 50000 - 40%
    more than 50000 - 47%

Please create WorkerTest class with unitest to the class Worker. Try to use setUp and tearDown methods.
Don`t use assertRaises in tests.
"""
import unittest


class Worker:
    def __init__(self, name, salary=0.0):
        self.name = name
        self.salary = float(salary)
        self.taxes = 0.0
        if self.salary < 0.0:
            raise ValueError

    def get_tax_value(self):

        if 1000 <= self.salary < 3000:
            self.taxes = (self.salary - 1000) * 0.1
            return self.taxes
        elif 3001 <= self.salary < 5000:
            self.taxes = (3001 - 1001) * 0.1 + (self.salary - 3001) * 0.15
        elif 5001 <= self.salary < 10000:
            self.taxes = (3001 - 1001) * 0.1 + (5001 - 3001) * 0.15 + (self.salary - 5001) * 0.21
        elif 10001 <= self.salary < 20000:
            self.taxes = (3001 - 1001) * 0.1 + (5001 - 3001) * 0.15 + (10001 - 5001) * 0.21 + \
                         (self.salary - 10001) * 0.3
        elif 20001 <= self.salary < 50000:
            self.taxes = (3001 - 1001) * 0.1 + (5001 - 3001) * 0.15 + (10001 - 5001) * 0.21 + \
                         (20001 - 10001) * 0.3 + (self.salary - 20001) * 0.4
        elif self.salary > 50000:
            self.taxes = (3001 - 1001) * 0.1 + (5001 - 3001) * 0.15 + (10001 - 5001) * 0.21 + \
                         (20001 - 10001) * 0.3 + (50000 - 20001) * 0.4 + (self.salary - 50000) * 0.47

        return float(round(self.taxes))


class WorkerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.worker1 = Worker("Jon", 300)
        self.worker2 = Worker("Jon", 2000)
        self.worker3 = Worker("Jon", 4000)
        self.worker4 = Worker("Jon", 8000)
        self.worker5 = Worker("Jon", 15000)
        self.worker6 = Worker("Jon", 40000)
        self.worker7 = Worker("Jon", 95000)

    def test_tax_salary_less_300(self):
        expected = 0
        actual = self.worker1.get_tax_value()
        self.assertEqual(expected, actual)

    def test_tax_salary_less_2000(self):
        expected = 100.0
        actual = self.worker2.get_tax_value()
        self.assertEqual(expected, actual)

    def test_tax_salary_less_5000(self):
        expected = 350.0
        actual = self.worker3.get_tax_value()
        self.assertEqual(expected, actual)

    def test_tax_salary_less_10000(self):
        expected = 1130.0
        actual = self.worker4.get_tax_value()
        self.assertEqual(expected, actual)

    def test_tax_salary_less_20000(self):
        expected = 3050.0
        actual = self.worker5.get_tax_value()
        self.assertEqual(expected, actual)

    def test_tax_salary_less_50000(self):
        expected = 12550.0
        actual = self.worker6.get_tax_value()
        self.assertEqual(expected, actual)

    def test_tax_salary_more_50000(self):
        expected = 37700.0
        actual = self.worker7.get_tax_value()
        self.assertEqual(expected, actual)

    @unittest.expectedFailure
    def test_ax_salary_less_0(self):
        expected = 0
        actual = Worker("Jon", -50).get_tax_value()
        self.assertEqual(expected, actual)

    def tearDown(self) -> None:
        self.worker1 = None
        self.worker2 = None
        self.worker3 = None
        self.worker4 = None
        self.worker5 = None
        self.worker6 = None
        self.worker7 = None


"""
worker = Worker("Vasia")
print(worker.get_tax_value())
0.0"""
worker = Worker("Vasia")
print(worker.get_tax_value())

worker = Worker("Natasha", 1001)
print(worker.get_tax_value())

#0.1

worker = Worker("Vika", 100000)
print(worker.get_tax_value())

#40050.0