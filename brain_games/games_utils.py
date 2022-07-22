from typing import Callable
from .cli import get_user_name


def check_answer(users_answer: str, right_answer: str, user_name: str) -> bool:
    """Check answer for games programms."""
    print(f"Your answer: {users_answer}")
    if str(users_answer) == str(right_answer):
        print("Correct!")
        return True
    else:
        print(
            f"'{users_answer}' is wrong answer ;(.",
            f"Correct answer was '{right_answer}'.\n",
            end="",
        )
        print(f"Let's try again, {user_name}!")
        return False


def start_game(
    user_name: str,
    answer_fn: Callable,
    description: str = None,
    limit: int = 3,
):

    """
    Cli mini game main module.

    user_name - the name of user
    answer_fn - functions or Callable which
    returns tuple of question and right answer

    limit - number of correct answers to win
    description - description of the game to show user
    """

    if description is not None:
        print(f"{description}")

    while limit:

        question, right_answer = answer_fn()

        users_answer = input(f"Question: {question}\n")

        result = check_answer(users_answer, right_answer, user_name)

        if not result:
            break

        limit -= 1

    if result:
        print(f"Congratulations, {user_name}!")


def game_template(game, desc=None):
    users_name = get_user_name()
    start_game(users_name, game, desc)
