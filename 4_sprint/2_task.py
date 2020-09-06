"""
Create a Pizza class with the attributes order_number and ingredients (which is given as a list).
Only the ingredients will be given as input.

You should also make it so that its possible to choose a ready made pizza flavour rather than typing
out the ingredients manually! As well as creating this Pizza class, hard-code the following pizza flavours.

Name           Ingradients
hawaiian       ham, pineapple
meat_festival  beef, meatball, bacon
garden_feast   spinach, olives, mushroom


Examples:
p1 = Pizza(["bacon", "parmesan", "ham"])    # order 1
p2 = Pizza.garden_feast()                  # order 2
p1.ingredients ➞ ["bacon", "parmesan", "ham"]
p2.ingredients ➞ ["spinach", "olives", "mushroom"]
p1.order_number ➞ 1
p2.order_number ➞ 2
"""


class Pizza:
    order_number = 1

    def __init__(self, list_ingredients):
        self.ingredients = list_ingredients
        self.order_number = self.__class__.order_number
        self.__class__.order_number += 1
        # @classmethod
        # def number(cls):
        #    cls.order_number+=1

    @classmethod
    def meat_festival(cls):
        # cls.order_number += 1
        return cls(['beef', 'meatball', 'bacon'])

    @classmethod
    def hawaiian(cls):
        # cls.order_number += 1
        return cls(['ham', 'pineapple'])

    @classmethod
    def garden_feast(cls):
        # cls.order_number += 1
        return cls(["spinach", "olives", "mushrooms"])


p1 = Pizza(["bacon", "parmesan", "ham"])  # order 1
p2 = Pizza.garden_feast()
print(p1.__class__.order_number)
