"""Logic of the brain even game."""

from random import randint

RULES = 'Answer "yes" if number even otherwise answer "no".'


def set_parameters():
    """Set parameters to play.

    Returns:
        random number from 1 to 100
    """
    return randint(1, 100)


def ask_and_calculate():
    """Prepare a question to user and calculate and return the correct answer.

    Returns:
        correct_answer: yes or no, depends on is number even or not
        question: string with prepared question
    """
    game_parts = set_parameters()
    correct_answer = 'yes' if (game_parts % 2 == 0) else 'no'
    question = str(game_parts)
    return (correct_answer, question)
