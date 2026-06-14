def rectangle_area(length: float, width: float) -> float:
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive")
    return length * width

print("Area of rectangle:", rectangle_area(5, 3))
