from bisect import bisect_left, insort


def split_list(obj: list, index: int) -> tuple[list, list]:
    """Splits list into two at given index."""
    return obj[:index], obj[index:]


def product(obj: list):
    prod = 1

    for item in obj:
        prod *= item

    return prod


class SortedList(object):
    def __init__(self, lst, key=None):
        self._lst = sorted(lst, key=key)
        self._key = key

    def __str__(self):
        return str(self._lst)

    def __repr__(self):
        return f"<SortedList {repr(self._lst)}>"

    def pop(self, index):
        return self._lst.pop(index)

    def add(self, item):
        insort(self._lst, item, key=self._key)

    def find(self, item):
        lookup_value = self._key(item) if self._key else item
        index = bisect_left(self._lst, lookup_value, key=self._key)

        while self._lst[index] != item:
            index += 1
            if self._key(item) != lookup_value:
                return -1

        return index
