# class Die 정의 - 은폐속성 face(random 1~6)
# 메소드 roll(random 1~6)
import random

import self as self


class Die:
    def __init__(self):
        self.__face = random.randrange(1, 7)
    def roll(self):
        self.__face = random.randrange(1, 7)

# property로 은폐속성 face getter
    @property
    def face(self):
        return self.__face

# class Dice_Game - 속성 dice(2개 꺼내기_class Die 이용)
class Dice_Game:
    def __init__(self):
        self.dice = [Die() for n in range(2)]

# 메소드 play(2개의 주사위를 class Die에서 roll을 이용해 굴리기)
    def play(self):
        for dice in self.dice:
            dice.roll()

# 메소드 win(2개 꺼낸 속성dice의 face만큼 sum하기)
    def win(self):
        sum=0
        for dice in self.dice:
            sum+=dice.face
            print(dice.face, end=' ')
        if sum>6:
            print("player wins")
        else:
            print("computer wins")


# 게임 테스트
game = Dice_Game()
game.play()
game.win()