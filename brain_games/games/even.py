"""Logic of the brain even game."""

from random import randint

import prompt

RULES = 'Answer "yes" if number even otherwise answer "no".'


def print_rules():
    """Print rules of the game."""
    print(RULES)


def set_parameters():
    """Set parameters to play.

    Returns:
        random number from 1 to 100
    """
    return randint(1, 100)


def ask_question(parts):
    """Ask a question to user.

    Args:
        parts: parameters to play
    """
    num = parts
    print('Question: {n}'.format(n=num))


def take_answer():
    """Take user's answer.

    Returns:
        user's answer
    """
    return prompt.string('Your answer: ')


def get_correct_answer(parts):
    """Take a parameter to play and check if it is even.

    Args:
        parts: parameters to play

    Returns:
        Boolean. True if number is even.
    """
    num = parts
    return 'yes' if (num % 2 == 0) else 'no'
