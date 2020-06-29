"""Logic of the brain prime game."""

from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    """Check if number is prime.

    Args:
        num: number to check

    Returns:
        Boolean. True if number is prime
    """
    for divisor in range(2, round(num / 2), 1):
        if num % divisor == 0:
            return False
    return True


def set_parameters():
    """Set parameters to play.

    Returns:
        random number from 1 to 100
    """
    return randint(1, 100)


def ask_and_calculate():
    """Prepare a question to user and calculate and return the correct answer.

    Returns:
        correct_answer: yes or no, depends on is number prime or not
        question: string with prepared question
    """
    game_parts = set_parameters()
    question = '{n}'.format(n=game_parts)
    correct_answer = 'yes' if is_prime(game_parts) else 'no'
    return (correct_answer, question)
