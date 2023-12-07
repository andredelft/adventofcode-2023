from functools import total_ordering
from collections import Counter


HIGH_CARD_ORDER = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


@total_ordering
class Hand(object):
    def __init__(self, cards: str):
        self.cards_list = list(cards)
        self.cards = Counter(cards)
        self.pairs = tuple(sorted(self.cards.values(), reverse=True))
        self.card_order = tuple(map(lambda c: HIGH_CARD_ORDER[c], self.cards_list))

    def __eq__(self, other):
        return self.pairs == other.pairs and self.card_order == other.card_order

    def __lt__(self, other):
        if self.pairs == other.pairs:
            return self.card_order < other.card_order

        return self.pairs < other.pairs

    def __str__(self):
        return "".join(self.cards_list)

    def __repr__(self):
        return f"<Hand: {self}>"
