from prac_09.car import Car
from random import randint

class UnreliableCar(Car):
    """A specialized version of a car that has a chance of not driving when driven."""

    def __init__(self, name="", fuel=0, reliability=0):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with reliability percentage."""
        return f"{super().__str__()}, {self.reliability}% reliability"

    def drive(self, distance):
        """Drive like parent Car but has a chance of not driving based on reliability"""
        if randint(0,100) <= self.reliability:
            super().drive(distance)
