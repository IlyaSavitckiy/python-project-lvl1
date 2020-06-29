"""Logic of the brain progression game."""

from random import randint

RULES = 'What number is missing in the progression?'


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
    progression = [str(start)]
    while counter < size:
        element += step
        progression.append(str(element))
        counter += 1
    return progression


def set_parameters():
    """Set parameters to play.

    Returns:
        progression made with random numbers
    """
    start = randint(1, 10)
    step = randint(1, 10)
    size = 10
    return build_progression(start, step, size)


def ask_and_calculate():
    """Prepare a question to user and calculate and return the correct answer.

    Returns:
        hidden number: hidden from progression
        question: string with prepared question
    """
    game_parts = set_parameters()
    random_index = randint(0, 9)
    hidden_number = game_parts[random_index]
    game_parts[random_index] = '...'
    question = ' '.join(game_parts)
    return (hidden_number, question)
