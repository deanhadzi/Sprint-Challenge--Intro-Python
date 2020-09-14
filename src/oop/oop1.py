# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle():
    """Base Class. The one to rule them all."""
    pass

class GroundVehicle(Vehicle):
    """Left Branch, middle level class."""
    pass

class Car(GroundVehicle):
    """Left Branch, bottom level class."""
    pass

class Motorcycle(GroundVehicle):
    """Left Branch, bottom level class."""
    pass

class FlightVehicle(Vehicle):
    """Right Branch, middle level class."""
    pass

class Starship(FlightVehicle):
    """Right Branch, bottom level class."""
    pass

class Airplane(FlightVehicle):
    """Right Branch, bottom level class."""
    pass