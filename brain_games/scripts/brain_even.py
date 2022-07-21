#!/usr/bin/env python

from random import randint
from ..cli import welcome_user
from ..check_answer import check_answer


def start_game(user_name: str, limit: int = 3):
    """Mini game where you try to guess the even number."""

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while limit:
        generated_number = randint(0, 100)

        print(f"Question: {generated_number}")
        right_answer = ["yes", "no"][generated_number % 2]
        users_answer = input()
        result = check_answer(users_answer, right_answer, user_name)
        if result:
            limit -= 1
        else:
            break

    if result:
        print(f"Congratulations, {user_name}!")


def main():
    user_name = welcome_user()
    start_game(user_name)


if __name__ == "__main__":
    main()
