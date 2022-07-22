#!/usr/bin/env python

from ..games_utils import game_template
from ..games import brain_even


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    game_template(brain_even, description)


if __name__ == "__main__":
    main()
