"""Logic of the brain gcd game."""

from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def set_parameters():
    """Set parameters to play.

    Returns:
        two random numbers from 1 to 100
    """
    num_one = randint(1, 100)
    num_two = randint(1, 100)
    return (num_one, num_two)


def find_greatest_divisor(num_one, num_two):
    """Find greatest common divisor of two numbers.

    Args:
        num_one: number more than 1
        num_two: number more than 1

    Returns:
        greatest common divisor
    """
    divisor = min(num_one, num_two)
    while divisor > 0:
        if (num_one % divisor == 0) and (num_two % divisor == 0):
            break
        divisor -= 1
    return divisor


def ask_and_calculate():
    """Prepare a question to user and calculate and return the correct answer.

    Returns:
        divisor: the greatest common divisor of two numbers
        question: string with prepared question
    """
    num_one, num_two = set_parameters()
    question = '{a} {b}'.format(a=num_one, b=num_two)
    greatest_divisor = find_greatest_divisor(num_one, num_two)
    return (str(greatest_divisor), question)
