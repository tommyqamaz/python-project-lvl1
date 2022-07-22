#!/usr/bin/env python

from ..games_utils import game_template
from ..games import progression


def main():
    game_template(
        progression,
        description="What number is missing in the progression?",
    )


if __name__ == "__main__":
    main()
