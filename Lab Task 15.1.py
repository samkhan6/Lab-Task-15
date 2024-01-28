#Q1: Abstract Base Classes and Multiple Inheritance
from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Child classes inheriting from Shape with specific functionalities
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# Example usage
circle = Circle(radius=5)
print(f"Circle Area: {circle.area()}")

square = Square(side_length=4)
print(f"Square Area: {square.area()}")
