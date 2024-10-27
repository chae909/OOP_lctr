class Base:
    def __init__(self, a):
        self._a = a

#    def __str__(self):
#        return f'속성 a: {self.a}'

    def welcome(self):
        print(f'Welcome {self._a}!')

class MyClass1(Base):
    def __init__(self, a, b):
        super().__init__(a)
        self.__b = b

    @property
    def b(self):
        return self.__b

#    def __str__(self):
#        return f'속성 a: {self.a}, 속성 b: {self.b}'

    def hello(self):
        print(f'Hello {self._a} and {self.__b}!')

class MyClass2(Base):
    def __init__(self, a, c):
        Base.__init__(self, a)
        self.__c = c

    @property
    def c(self):
        return self.__c

#    def __str__(self):
#        return super().__str__() + f', 속성 c: {self.c}'

    def hi(self):
        print(f'Hi {self._a} and {self.__c}!')

if __name__ == '__main__':
    obj1 = MyClass1('p1', 'p2')
    obj2 = MyClass2('k1', 'k2')

    print(obj1)
    obj1.welcome()
    obj1.hello()

    print(obj2)
    obj2.welcome()
    obj2.hi()

