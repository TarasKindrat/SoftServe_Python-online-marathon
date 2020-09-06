"""
Imagine we have a washing machine which can wash the clothes, rinse the clothes and spin the clothes
but all the tasks separately. We need a system that can automate the whole task without the disturbance
or interference of us.

To solve the above-described problem, we would like to hire the Facade Method. It will help us to hide or
 abstract the complexities of the subsystems as follows.

Note: the methods wash(), rinse() and spin() provide the output of the appropriate operation.
"""

class Washing:
    def wash(self):
        return "Washing..."


class Rinsing:
    def rinse(self):
        return "Rinsing..."


class Spinning:
    def spin(self):
        return "Spinning..."

class  WashingMachine:
   def __init__(self):
       print(Washing().wash())
       print(Rinsing().rinse())
       print(Spinning().spin())

   def startWashing(self):
       print(Washing().wash())
       print(Rinsing().rinse())
       print(Spinning().spin())


washingMachine = WashingMachine()
#wash = WashingMachine()

#wash.startWashing()