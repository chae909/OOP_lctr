import math

class Shape:
    def __init__(self, border_col='black'):
        self._border_col= border_col
    def display(self):
        print(f'This is a shape with {self._border_col} color')
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, border='black', side=1):
        super().__init__(border)
        self.__side = side
    def display(self):
        super().display()
        print(f'This is a square with size {self.__side}')
    def area(self):
        return self.__side*self.__side

class Circle(Shape):
    def __init__(self, border='black', radius=1):
        super().__init__(border)
        self.__radius = radius
    def display(self):
        super().display()
        print(f'This is a circle with radius {self.__radius}')
    def area(self):
        return math.pi*self.__radius**2

if __name__ == '__main__':
    shape_inst = Shape()
    print(f'면적: {shape_inst.area():.3f}')
    shape_inst.display()

    rect_inst = Square(side=2)
    print(f'면적: {rect_inst.area():.3f}')
    rect_inst.display()

    circle_inst = Circle(radius=3)
    print(f'면적: {circle_inst.area():.3f}')
    circle_inst.display()