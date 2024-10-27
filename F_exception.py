from decimal import Decimal

class InvalidWithdrawal(ValueError):
    def __init__(self, balance:Decimal, amount:Decimal)->None:
        super().__init__(f"Account doesn't have ${amount}")
        self.amount = amount
        self.balance = balance

    def overage(self)->Decimal:
        return self.amount - self.balance

if __name__ == '__main__':
    balance = Decimal('20.00')
    withdrawal = Decimal('50.00')

    try:
        if balance < withdrawal:
            raise InvalidWithdrawal(balance, withdrawal)
    except InvalidWithdrawal as ex:
        print(f"I'm sorry, but yout withdrawal is more than your balance by ${ex.overage()}")

'''
'''

while True:
    try:
        num = float(input("Enter a number: "))
        break
    except ValueError:
        print('***Error: Enter a numeric value.***')

num = num*2
print(num)

'''
'''

import csv

while True:
    try:
        with open(input('Enter a file: ')) as in_file:
            data_reader = csv.reader(in_file)
            for row in data_reader:
                print(row)
        break
    except IOError:
        print("***Error: 올바른 파일이름을 입력하세요.***")
