class A:
    def __init__(self, x):
        self.__x = x
    def m(self):
        print(self.__x - 1)

class B(A):
    def __init__(self, y):
        super().__init__(y - 1)

        self.__y = y
    def m(self):
        print(self.__y+1)

if __name__ == '__main__':
    A(3).m()
    B(3).m()
