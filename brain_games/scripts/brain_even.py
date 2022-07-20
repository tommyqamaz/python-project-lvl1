#!/usr/bin/env python

from random import randint
from ..cli import welcome_user
from time import sleep


def start_game(user_name: str, limit: int = 3):
    """Mini game where you try to guess the even number."""

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while limit:
        generated_number = randint(0, 100)

        print(f"Question: {generated_number}")
        sleep(1)
        right_anser = ["yes", "no"][generated_number % 2]
        users_answer = input()
        sleep(0.5)
        print(f"Your answer: {users_answer}")
        if users_answer == right_anser:
            print("Correct!")
            limit -= 1
            if limit == 0:
                print(f"Congratulations, {user_name}!")
        else:
            print(
                f"'{users_answer}' is wrong answer ;(. Correct answer was '{right_anser}'."
            )
            print(f"Let's try again, {user_name}!")
            limit = 0


def main():
    user_name = welcome_user()
    start_game(user_name)


if __name__ == "__main__":
    main()
