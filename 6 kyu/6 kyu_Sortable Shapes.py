from math import pi
class Shape:
    def __init__(self, area):
        self.area=area
    def __lt__(self, other):
         return self.area < other.area
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(base*height/2)
class Square(Shape):
    def __init__(self, side):
        super().__init__(side*side)
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius**2*pi)
class Rectangle(Shape):
    def __init__(self, base, height):
        super().__init__(base*height)
class CustomShape(Shape):
    def __init__(self, area):
        super().__init__(area)