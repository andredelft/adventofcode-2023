import re

from lib.field import iter_around
from lib.array import product


def parse_input(input_string: str):
    return input_string.split("\n")


def solve_a(input_string: str):
    field = parse_input(input_string)

    part_number_sum = 0
    for y, line in enumerate(field):
        for match in re.finditer(r"\d+", line):
            if any(
                re.match(r"[^\d\.]", field[j][i])
                for (j, i) in iter_around(field, y, match.span())
            ):
                part_number_sum += int(match.group())

    return part_number_sum


def solve_b(input_string: str):
    field = parse_input(input_string)

    gears = {}
    for y, line in enumerate(field):
        for match in re.finditer(r"\d+", line):
            number = int(match.group())
            for j, i in iter_around(field, y, match.span()):
                if field[j][i] == "*":
                    gears[(j, i)] = gears.get((j, i), []) + [number]

    return sum(product(nums) for nums in gears.values() if len(nums) == 2)
