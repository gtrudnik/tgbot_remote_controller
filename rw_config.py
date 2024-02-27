def read_config():
    try:
        with open("config.txt") as f:
            lines = f.readlines()
        token = lines[0].split("=")[-1].strip()
        password = lines[1].split("=")[-1].strip()
    except Exception:
        create_config()
        token, password = read_config()
    return token, password


def create_config():
    with open("config.txt", "w") as f:
        f.write("token=my_token\n")
        f.write("password=12345678\n")


def add_commands():
    pass


print(read_config())