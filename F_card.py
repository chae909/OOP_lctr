import random

class Card:
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    suits_v = {"Spades": "\u2664", "Hearts": "\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
                # 직접 모양을 나타내는 유니코드 입력
    values = [None, None, "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "J", "Q", "K", "A"]

    """suit + value are ints"""
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __gt__(self, another):
        if self.value > another.value:
            return True
        if self.value == another.value:
            if self.suit > another.suit:
                return True
            else:
                return False
        return False

    def __str__(self):
        v = self.suits_v[self.suits[self.suit]] + " " + self.values[self.value]
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        random.shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        self.deck = Deck()
        self.p1 = Player(input("player1 name: "))
        self.p2 = Player(input("player2 name: "))

    def wins(self, winner):
        print(f"{winner} wins.")

    def draw(self, p1n, p1c, p2n, p2c):
        print(f'{p1n}: {p1c}, {p2n}: {p2c}')

    def play_game(self):
        cards = self.deck.cards
        while len(cards) >= 2:
            response = input("q to quit. Any key to play: ")
            if response == 'q':
                break
            p1c, p2c = self.deck.remove_card(), self.deck.remove_card()
            self.draw(self.p1.name, p1c, self.p2.name, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        win = self.winner(self.p1, self.p2)
        print(f"Game over. {win} wins")

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"


if __name__ == '__main__':
    game = Game()
    game.play_game()