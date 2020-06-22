#!/usr/bin/env python3
"""This is the script of brain even game."""


from brain_games import engine
from brain_games.games import even


def main():
    """Start to play."""
    engine.start(even)


if __name__ == '__main__':
    main()
