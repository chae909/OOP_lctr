# class A 정의 - 기본값이 0인 변수 x 설정
class A:
    def __init__(self, x=0):
        self.__x = x

# 은폐속성 x에 대한 getter
    #def get_x(self):
    #    return self.__x

    @property
    def x(self):
        return self.__x

# 은폐속성 x에 대한 setter
    #def set_x(self, x):
    #    self.__x = x

    @x.setter
    def x(self, x):
        self.__x = x

# a와 b에 class A를 이용한 x값 두개 만들어 저장하기
if __name__ == '__main__':
    a = A()
    b = A(10)

# a와 b출력
    print(f'객체 a의 속성값 x: {a.get_x():.1f}')

# setter를 이용하여 a를 b의 두배가 되도록 값 설정 후 소수점아래 1자리까지 출력
    a.set_x(2*b.get_x())

    print(f'객체 a의 속성값 x: {a.get_x():.1f}')
    print(f'객체 b의 속성값 x: {b.get_x():.1f}')