"""
Create class Triangle with method get_area() that calculate area of triangle. As input you will have list of 3 sides size

Examples:
triangle = Triangle([3, 3, 3])

Use classes TriangleNotValidArgumentException and TriangleNotExistException

Create class TriangleTest with parametrized unittest for class Triangle
test data:

valid_test_data = [
    ((3, 4, 5), 6.0),
    ((10, 10, 10), 43.30),
    ((6, 7, 8), 20.33),
    ((7, 7, 7), 21.21),
    ((50, 50, 75), 1240.19),
    ((37, 43, 22), 406.99),
    ((26, 25, 3), 36.0),
    ((30, 29, 5), 72.0),
    ((87, 55, 34), 396.0),
    ((120, 109, 13), 396.0),
    ((123, 122, 5), 300.0)
]
    not_valid_triangle = [
    (1, 2, 3),
    (1, 1, 2),
    (7, 7, 15),
    (100, 7, 90),
    (17, 18, 35),
    (127, 17, 33),
    (145, 166, 700),
    (1000, 2000, 1),
    (717, 17, 7),
    (0, 7, 7),
    (-7, 7, 7)
]
    not_valid_arguments = [
    ('3', 4, 5),
    ('a', 2, 3),
    (7, "str", 7),
    ('1', '1', '1'),
    'string',
    (7, 2),
    (7, 7, 7, 7),
    'str',
    10,
    ('a', 'str', 7)
]

"""
import math
import unittest


class TriangleNotValidArgumentException(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class TriangleNotExistException(Exception):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class Triangle:
    def __init__(self, sides_list):
        if hasattr(sides_list, '__iter__'):
            self.sides_list = list(sides_list)
        else:
            raise TriangleNotValidArgumentException("Not valid arguments")

        if len(self.sides_list) != 3:
            raise TriangleNotValidArgumentException("Not valid arguments")
        if len(self.sides_list) == 3:
            for i in self.sides_list:
                if not (isinstance(i, int)):
                    raise TriangleNotValidArgumentException("Not valid arguments")
                if i <= 0:
                    raise TriangleNotExistException("Can`t create triangle with this arguments")

        if not ((self.sides_list[0] + self.sides_list[1] > self.sides_list[2]) and
                (self.sides_list[0] + self.sides_list[2] > self.sides_list[1]) and
                (self.sides_list[1] + self.sides_list[2] > self.sides_list[0])):
            raise TriangleNotExistException("Can`t create triangle with this arguments")

    def get_area(self):
        p = (self.sides_list[0] + self.sides_list[1] + self.sides_list[2]) / 2
        s = math.sqrt(p * (p - self.sides_list[0]) * (p - self.sides_list[1]) * (p - self.sides_list[2]))
        return s



class TriangleTest(unittest.TestCase):
    def setUp(self):
        self.valid_test_data = [
        ((3, 4, 5), 6.0),
        ((10, 10, 10), 43.30),
        ((6, 7, 8), 20.33),
        ((7, 7, 7), 21.21),
        ((50, 50, 75), 1240.19),
        ((37, 43, 22), 406.99),
        ((26, 25, 3), 36.0),
        ((30, 29, 5), 72.0),
        ((87, 55, 34), 396.0),
        ((120, 109, 13), 396.0),
        ((123, 122, 5), 300.0)
        ]
        self.not_valid_triangle = [
        (1, 2, 3),
        (1, 1, 2),
        (7, 7, 15),
        (100, 7, 90),
        (17, 18, 35),
        (127, 17, 33),
        (145, 166, 700),
        (1000, 2000, 1),
        (717, 17, 7),
        (0, 7, 7),
        (-7, 7, 7)
        ]
        self.not_valid_arguments = [
        ('3', 4, 5),
        ('a', 2, 3),
        (7, "str", 7),
        ('1', '1', '1'),
        'string',
        (7, 2),
        (7, 7, 7, 7),
        'str',
        10,
        ('a', 'str', 7)
        ]

    def test_valid_triangle2(self):
        self.assertEqual(1,1)

    def test_valid_triangle(self):
        for p1, p2 in self.valid_test_data:
            with self.subTest():
                self.assertEqual(Triangle(p1).get_area(), p2)

    @unittest.expectedFailure
    def test_not_valid_triangle(self):
        for data in self.not_valid_triangle:
            with self.subTest():
                self.assertTrue(Triangle(data).get_area())

    @unittest.expectedFailure
    def test_not_valid_triangle(self):
        for data in self.not_valid_arguments:
            with self.subTest():
                self.assertTrue(Triangle(data).get_area())

    def tearDown(self):
        self.valid_test_data = None
        self.not_valid_arguments = None
        self.not_valid_triangle = None


# triangl = Triangle([3, 4, 5])
# print(triangl.get_area())

# triang2 = Triangle([127, 17, 33])
# print(triang2.get_area())
# triang3 = Triangle([7, 2])
# print(triang3.get_area())

# print(type(((3, 4, 5), 6.0)))
valid_test_data = [
    (3, 4, 5),
    (26, 25, 3),
    (30, 29, 5),
    (87, 55, 34),
    (120, 109, 13),
    (123, 122, 5)]
for data in valid_test_data:
    print(Triangle(data).get_area())

not_valid_triangle = [
    (1, 2, 3),
    (1, 1, 2),
    (7, 7, 15),
    (100, 7, 90),
    (17, 18, 35),
    (127, 17, 33),
    (145, 166, 700),
    (1000, 2000, 1),
    (717, 17, 7),
    (0, 7, 7),
    (-7, 7, 7)
]
for data in not_valid_triangle:
    try:
        Triangle(data)
    except TriangleNotExistException as e:
        print(e)

#
not_valid_arguments = [
    ('3', 4, 5),
    ('a', 2, 3),
    'string',
    (7, 2),
    (7, 7, 7, 7),
    10
]
for data in not_valid_arguments:
    try:
        Triangle(data)
    except TriangleNotValidArgumentException as e:
        print(e)

