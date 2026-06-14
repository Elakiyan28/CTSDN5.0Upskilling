def split_bill(total_bill: int, people: int) -> int:
    if people <= 0:
        raise ValueError("Number of people must be positive")
    return total_bill // people

print("Each pays:", split_bill(1250, 4))
