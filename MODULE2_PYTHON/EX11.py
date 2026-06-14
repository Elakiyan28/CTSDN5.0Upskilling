def convert_weight():
    try:
        kg = float(input("Enter weight in kg: "))
        lbs = round(kg * 2.20462, 2)
        print(f"Weight in pounds: {lbs}")
    except ValueError:
        print("Invalid input: must be a decimal number")

convert_weight()
