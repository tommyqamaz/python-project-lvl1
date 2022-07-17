import prompt


def welcome_user():
    """Greets the user by his name."""
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
