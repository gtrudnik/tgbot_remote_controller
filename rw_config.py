def get_commands():
    with open("config.txt") as f:
        commands = [i.split("#")[0] for i in f.readlines()]
    return commands


def add_commands():
    pass


print(get_commands())