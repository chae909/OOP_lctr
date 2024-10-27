from abc import ABC, abstractmethod
from datetime import date

class Goods(ABC):
    def __init__(self, regular_price):
        self._regular_price = regular_price

    @abstractmethod
    def price(self):
        ...

class Book(Goods):
    def __init__(self, title, pub_year, regular_price):
        super().__init__(regular_price)
        self._title = title
        self._pub_year = pub_year

    @property
    def price(self):
        elapsed_yr = date.today().year - self._pub_year
        if elapsed_yr > 5:
            rate = 0.2
        else:
            rate = 0.0
        return (int)((1-rate)*self._regular_price)

class ChildrenBook(Book):
    def __init__(self, title, pub_year, ages, regular_price):
        super().__init__(title, pub_year, regular_price)
        self.__ages = ages

    @property
    def price(self):
        elapsed_yr = date.today().year - self._pub_year
        if elapsed_yr > 2:
            rate = 0.4
        else:
            rate = 0.2
        return (int)((1-rate)*self._regular_price)

class Cartoon(Book):
    def __init__(self, title, pub_year, characters, regular_price):
        super().__init__(title, pub_year, regular_price)
        self.__characters = characters

    @property
    def price(self):
        return (int)(self._regular_price * 0.8)

if __name__ == '__main__':
    buying_books = [Book("제3인류", 2013, 20000),
                    Book("한국현대사", 2020, 30000),
                    ChildrenBook("어서와! 장풍아", 2021, '4~7', 10000),
                    Cartoon('배트맨', 2018, ["Robin", "Bat Girl", "Damian Wayne"], 20000)]

    total_price = 0

    for book in buying_books:
        print(book.price)
        total_price += book.price

    print(f"합계: {total_price}")