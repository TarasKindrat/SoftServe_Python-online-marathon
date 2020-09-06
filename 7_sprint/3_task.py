"""
Imagine you are creating an application that shows the data about all different types of vehicles present.
It takes the data from APIs of different vehicle organizations in XML format and then displays the information.
But suppose at some time you want to upgrade your application with a Machine Learning algorithms that work
beautifully on the data and fetch the important data only. But there is a problem, it takes data in JSON format only.
It will be a really poor approach to make changes in Machine Learning Algorithm so that it will take data in
XML format.

For solving the problem we defined above, you can use Adapter Method that helps by creating an Adapter object.
To use an adapter in your code:

    Client should make a request to the adapter by calling a method on it using the target interface.
    Using the Adaptee interface, the Adapter should translate that request on the adaptee.
    Result of the call is received the client and he/she is unaware of the presence of the Adapter’s presence.

Class diagram for the Adapter method:
"""


class MotorCycle:
    """Class for MotorCycle"""

    def __init__(self):
        self.name = "MotorCycle"

    def TwoWheeler(self):
        return "TwoWheeler"


class Truck:
    def __init__(self):
        self.name = "Truck"

    def EightWheeler(self):
        return "EightWheeler"


class Car:
    def __init__(self):
        self.name = "Car"

    def FourWheeler(self):
        return "FourWheeler"


class Adapter:
    """
    Adapts an object by replacing methods.
    Usage:
    motorCycle = MotorCycle()
    motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler)
    """

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        for item, value in adapted_methods.items():
            setattr(self, item, value)
            

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return self.obj.name

    def original_dict(self):
        """Print original object dict"""
        print(self.__dict__)


objects = []
motorCycle = MotorCycle()
objects.append(Adapter(motorCycle, wheels=motorCycle.TwoWheeler))
truck = Truck()
objects.append(Adapter(truck, wheels=truck.EightWheeler))
car = Car()
objects.append(Adapter(car, wheels=car.FourWheeler))
for obj in objects:
    print("A {0} is a {1} vehicle".format(obj.name, obj.wheels()))

"""	

A MotorCycle is a TwoWheeler vehicle
A Truck is a EightWheeler vehicle
A Car is a FourWheeler vehicle"""
