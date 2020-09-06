class Person:
    def __init__(self, id):
        self.id = id
sam = Person(100)
sam.__dict__['age'] = 49
print(sam.age + len(sam.__dict__))
print(sam.__dict__)


class A:
    def __init__(self):
        self.d= 3
        print('Initializing: class A')

    def sub_method(self, b):
        print('Printing from class A:', b)


class B(A):
    def __init__(self):
        print('Initializing: class B')
        A.__init__(self)

    def sub_method(self, b):
        print('Printing from class B:', b)
        super().sub_method(b + 1)


class C(B):
    def __init__(self):
        print('Initializing: class C')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class C:', b)
        super().sub_method(b + 1)


if __name__ == '__main__':
    c = C()
    c.sub_method(1)
    b = B()
    print(b.d)
isinstance(A, B)