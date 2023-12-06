Number = int | float


def solve_quadratic(a: Number, b: Number, c: Number) -> list[float]:
    """Solve the quadratic equation `ax ** 2 + bx + c == 0` with `a != 0`"""

    determinant = b**2 - 4 * a * c

    if determinant > 0:
        numerator_1 = -1 * b - (determinant) ** 0.5
        numerator_2 = -1 * b + (determinant) ** 0.5
        denominator = 2 * a

        sol_1 = numerator_1 / denominator
        sol_2 = numerator_2 / denominator

        return [sol_1, sol_2] if a > 0 else [sol_2, sol_1]
    elif determinant == 0:
        return [-1 * b / (2 * a)]
    else:
        return []
