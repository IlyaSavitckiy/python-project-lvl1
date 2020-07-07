#!/usr/bin/env python3
"""Start to play brain gcd game."""


from brain_games import engine
from brain_games.games import gcd


def main():
    """Start to play."""
    engine.play(gcd)


if __name__ == '__main__':
    main()
