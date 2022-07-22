#!/usr/bin/env python

from ..games import gcd
from ..cli import game_template


def main():
    game_template(gcd, description="Find the great common divisor")


if __name__ == "__main__":
    main()
