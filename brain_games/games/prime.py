"""Logic of the brain prime game."""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    """Check if number is prime.

    Args:
        num: number to check

    Returns:
        Boolean. True if number is prime
    """
    if num <= 1:
        return False
    for divisor in range(2, round(num / 2), 1):
        if num % divisor == 0:
            return False
    return True


def prepare_question_and_calculate():
    """Prepare a question to user and calculate and return the correct answer.

    Returns:
        correct_answer: 'yes' or 'no', depends on is number prime or not
        question: string with prepared question
    """
    number_to_ask = randint(1, 100)
    question = str(number_to_ask)
    correct_answer = 'yes' if is_prime(number_to_ask) else 'no'
    return (correct_answer, question)
