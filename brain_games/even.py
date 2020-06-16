"""Logic of the brain even game."""

from random import randint

import prompt

RULES = 'Answer "yes" if number even otherwise answer "no".\n'


def is_even(num):
    """
    Look if number is even.

    Args:
        num: random number to check is it even.

    Returns:
        Boolean. True if number is even.
    """
    even = num % 2 == 0
    return 'yes' if even else 'no'


def get_answer(num):
    """
    Get operator's answer.

    Args:
        num: random number to show it to operator.

    Returns:
        Operator's answer: yes if the num is even otherwise no.
    """
    print('Question: {n}'.format(n=num))
    return prompt.string('Your answer: ')


def even_game(name):
    """
    Logic of game.

    Args:
        name: operator's name
    """
    game_count = 3
    while game_count > 0:
        num = randint(1, 100)
        right_answer = is_even(num)
        operators_answer = get_answer(num)
        if right_answer != operators_answer:
            print(
                """'{a}' is wrong answer ;(. Correct answer was '{b}'.
Let's try again, {c}!
                """.format(a=operators_answer, b=right_answer, c=name),
            )
            break
        print('Correct!')
        game_count -= 1
    if game_count == 0:
        print('Congratulations, {c}!'.format(c=name))
