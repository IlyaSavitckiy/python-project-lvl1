"""Logic of the brain calc game."""

from operator import add, mul, sub
from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'
OPERATORS = ('+', '-', '*')


def calculate(num_one, num_two, operator):
    """Calculate a result of an operation with 2 numbers using operator.

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


def prepare_question_and_calculate():
    """Prepare a question to user and calculate and return the correct answer.

    Returns:
        correct_answer: string-result of calculation with two ramdom numbers
        question: string with prepared question
    """
    num_one = randint(1, 100)
    num_two = randint(1, 100)
    operator = choice(OPERATORS)
    correct_answer = str(calculate(num_one, num_two, operator))
    question = '{0} {2} {1}'.format(num_one, num_two, operator)
    return (correct_answer, question)
