"""
1. Create a class according to the following requirements:
It's name is Vehicle and it has the following attributes/methods:
Attributes/properties:
  name: str
  max_speed: int
  capacity: int
Methods:
    vroom() -> None
        Prints "Vroom" max_speed times
2. Create a child/subclass of Vehicle called Bus with the following methods:
Methods:
    fare(age: float) -> None
        Prints "The fare of the bus ride is {}."
            Price depends on age:
                0-17 years - Free
                18-60 years - $5
                61+ years - Free
"""

class Vehicle:

    def __init__(self):
        self.name = "car"
        self.max_speed = 60
        self.capacity = 5

    def vroom (self):
        for vroom in range(self.max_speed):
            print("Vroom")


class Bus(Vehicle):
    """Bus is a Vehicle that can drive
    humans around in it"""
    def fare(self, age: int) -> None:
        """Tells how much fare is for a particular age"""
        if 18 <= age <= 60:
            print("The fare of this bus ride is $5.00. 🚌")
        else:
            print("You ride free!~ 🚌")


a_vehicle = Vehicle()
a_vehicle.name = "La Ferrari"
a_vehicle.max_speed = 372
a_vehicle.capacity = 2
a_vehicle.vroom()

a_bus = Bus()
a_bus.name = "Tranlink Bus - 407"
a_bus.capacity = 35
a_bus.max_speed = 140
a_bus.vroom()
a_bus.fare(10)
print()
a_bus.fare(-1)
a_bus.fare(0)
a_bus.fare(17)
a_bus.fare(18)
a_bus.fare(60)
a_bus.fare(61)