from collections import Counter

from .array import product

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


def iter_prime_factors(num: int):
    """Very primitive prime factorization method, works fine for prime factors < 10^6"""
    factor = 2
    while num != 1:
        while num % factor == 0:
            yield factor
            num //= factor
        factor += 1


def prime_factors(num: int):
    return list(iter_prime_factors(num))


def lcm(*nums: int):
    """The least common multiple of given numbers"""
    prime_union = Counter()
    for num in nums:
        new_primes = Counter(iter_prime_factors(num))

        for prime, num_factors in new_primes.items():
            prime_union[prime] = max(prime_union[prime], num_factors)

    return product(prime_union.elements())


def gcd(*nums: int):
    """The greatest common divider of given numbers"""
    if not nums:
        return 1

    common_primes = Counter(iter_prime_factors(nums[0]))
    for num in nums[1:]:
        new_primes = Counter(iter_prime_factors(num))

        for prime, num_factors in common_primes.items():
            common_primes[prime] = min(num_factors, new_primes[prime])

        if not common_primes:
            break

    return product(common_primes.elements())
