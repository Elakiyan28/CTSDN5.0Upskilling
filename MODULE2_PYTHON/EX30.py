def safe_divide(a: float, b: float) -> None:
    try:
        result = a / b
        print(f"Result: {result:.2f}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    except Exception as e:
        print("Unexpected error:", e)

safe_divide(10, 2)   
safe_divide(5, 0)    
