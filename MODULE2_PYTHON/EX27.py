def string_length(text: str) -> None:
    if not isinstance(text, str) or not text.strip():
        print("Invalid input: must be a non-empty string")
        return
    print(f"Length of '{text}': {len(text)}")

string_length("Python3")
