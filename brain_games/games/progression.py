"""Logic of the brain progression game."""

from random import randint

RULES = 'What number is missing in the progression?'


def make_progression():
    """Set progression to play the game.

    Returns:
        progression with 10 str(numbers) and random step
    """
    start = randint(1, 10)
    step = randint(1, 10)
    count = 0
    part = start
    progression = [str(start)]
    while count < 10:
        part += step
        progression.append(str(part))
        count += 1
    return progression


def set_parameters():
    """Set parameters to play.

    Returns:
        hidden_number: number to guess
        progression: progression by string with hidden_number
    """
    progression = make_progression()
    rand_index = randint(0, 9)
    hidden_number = str(progression[rand_index])
    progression[rand_index] = '...'
    return (hidden_number, progression)


def ask_question(parts):
    """Ask a question to user.

    Args:
        parts: parameters to play
    """
    progression = ' '.join(parts[1])
    print('Question: {pr}'.format(pr=progression))


def get_correct_answer(parts):
    """Take parameters to play, get correct answer and return it.

    Args:
        parts: parameters to play

    Returns:
        correct answer: hidden number from progression.
    """
    return parts[0]
