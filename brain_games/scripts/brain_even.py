#!/usr/bin/env python

from random import randint
from ..cli import welcome_user


def start_game(user_name: str):
    """Mini game where you try to guess the even number."""

    limit = 3
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while limit:
        generated_number = randint(0, 100)

        print(f"Question: {generated_number}")

        right_anser = ["yes", "no"][generated_number % 2]
        users_answer = input()

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
            break


def main():
    user_name = welcome_user()
    start_game(user_name)


if __name__ == "__main__":
    main()
