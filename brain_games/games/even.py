"""Logic of the brain even game."""

from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def prepare_question_and_calculate():
    """Prepare a question to user and calculate and return the correct answer.

    Returns:
        correct_answer: 'yes' or 'no', depends on is number even or not
        question: string with prepared question
    """
    number_to_ask = randint(1, 100)
    correct_answer = 'yes' if (number_to_ask % 2 == 0) else 'no'
    question = str(number_to_ask)
    return (correct_answer, question)
