Field = list[list]


def get_dimensions(field: Field):
    return len(field), len(field[0])


def iterate_field(field: Field):
    for i, row in enumerate(field):
        for j, item in enumerate(row):
            yield item, i, j


def iter_around(
    field: Field,
    y: int | list[int, int] | tuple[int, int],
    x: int | list[int, int] | tuple[int, int],
):
    hgt, wdt = get_dimensions(field)

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

    if top >= 0 and rgt < wdt:
        yield (top, rgt)

    if rgt < wdt:
        for j in range(top + 1, btm):
            yield (j, rgt)

    if btm < hgt and rgt < wdt:
        yield (btm, rgt)

    if btm < hgt:
        for i in reversed(range(lft + 1, rgt)):
            yield (btm, i)

    if btm < hgt and lft >= 0:
        yield (btm, lft)

    if lft >= 0:
        for j in reversed(range(top + 1, btm)):
            yield (j, lft)
