from ..cli import get_user_name
from ..games_utils import start_game
from ..games import progression


def main():
    users_name = get_user_name()
    start_game(
        users_name,
        progression,
        description="What number is missing in the progression?",
    )


if __name__ == "__main__":
    main()
