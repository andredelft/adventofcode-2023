from .hand import Hand


def parse_input(input_string: str):
    for line in input_string.split("\n"):
        cards, bid = line.split(" ")
        yield Hand(cards), int(bid)


def solve_a(input_string: str):
    hands = parse_input(input_string)

    sorted_hands = sorted(hands, key=lambda hand: hand[0])

    return sum(rank * bid for (rank, (_, bid)) in enumerate(sorted_hands, 1))


def solve_b(input_string: str):
    parse_input(input_string)
