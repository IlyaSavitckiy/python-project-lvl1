#!/usr/bin/env python3
"""This is the script of brain prime game."""


from brain_games import engine
from brain_games.games import prime


def main():
    """Start to play."""
    engine.start(prime)


if __name__ == '__main__':
    main()
