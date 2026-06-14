def read_file(filename: str) -> None:
    try:
        with open(filename, "r") as f:
            content = f.read()
        print("File Content:\n", content)
    except FileNotFoundError:
        print(f"Error: {filename} not found")
    except Exception as e:
        print("Error reading file:", e)

read_file("greeting.txt")
