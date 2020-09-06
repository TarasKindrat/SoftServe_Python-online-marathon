import unittest

"""
в данному випадку треба використовувати декоратор @unittest.expectedFailures"""


class Worker:
    def __init__(self, name, salary):
        self.name = name
        if salary < 0:
            raise ValueError
        self.salary = float(salary)


def get_tax_values(salary):
    taxes = 0
    if 1001 <= salary < 3000:
        taxes = salary * 0.1
    elif 3001 <= salary < 5000:
        taxes = salary * 0.15
    elif 5001 <= salary < 10000:
        taxes = salary * 0.21
    elif 10001 <= salary < 20000:
        taxes = salary * 0.3
    elif 20001 <= salary < 50000:
        taxes = salary * 0.4
    elif salary > 50000:
        taxes = salary * 0.47
    return taxes


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
        actual = get_tax_values(self.worker1.salary)
        self.assertEqual(expected, actual)

    def test_tax_salary_less_2000(self):
        expected = 200.0
        actual = get_tax_values(self.worker2.salary)
        self.assertEqual(expected, actual)

    def test_tax_salary_less_5000(self):
        expected = 600.0
        actual = get_tax_values(self.worker3.salary)
        self.assertEqual(expected, actual)

    def test_tax_salary_less_10000(self):
        expected = 1680.0
        actual = get_tax_values(self.worker4.salary)
        self.assertEqual(expected, actual)

    def test_tax_salary_less_20000(self):
        expected = 4500.0
        actual = get_tax_values(self.worker5.salary)
        self.assertEqual(expected, actual)

    def test_tax_salary_less_50000(self):
        expected = 16000.0
        actual = get_tax_values(self.worker6.salary)
        self.assertEqual(expected, actual)

    def test_tax_salary_more_50000(self):
        expected = 44650.0
        actual = get_tax_values(self.worker7.salary)
        self.assertEqual(expected, actual)

    @unittest.expectedFailure
    def test_ax_salary_less_0(self):
        expected = 0
        actual = get_tax_values(Worker("Jon", -50))
        self.assertEqual(expected, actual)

    def tearDown(self) -> None:
        self.worker1 = None
        self.worker2 = None
        self.worker3 = None
        self.worker4 = None
        self.worker5 = None
        self.worker6 = None
        self.worker7 = None