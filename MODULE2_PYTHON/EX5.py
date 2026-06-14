def show_coordinates(coords: tuple[int, int]) -> None:
    if len(coords) != 2:
        raise ValueError("Coordinates must be a pair (x, y)")
    x, y = coords
    print(f"Coordinates: x={x}, y={y}")

show_coordinates((10, 20))

