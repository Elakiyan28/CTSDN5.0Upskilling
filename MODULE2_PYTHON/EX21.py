def nested_check(a: bool, b: bool) -> None:
    if a:
        if b:
            print("Nested")
    print("Check complete")

nested_check(True, True)
