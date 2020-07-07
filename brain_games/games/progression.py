"""Logic of the brain progression game."""

from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def build_progression(start, step, size):
    """Set progression to play the game.

    Args:
        start: first number to build a progression
        step: step of progression
        size: amount of numbers in progression

    Returns:
        progression with 10 str(numbers) and random step
    """
    counter = 0
    element = start
    progression = []
    while counter < size:
        progression.append(str(element))
        element += step
        counter += 1
    return progression


def prepare_question_and_calculate():
    """Prepare a question to user and calculate and return the correct answer.

    Returns:
        hidden number: hidden from progression
        question: string with prepared question
    """
    progression = build_progression(
        randint(1, 10), randint(1, 10), 10,
    )
    random_index = randint(0, len(progression) - 1)
    hidden_number = progression[random_index]
    progression[random_index] = '...'
    question = ' '.join(progression)
    return (hidden_number, question)
