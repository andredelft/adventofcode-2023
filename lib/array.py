def split_list(obj: list, index: int) -> tuple[list, list]:
    """Splits list into two at given index."""
    return obj[:index], obj[index:]


def product(obj: list):
    prod = 1

    for item in obj:
        prod *= item

    return prod
