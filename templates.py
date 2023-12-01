TEMPLATE = """\
def parse_input(input_string: str):
    return input_string


def solve_a(input_string: str):
    parse_input(input_string)


def solve_b(input_string: str):
    parse_input(input_string)
"""

TEST_TEMPLATE = """\
from {day_path}.{module_name} import solve_a, solve_b

TEST_INPUT = \"\"\"\\
\"\"\"

EXPECTED_SOLUTION_A = None
EXPECTED_SOLUTION_B = None


def test_a():
    assert solve_a() == EXPECTED_SOLUTION_A


def test_b():
    assert solve_b() == EXPECTED_SOLUTION_B
"""
