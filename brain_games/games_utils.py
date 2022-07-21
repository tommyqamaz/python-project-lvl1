from typing import Any
from typing import Callable


def check_answer(users_answer: Any, right_answer: Any, user_name: str) -> bool:
    """Check answer for games programms."""
    print(f"Your answer: {users_answer}")
    if users_answer == right_answer:
        print("Correct!")
        return True
    else:
        print(
            f"'{users_answer}' is wrong answer ;(. Correct answer was '{right_answer}'."
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
    answer_fn - functions or Callable which returns tuple of question and right answer
    limit - number of correct answers to win
    description - description of the game to show user
    """

    if description is not None:
        print(f"{description}")

    while limit:

        question, right_answer = answer_fn()

        print(f"Question: {question}")

        users_answer = input()

        result = check_answer(users_answer, right_answer, user_name)

        if result:
            limit -= 1
        else:
            break

    if result:
        print(f"Congratulations, {user_name}!")
