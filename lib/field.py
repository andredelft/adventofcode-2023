from typing import Generator

Coordinate = tuple[int, int]


class Field(object):
    def __init__(self, field: list[list[str]] | list[str] | str):
        if isinstance(field, str):
            self.field = [list(line) for line in field.split("\n")]
        else:
            self.field = [list(line) for line in field]

        self.height = len(self.field)
        self.width = len(self.field[0])

    def __repr__(self):
        return f"<Field ({self.height}x{self.width})>"

    def __str__(self):
        return "\n".join("".join(line) for line in self.field)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        if isinstance(other, Field):
            return self.field == other.field

    def __len__(self):
        return self.height * self.width

    def __getitem__(self, coord: Coordinate):
        return self.field[coord[0]][coord[1]]

    def __setitem__(self, key: tuple[int, int], value):
        self.field[key[0]][key[1]] = value

    def __iter__(self):
        for coord in self.coords():
            yield self[coord]

    def coords(self) -> Generator[Coordinate, None, None]:
        for j in range(self.height):
            for i in range(self.width):
                yield (j, i)

    def enumerate(self):
        for coord in self.coords():
            yield coord, self[coord]

    def row(self, index: int, joined=False):
        _row = self[index]
        return "".join(_row) if joined else _row

    def col(self, index: int, joined=False):
        _col = [self[j, index] for j in range(self.height)]
        return "".join(_col) if joined else _col

    def rows(self, joined=False):
        for j in range(self.height):
            _row = self[j]
            yield "".join(_row) if joined else _row

    def cols(self, joined=False):
        for i in range(self.width):
            _col = [self[j, i] for j in range(self.height)]
            yield "".join(_col) if joined else _col

    def coords_around(
        self,
        y: int | list[int, int] | tuple[int, int],
        x: int | list[int, int] | tuple[int, int],
    ):
        if isinstance(y, list) or isinstance(y, tuple):
            top = y[0] - 1
            btm = y[1]
        else:
            top = y - 1
            btm = y + 1

        if isinstance(x, list) or isinstance(x, tuple):
            lft = x[0] - 1
            rgt = x[1]
        else:
            lft = x - 1
            rgt = x + 1

        if top >= 0 and lft >= 0:
            yield (top, lft)

        if top >= 0:
            for i in range(lft + 1, rgt):
                yield (top, i)

        if top >= 0 and rgt < self.width:
            yield (top, rgt)

        if rgt < self.width:
            for j in range(top + 1, btm):
                yield (j, rgt)

        if btm < self.height and rgt < self.width:
            yield (btm, rgt)

        if btm < self.height:
            for i in reversed(range(lft + 1, rgt)):
                yield (btm, i)

        if btm < self.height and lft >= 0:
            yield (btm, lft)

        if lft >= 0:
            for j in reversed(range(top + 1, btm)):
                yield (j, lft)

    def contains(self, coord: Coordinate):
        return 0 <= coord[0] < self.height and 0 <= coord[1] < self.width

    def copy(self):
        return Field([_row.copy() for _row in self.rows()])
