from typing import Any


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
