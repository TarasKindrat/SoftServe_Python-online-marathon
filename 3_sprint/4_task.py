"""
Create function-generator divisor that should return all divisors of the positive number.
If there are no divisors left function should return None.
three = divisor(3)
next(three) => 1
next(three) => 3
next(three) => None

В 4 завдані має таким чином працювати?
three = divisor(3)
next(three) => 1
next(three) => 3
next(three) => None

four = divisor(4)
next(four) => 1
next(four) => 2
next(four) => 4
next(four) => None

"""

def divisor(x):
    for i in range(1, x+1):
        if x % i == 0:
            yield i
        if i == x:
            yield None
    yield None
    return

four = divisor(1)

next(four)
next(four)
#next(four)
print(dir(divisor(4)))
