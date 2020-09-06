"""
The string defining the points of the quadrilateral has the next form: "#LB1:1#RB4:1#LT1:3#RT4:3"

     LB - Left Bottom point
     LT - Left Top point
     RT - Right Top point
     RB - Right Bottom point
    numbers after letters are the coordinates of a point.

Write a function figure_perimetr() that calculates the perimeter of a quadrilateral

The formula for calculating the distance between points:


For example:
Test 	Result

test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
print(figure_perimetr(test1))

10.0
"""


def figure_perimetr(test1):
    def distance(x1, y1, x2, y2):
        import math
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return dist

    return distance(test1[3], test1[5], test1[9], test1[11]) + \
           distance(test1[9], test1[11], test1[21], test1[23]) + \
           distance(test1[21], test1[23], test1[15], test1[17]) + \
           distance(test1[15], test1[17], test1[3], test1[5])

print(figure_perimetr("#LB1:1#RB4:1#LT1:3#RT4:3"))