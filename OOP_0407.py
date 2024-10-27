import turtle


# 1-1 point 클래스 (매개변수 기본값 0)
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def move(self, new_x, new_y):
        self.__x = new_x
        self.__y = new_y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __str__(self):
        return f"({self.x}, {self.y})"

# 1-2 rectangle 클래스 (매개변수 기본값 원점)
class Rectangle:
    def __init__(self, color, base_point=Point(), width=0, height=0, ):
        self.__base_point = base_point
        self.__width = width
        self.__height = height
        self.__color = color

    @property
    def base_point(self):
        return self.__base_point

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def color(self):
        return self.__color

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"기준점(좌측 하단) : {self.base_point} 가로 : {self.width} 세로 : {self.height} \
    면적 : {self.area} 둘레 : {self.perimeter}"

    def draw(self):
        turtle.penup()
        turtle.goto(self.base_point.x, self.base_point.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)
        turtle.end_fill()


# 1-a 테스트 코드
if __name__ == "__main__":
    base_point = Point(-50, 100)
    rectangle = Rectangle("blue", base_point, 50, 25)
    print(rectangle)



# 2 사각형들을 저장할 리스트
rectangles = []

# 주어진 좌표와 사각형 속성에 맞게 사각형 객체 생성
rectangle_data = [(-200, -200), 400, 200, 'green'], \
    [(-100, 0), 200, 100, 'red'], \
    [(-50, 100), 100, 50, 'green'], \
    [(-25, 150), 50, 25, 'red'], \
    [(-12, 175), 25, 12, 'green']


for data in rectangle_data:
    color = data[3]
    base_point = Point(data[0][0], data[0][1])
    width = data[1]
    height = data[2]
    rectangle = Rectangle(color, base_point, width, height)
    rectangles.append(rectangle)



# 3 turtle을 이용하여 사각형 그리기
turtle.speed(0)  # 최대 속도로 설정
for rectangle in rectangles:
    rectangle.draw()

turtle.done()