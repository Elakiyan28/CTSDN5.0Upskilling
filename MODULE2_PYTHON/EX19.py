def sum_odds(limit: int) -> None:
    total = 0
    for i in range(limit):
        if i % 2 == 0:
            continue
        total += i
    print("Sum of odd numbers:", total)

sum_odds(10)
