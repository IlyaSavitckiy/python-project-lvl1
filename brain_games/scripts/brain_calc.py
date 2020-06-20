"""Start to play brain calc game."""


from brain_games import engine
from brain_games.games import calc


def main():
    """Start to play."""
    engine.start(calc)


if __name__ == '__main__':
    main()
