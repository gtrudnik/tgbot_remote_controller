def read_config():
    try:
        with open("config.txt") as f:
            lines = f.readlines()
        token = lines[0].split("=")[-1].strip()
        password = lines[1].split("=")[-1].strip()
    except Exception:
        print("Created config.txt, you should edit it.")
        create_config("token_bot", "password")
        token, password = read_config()
    return token, password


def create_config(token_bot: str, password: str):
    with open("config.txt", "w") as f:
        f.write(f"token={token_bot}\n")
        f.write(f"password={password}\n")


def add_commands():
    pass

