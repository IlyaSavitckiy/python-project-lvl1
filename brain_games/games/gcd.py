"""Logic of the brain gcd game."""

from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_greatest_common_divisor(num_one, num_two):
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


def prepare_question_and_calculate():
    """Prepare a question to user and calculate and return the correct answer.

    Returns:
        divisor: string with the greatest common divisor of two numbers
        question: string with prepared question
    """
    num_one = randint(1, 100)
    num_two = randint(1, 100)
    question = '{0} {1}'.format(num_one, num_two)
    greatest_divisor = str(find_greatest_common_divisor(num_one, num_two))
    return (greatest_divisor, question)
