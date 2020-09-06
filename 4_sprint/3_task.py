"""
Create a class Employee that will take a full name as argument, as well as a set of none,
 one or more keywords.

Each instance should have a name and a lastname attributes plus one more attribute for each of
the keywords, if any.

Examples:

john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
mary.lastname ➞ "Major"
richard.height ➞ 178
giancarlo.nationality ➞ "Italian"
john.name ➞ "John"
"""

class Employee:
    def __init__(self,*name_last_n, **propert):
        list_names = list(name_last_n)[0].split(" ")
        if len(list_names) == 2:
            self.name = list_names[0]
            self.lastname = list_names[1]
        else:
            self.name = name_last_n[0]
        for item, value in propert.items():
            setattr(self, item, value)

john = Employee('John Doe')
print(john.lastname)

mary = Employee('Mary Major', salary=120000)
print(mary.salary)
#print(mary.item)

