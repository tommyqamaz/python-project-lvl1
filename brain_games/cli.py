import prompt


def get_user_name():
    """Greets the user by his name."""
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name
