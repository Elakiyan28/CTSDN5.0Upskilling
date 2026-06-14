def first_even(n: int) -> None:
    for i in range(1, n + 1):
        if i % 2 == 0:
            print("First even:", i)
            break

first_even(10)
