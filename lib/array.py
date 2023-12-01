def split_list(obj: list, index: int) -> tuple[list, list]:
    """Splits list into two at given index."""
    return obj[:index], obj[index:]


def product(obj: list):
    if len(obj) == 0:
        return 1

    prod = obj[0]
    for item in obj[1:]:
        prod *= item

    return prod
