from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, border_color):
        self.border_color = border_color

    @property
    @abstractmethod
    def area(self):
        ...
    def draw(self):
        ...

class Square(Shape):
    def __init__(self, side, border_color='black'):
        super().__init__(border_color)
        self.side = side

    @property
    def area(self):
        return math.pow(self.side, 2)
    def draw(self):
        print(f"Drawing a {self.border_color} square with sides of length {self.side}.")

class Circle(Shape):
    def __init__(self, radius, border_color='black'):
        super().__init__(border_color)
        self.radius = radius

    @property
    def area(self):
        return math.pi * math.pow(self.radius, 2)
    def draw(self):
        print(f"Drawing a {self.border_color} circle with radius {self.radius}.")

if __name__ == '__main__':
    # shape = Shape()          # error‐추상클래스의인스턴스생성불가

    shapes = [Square(3), Circle(2), Square(5)]
    for shape in shapes:
        print(f'면적 {shape.area}')
        shape.draw()