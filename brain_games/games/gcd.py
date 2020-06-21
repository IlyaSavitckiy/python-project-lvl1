"""Logic of the brain gcd game."""

from random import randint

import prompt

RULES = 'Find the greatest common divisor of given numbers.'


def set_parameters():
    """Set parameters to play.

    Returns:
        two random numbers from 1 to 100
    """
    return (randint(1, 100), randint(1, 100))


def ask_question(parts):
    """Ask a question to user.

    Args:
        parts: parameters to play
    """
    num_one, num_two = parts
    print('Question: {a} {b}'.format(a=num_one, b=num_two))


def take_answer():
    """Take user's answer.

    Returns:
        user's answer
    """
    return prompt.integer('Your answer: ')


def is_divise(num, divisor):
    """Check if num divise by divisor.

    Args:
        num: random number
        divisor: number

    Returns:
        bool
    """
    return num % divisor == 0


def get_correct_answer(parts):
    """Take parameters to play, get correct answer and return it.

    Args:
        parts: parameters to play

    Returns:
        correct answer: the greatest common divisor of two numbers.
    """
    num_one, num_two = parts
    divisor = min(num_one, num_two)
    while divisor >= 1:
        if is_divise(num_one, divisor) and is_divise(num_two, divisor):
            return divisor
        divisor -= 1
    return divisor
