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

HIGH_CARD_ORDER_WITH_JOKERS = {
    **HIGH_CARD_ORDER,
    "J": 1,
}


@total_ordering
class Hand(object):
    def __init__(self, cards: str, with_jokers=False):
        self.cards_list = list(cards)
        self.cards = Counter(cards)

        if with_jokers:
            try:
                num_jokers = self.cards.pop("J")
            except KeyError:
                pass
            else:
                if num_jokers == 5:
                    # Reset hand, since there is no other card to turn the joker into
                    self.cards["J"] = 5
                elif num_jokers > 0:
                    most_common_card = self.cards.most_common(1)[0][0]
                    self.cards[most_common_card] += num_jokers

        high_card_order = (
            HIGH_CARD_ORDER_WITH_JOKERS if with_jokers else HIGH_CARD_ORDER
        )

        self.pairs = tuple(sorted(self.cards.values(), reverse=True))
        self.card_order = tuple(high_card_order[card] for card in self.cards_list)

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
