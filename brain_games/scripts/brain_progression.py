#!/usr/bin/env python3
"""Start to play brain progression game."""


from brain_games import engine
from brain_games.games import progression


def main():
    """Start to play."""
    engine.play(progression)


if __name__ == '__main__':
    main()
