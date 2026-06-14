def next_year_age():
    try:
        age = int(input("Enter your age: "))
        print(f"Next year you'll be {age + 1}")
    except ValueError:
        print("Invalid input: must be a number")

next_year_age()
