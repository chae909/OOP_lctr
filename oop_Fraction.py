import math

class Fraction:
    def __init__(self, num:int=1, denom:int=1):
        if denom == 0:
            raise ValueError("denominator cannot be zero")
        self.numerator, self.denominator = Fraction.reduce(num, denom)

    @classmethod
    def reduce(cls, num:int, denom:int):
        g = math.gcd(num, denom)
        return (num//g, denom//g)

    def __add__(self, other:"Fraction"):
        n = self.numerator*other.denominator + other.numerator*self.denominator
        d = self.denominator*other.denominator
        return Fraction(n,d)

    def __mul__(self, other:"Fraction"):
        n = self.numerator*other.numerator
        d = self.denominator*other.denominator
        return Fraction(n,d)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

if __name__ == '__main__':
    fr1 = Fraction(2, 3)
    fr2 = Fraction(4, 5)

    fr3 = fr1+fr2
    print(f'{fr1}+{fr2}={fr3}')

    fr4 = fr1*fr2
    print(f'{fr1}*{fr2}={fr4}')

