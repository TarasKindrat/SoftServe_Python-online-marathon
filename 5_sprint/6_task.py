"""
Write  the function solve_quadric_equation(a, b, c) the three input parameters of which are numbers.
 The function should return
the solution of quadratic equation ax2+bx+c=0, where coefficients a, b, c are input parameters of
 the function solve_quadric_equation:

     in case of correct data the function should displayed the corresponding message –
     "The solution are x1=… and x2=…"

    in the case of division by zero the function should displayed the corresponding message –
    "Zero Division Error"

    in the case of incorrect data the function should displayed the message –
    "Could not convert string to float"

Note: in the function you must use the "try except" construct.


 Function example:

solve_quadric_equation(1, 5, 6)            #output:   " The solution are x1=(-2-0j) and x2=(-3+0j)"

solve_quadric_equation(0, 8, 1)            #output:   "Zero Division Error"

solve_quadric_equation(1,”abc”, 5)       #output:   "Could not convert string to float"

ax2 +bx +c = 0
"""


def solve_quadric_equation(a, b, c):
    import logging
    import cmath
    
    logging.basicConfig(level=logging.DEBUG)

    try:
        a = float(a)
        b = float(b)
        c = float(c)
        d = b ** 2 - 4 * a * c

        x1 = (-b - cmath.sqrt(d)) / (2 * a)
        x2 = (-b + cmath.sqrt(d)) / (2 * a)
        print(f"The solution are x1={x1} and x2={x2}")

    except ValueError:
        print("Could not convert string to float")
    except ZeroDivisionError:
        print("Zero Division Error")

solve_quadric_equation(1, 5, 6)
solve_quadric_equation(0, 8, 1)
solve_quadric_equation(1,"abc", 5)