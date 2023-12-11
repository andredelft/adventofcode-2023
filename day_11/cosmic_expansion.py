from itertools import combinations

from lib.field import get_dimensions, iterate_field, print_field


def cosmic_expansion(cosmos):
    expanded_cosmos = []
    _, width = get_dimensions(cosmos)

    for line in cosmos:
        expanded_cosmos.append([*line])
        if all(char == "." for char in line):
            expanded_cosmos.append([*line])

    for i in reversed(range(width)):
        if all(line[i] == "." for line in cosmos):
            for j in range(len(expanded_cosmos)):
                expanded_cosmos[j].insert(i, ".")

    return expanded_cosmos


def parse_input(input_string: str):
    return [list(line) for line in input_string.split("\n")]


def solve_a(input_string: str):
    cosmos = parse_input(input_string)
    expanded_cosmos = cosmic_expansion(cosmos)
    print_field(expanded_cosmos)

    galaxies = [
        (j, i) for value, j, i in iterate_field(expanded_cosmos) if value == "#"
    ]

    distance_sum = 0
    for g_1, g_2 in combinations(galaxies, 2):
        distance_sum += abs(g_1[0] - g_2[0]) + abs(g_1[1] - g_2[1])

    return distance_sum


def solve_b(input_string: str, expansion_coefficient=1_000_000):
    cosmos = parse_input(input_string)

    empty_rows = set(
        j for j, row in enumerate(cosmos) if all(char == "." for char in row)
    )
    empty_cols = set(
        i for i in range(len(cosmos[0])) if all(row[i] == "." for row in cosmos)
    )

    galaxies = [(j, i) for value, j, i in iterate_field(cosmos) if value == "#"]

    distance_sum = 0

    for g_1, g_2 in combinations(galaxies, 2):
        row_min, row_max = sorted([g_1[0], g_2[0]])
        col_min, col_max = sorted([g_1[1], g_2[1]])

        num_empty_rows = len([row for row in empty_rows if row_min < row < row_max])
        num_empty_cols = len([col for col in empty_cols if col_min < col < col_max])

        row_dist = row_max - row_min + num_empty_rows * (expansion_coefficient - 1)
        col_dist = col_max - col_min + num_empty_cols * (expansion_coefficient - 1)

        distance_sum += row_dist + col_dist

    return distance_sum
