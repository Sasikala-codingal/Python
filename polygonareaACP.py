from abc import ABC, abstractmethod
import math


class Polygon(ABC):
    @abstractmethod
    def get_area(self):
        """Calculate the area of the polygon"""
        pass

    @abstractmethod
    def get_perimeter(self):
        """Calculate the perimeter of the polygon"""
        pass


class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"


rect = Rectangle(5, 10)
sq = Square(4)

print(f"{rect} Area: {rect.get_area()}")   
print(f"{sq} Area: {sq.get_area()}")       
print(f"{sq} Perimeter: {sq.get_perimeter()}") 
