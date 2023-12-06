import re


def parse_number(string: str) -> int | None:
    """Searches for first occurence of a number in a given string, and returns it as an integer if found, and None otherwise."""
    n = re.search(r"\d+", string)
    return int(n.group()) if n else None


def parse_numbers(string: str) -> list[int]:
    """Searches for all occurences of a number in a given string, and returns it as list of integers."""
    return [int(n) for n in re.findall(r"\d+", string)]


def is_num(string: str) -> bool:
    return re.search(r"^\d+$", string)
