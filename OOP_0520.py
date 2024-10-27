import math

# class vector 정의하기
class Vector:
    def __init__(self, *args):
        self.v = tuple(float(arg) for arg in args)
    # 매개변수는 가변인수를 처리하도록 정의
    # 임의의 차원에 대한 인수를 모두 처리 가능해야 함

    def __add__(self, other):
        if len(self.v) != len(other.v):
            return "두 벡터의 크기가 달라 + 연산이 불가능합니다."
        result = [self.v[i] + other.v[i] for i in range(len(self.v))]
        return Vector(*result)

    def __sub__(self, other):
        if len(self.v) != len(other.v):
            return "두 벡터의 크기가 달라 - 연산이 불가능합니다."
        result = [self.v[i] - other.v[i] for i in range(len(self.v))]
        return Vector(*result)

    def __mul__(self, other):
        if len(self.v) != len(other.v):
            return "두 벡터의 크기가 달라 * 연산이 불가능합니다."
        result = sum(self.v[i] * other.v[i] for i in range(len(self.v)))
        return result

    def distance(self, other):
        if len(self.v) != len(other.v):
            return "두 벡터의 크기가 달라 거리 연산이 불가능합니다."
        result = math.sqrt(sum((self.v[i] - other.v[i]) ** 2 for i in range(len(self.v))))
        return result

    def norm(self):
        result = math.sqrt(sum(a ** 2 for a in self.v))
        return result

    def __str__(self):
        return "(" + ", ".join(str(value) for value in self.v) + ")"


# 실행 예
u1 = Vector(1, 2, 3, 4)
u2 = Vector(-1, 0, 1, 0)
u3 = Vector(1, 0, 1)
u4 = Vector(-1, 0, 1)


print("u1과 u2의 거리:", u1.distance(u2))
print("u3와 u4의 거리:", u3.distance(u4))
print("u1의 길이:", u1.norm())
print("u2의 길이:", u2.norm())
print("u3의 길이:", u3.norm())
print("u4의 길이:", u4.norm())
print("u1 + u2:", u1 + u2)
print("u3 - u4:", u3 - u4)
print("u1 * u2:", u1 * u2)
print("u1 + u3:", u1 + u3)
print("u1 * u3:", u1 * u3)