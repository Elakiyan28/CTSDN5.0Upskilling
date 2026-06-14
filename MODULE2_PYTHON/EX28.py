def write_greeting(filename: str) -> None:
    try:
        with open(filename, "w") as f:
            f.write("Hello World")
        print(f"Greeting saved to {filename}")
    except Exception as e:
        print("Error writing file:", e)

write_greeting("greeting.txt")
