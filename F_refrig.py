class People:
    def __init__(self, name):
        self.name = name

    def open(self, bx):
        bx.open_door(self)

    def close(self, bx):
        bx.close_door(self)

class Refrigerator:
    def __init__(self, name):
        self.name = name

    def open_door(self, p):
        print(f"{p.name} opened the {self.name} refrigerator")

    def close_door(self, p):
        print(f"{p.name} closed the {self.name} refrigerator")


if __name__ == '__main__':
    r = People("John")
    ref = Refrigerator("LG")
    r.open(ref)
    r.close(ref)