class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius


if __name__ == "__main__":
    c1 = Circle(5)
    c2 = Circle(3)

    if c1 < c2:
        print(f"{c1} is less than {c2}")
    elif c1 == c2:
        print(f"{c1} is equal to {c2}")
    else:
        print(f"{c1} is greater to {c2}")