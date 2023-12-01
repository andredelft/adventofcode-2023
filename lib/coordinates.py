Coordinate = tuple[int, int]
Coordinates = set[Coordinate]

Dimensions = tuple[list[int, int], list[int, int]]


def get_dimensions(
    coordinates: Coordinates, initial_coordinate: Coordinate | None = None
) -> Dimensions:
    coordinate_list = list(coordinates)
    if not initial_coordinate:
        initial_coordinate = coordinate_list[0]
        coordinate_list = coordinate_list[1:]

    y = [initial_coordinate[0], initial_coordinate[0]]
    x = [initial_coordinate[1], initial_coordinate[1]]

    for coord in coordinate_list:
        y[0] = min(coord[0] - 1, y[0])
        y[1] = max(coord[0] + 2, y[1])
        x[0] = min(coord[1] - 1, x[0])
        x[1] = max(coord[1] + 2, x[1])

    return y, x
