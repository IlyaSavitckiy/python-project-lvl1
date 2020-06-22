"""Logic of the brain prime game."""

from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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


def is_prime(parts):
    """Check if number is prime.

    Args:
        parts: number to check

    Returns:
        Boolean. True if number is prime
    """
    for divisor in range(2, round(parts / 2), 1):
        if parts % divisor == 0:
            return False
    return True


def get_correct_answer(parts):
    """Take a parameter to play and check if it is prime.

    Args:
        parts: parameters to play

    Returns:
        yes or no, depends on is number prime or not
    """
    return 'yes' if is_prime(parts) else 'no'
