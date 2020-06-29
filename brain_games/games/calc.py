"""Logic of the brain calc game."""

from operator import add, mul, sub
from random import choice, randint

RULES = 'What is the result of the expression?'
OPERATORS = ('+', '-', '*')


def make_operation(num_one, num_two, operator):
    """Make an operation with 2 numbers using operator.

    Args:
        num_one: some number
        num_two: some number
        operator: some operator from OPERATORS

    Returns:
        result of the operation
    """
    if operator == '+':
        return add(num_one, num_two)
    elif operator == '-':
        return sub(num_one, num_two)
    elif operator == '*':
        return mul(num_one, num_two)


def set_parameters():
    """Set parameters to play.

    Returns:
        two random numbers from 1 to 100 and operator
    """
    num_one = randint(1, 100)
    num_two = randint(1, 100)
    operator = choice(OPERATORS)
    return (num_one, num_two, operator)


def ask_and_calculate():
    """Prepare a question to user and calculate and return the correct answer.

    Returns:
        result_of_operation: result of operation with two ramdom numbers
        question: string with prepared question
    """
    num_one, num_two, operator = set_parameters()
    result_of_operation = str(make_operation(num_one, num_two, operator))
    question = '{a} {op} {b}'.format(a=num_one, b=num_two, op=operator)
    return (result_of_operation, question)
