def login(user: str, pwd: str) -> None:
    if user:
        if pwd:
            if user == "admin" and pwd == "pass123":
                print("Login successful")
            else:
                print("Invalid credentials")
        else:
            print("Password cannot be blank")
    else:
        print("Username cannot be blank")

login("admin", "pass123")
