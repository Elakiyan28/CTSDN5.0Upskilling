import math

def circle_area(radius: float) -> float:
    if radius <= 0:
        raise ValueError("Radius must be positive")
    return round(math.pi * radius ** 2, 2)

print("Area of circle:", circle_area(7))
