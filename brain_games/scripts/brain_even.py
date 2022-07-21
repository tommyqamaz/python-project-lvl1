#!/usr/bin/env python

from ..cli import get_user_name
from ..games_utils import start_game
from ..games import brain_even


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    user_name = get_user_name()
    start_game(user_name, brain_even, description)


if __name__ == "__main__":
    main()
