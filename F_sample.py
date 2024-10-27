class SampleClass:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'value: {self.value}'

    def __add__(self, other):
        result = self.value + other.value
        return SampleClass(result)

if __name__ == '__main__':
    obj1 = SampleClass(1)
    obj2 = SampleClass(2)

    print(obj1 + obj2)