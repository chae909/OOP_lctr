import math
class Point:
    def __init__(self, x:float=0.0, y:float=0.0):
        self._x = x
        self._y = y
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @x.setter
    def x(self, x:float):
        self._x = x
    @y.setter
    def y(self, y:float):
        self._y = y
    def move(self, x:float, y:float):
        self._x = x
        self._y = y

    def reset(self):
        self.move(0.0, 0.0)
    def cal_dist(self, other:"Point"):
        d = math.hypot(self._x-other.x, self._y-other.y)
        return d

point1 = Point(10.0, 10.0)
point2 = Point(20.0, 20.0)
print(f'점1과 점2 사이의 거리: {point1.cal_dist(point2):.2f}')

point1.move(15, 15)
point2.move(9, 9)
print(f'옮긴 점1과 점2 사이의 거리: {point1.cal_dist(point2):.2f}')

