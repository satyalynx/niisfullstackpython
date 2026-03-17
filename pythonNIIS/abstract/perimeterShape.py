from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side


r = Rectangle(10, 5)
print("Rectangle Perimeter:", r.perimeter())

s = Square(6)
print("Square Perimeter:", s.perimeter())