"""Logic of the brain calc game."""

from random import choice, randint

import prompt

RULES = 'What is the result of the expression?'
operators = ['+', '-', '*']


def set_parameters():
    """Set parameters to play.

    Returns:
        two random numbers from 1 to 100 and operator
    """
    return (randint(1, 100), randint(1, 100), choice(operators))


def ask_question(parts):
    """Ask a question to user.

    Args:
        parts: parameters to play
    """
    num_one, num_two, operator = parts
    print('Question: {a} {op} {b}'.format(a=num_one, b=num_two, op=operator))


def take_answer():
    """Take user's answer.

    Returns:
        user's answer
    """
    return prompt.integer('Your answer: ')


def get_correct_answer(parts):
    """Take parameters to play, get correct answer and return it.

    Args:
        parts: parameters to play

    Returns:
        correct answer: result of operation with two ramdom numbers.
    """
    num_one, num_two, operator = parts
    if operator == '+':
        return num_one + num_two
    elif operator == '-':
        return num_one - num_two
    elif operator == '*':
        return num_one * num_two
