#!/usr/bin/env python

from ..games import gcd
from ..games_utils import start_game
from ..cli import get_user_name


def main():
    user_name = get_user_name()
    start_game(user_name, gcd, description="Find the great common divisor")


if __name__ == "__main__":
    main()
