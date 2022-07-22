#!/usr/bin/env python

from ..cli import get_user_name
from ..games_utils import start_game
from ..games import prime


def main():
    users_name = get_user_name()
    start_game(
        users_name,
        prime,
        'Answer "yes" if given number is prime. Otherwise answer "no".',
    )


if __name__ == "__main__":
    main()
