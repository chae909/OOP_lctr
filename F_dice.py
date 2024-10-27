from typing import Type, Any, Set, Iterable
from abc import ABC, abstractmethod
import random

class Die(ABC):
    def __init__(self)->None:
        self.face:int
        self.roll()

    def __repr__(self) -> str:
        return f"{self.face}"

    @abstractmethod
    def roll(self)->None:
        ...

class D4(Die):
    def roll(self)->None:
        self.face = random.choice((1,2,3,4))
        # 상속받은 face를 구체화시킴
        # random choice = 묶음 자료형이 들어감(이중에서 하나 선택)

class D6(Die):
    def roll(self)->None:
        self.face = random.randint(1,6)

class Dice(ABC):              # Type[Die]-> 모든 주사위(D4, D6) 허용
    def __init__(self, n:int, die_class: Type[Die])->None:
        self.dice = [die_class() for _ in range(n)]
                                # for문에서 range나 묶음자료형을 쓸 때
                                # _는 값이 저장되지 않음 -> 메모리 아낄 수 있음

    @abstractmethod
    def roll(self)->None:
        ...

    @property
    def total(self):
        return sum(d.face for d in self.dice)

class SimpleDice(Dice):
    def roll(self)->None:
        for d in self.dice:
            d.roll()

    @property
    def faces(self)->list:
        face_list=[]
        for d in self.dice:
            face_list.append(d.face)
        return face_list

if __name__ == "__main__":
    simpledice = SimpleDice(6, D6)
    simpledice.roll()
    print(simpledice.faces)

    print(f"합: {simpledice.total}")