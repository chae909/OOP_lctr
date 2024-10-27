# 클래스 정의하기

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def area(self):
        return 0

    @abstractmethod
    def volume(self):
        return 0

    def __str__(self):
        return (f"도형 종류: {self._name}"
                f"면적: {self.area():.3f}, 체적: {self.volume():.3f} \n")

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def area(self):
        return self.width * self.height

    def volume(self):
        return 0

    def __str__(self):
        return (f"도형 종류: {self._name} (가로: {self.width:.1f}, 세로: {self.height:.1f}) \n"
                f"면적: {self.area():.3f}, 체적: {self.volume():.3f} \n")


class Box(Rectangle):
    def __init__(self, name, width, height, depth):
        super().__init__(name, width, height)
        self.__depth = depth

    @property
    def depth(self):
        return self.__depth

    def area(self):
        return 2*(self.width*self.height) + 2*(self.width*self.depth) + 2*(self.depth*self.height)

    def volume(self):
        return self.width * self.height * self.depth

    def __str__(self):
        return (f"도형 종류: {self._name} (가로: {self.width:.1f}, 세로: {self.height:.1f}, 높이: {self.depth:.1f}) \n"
                f"겉넓이: {self.area():.3f}, 체적: {self.volume():.3f} \n")

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    def area(self):
        return math.pi * self.radius * self.radius

    def volume(self):
        return 0

    def __str__(self):
        return (f"도형 종류: {self._name} (반지름: {self.radius:.1f}) \n"
                f"면적: {self.area():.3f}, 체적: {self.volume():.3f} \n")

class Cylinder(Circle):
    def __init__(self, name, radius, height):
        super().__init__(name, radius)
        self.__height = height

    @property
    def height(self):
        return self.__height

    def area(self):
        return (2 * math.pi * self.radius * self.radius) + (2 * math.pi * self.radius * self.height)

    def volume(self):
        return math.pi * self.radius * self.radius * self.height

    def __str__(self):
        return (f"도형 종류: {self._name} (반지름: {self.radius:.1f}, 높이: {self.height:.1f}) \n"
                f"겉면적 : {self.area():.3f}, 체적: {self.volume():.3f} \n")

class Sphere(Circle):
    def __init__(self, name, radius):
        super().__init__(name, radius)

    def area(self):
        return 4 * math.pi * self.radius * self.radius

    def volume(self):
        return 4/3 * math.pi * self.radius * self.radius

    def __str__(self):
        return (f"도형 종류: {self._name} (반지름: {self.radius:.1f}) \n"
                f"겉면적: {self.area():.3f}, 체적: {self.volume():.3f} \n")

rectangle = Rectangle("Rectangle", 10, 5)
print(rectangle)

box = Box("Box", 10, 5, 30)
print(box)

circle = Circle("Circle", 20)
print(circle)

cylinder = Cylinder("Cylinder", 20, 50)
print(cylinder)

sphere = Sphere("Sphere", 20)
print(sphere)