import math
import random


class Circle:
    circle_list:list["Circle"] = []
    def __init__(self, radius: float=1.0):
        self.radius = radius
        Circle.circle_list.append(self)  # 생성 객체를 클래스 변수에 저장

    @property
    def area(self):
        return math.pi * math.sqr(self.radius, 2)

    def __str__(self):
        return f"원 반지름: {self.radius:.3f}"


if __name__ == '__main__':
    circles = []
    for n in range(3):
        r = random.randint(1, 10)
        Circle(r)

    for circle in Circle.circle_list:
        print(circle)