"""Start to play brain gcd game."""


from brain_games import engine
from brain_games.games import gcd


def main():
    """Start to play."""
    engine.start(gcd)


if __name__ == '__main__':
    main()
