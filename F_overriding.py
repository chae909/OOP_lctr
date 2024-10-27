class Employee:
    def __init__(self, name:str, base_pay:int)->None:
        self.name = name
        self.base_pay = base_pay

    @property
    def pay(self)->int:
        return self.base_pay

class SalesEmployee(Employee):
    def __init__(self, name, base_pay, rate:float)->None:
        super().__init__(name, base_pay)
        self.incentive_rate = rate

    @property
    def pay(self)->int:
        return (int)((1+self.incentive_rate)*super().pay)

if __name__ == '__main__':
    john = SalesEmployee('John', 10000000, 0.1)
    print(f"{john.name}'s pay: {john.pay}")