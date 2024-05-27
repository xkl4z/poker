import random


class Deck:

    CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    SUITS = ["s", "h", "c", "d"]
    SUITS_SYMBOLS = {"s": "\u2660", "h": "\u2665", "c": "\u2663", "d": "\u2666"}

    def __init__(self):
        self.remaining = []

    def convert_to_symbol(self, suit):
        return self.SUITS_SYMBOLS[suit]

    def new_round(self):
        self.remaining = []
        for suit in self.SUITS:
            self.remaining += [card + self.convert_to_symbol(suit) for card in self.CARDS]

        self.shuffle()

    def shuffle(self):
        self.remaining = random.sample(self.remaining, len(self.remaining))

    def deal(self):
        return self.remaining.pop()


if __name__ == "__main__":

    d = Deck()

    d.new_round()
    d.shuffle()

    while len(d.remaining) > 0:
        print(len(d.remaining))
        d.deal()
