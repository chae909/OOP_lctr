class A:
    def __init__(self):
        print('init A')

class B:
    def __init__(self):
        print('init B')

class C(A):
    def __init__(self):
        print('init C')
        super().__init__()

class D(B, C):
    def __init__(self):
        print('init D')
        B.__init__(self)
        C.__init__(self)

if __name__ == '__main__':
    D()