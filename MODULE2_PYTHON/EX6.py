def check_even_odd(number: int) -> str:
    if not isinstance(number, int):
        raise TypeError("Number must be an integer")
    return "Even" if number % 2 == 0 else "Odd"

print(check_even_odd(17))
