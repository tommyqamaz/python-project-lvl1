from ..cli import get_user_name
from ..games_utils import start_game
from ..games import gcd


def main():
    users_name = get_user_name()
    start_game(users_name, gcd, description="Find the great common divisor")


if __name__ == "__main__":
    main()
