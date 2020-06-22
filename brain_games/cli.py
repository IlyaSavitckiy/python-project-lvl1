"""File with foo to greet operator."""

import prompt


def greeting():
    """Print common greeting."""
    print('Welcome to the Brain Games!')


def print_rules(rules):
    """Print rules of the game.

    Args:
        rules: string with rules
    """
    print(rules)


def welcome_user():
    """Take user's name and greet him.

    Returns:
        user's name
    """
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {name}!'.format(name=name))
    return name


def take_answer():
    """Take user's answer.

    Returns:
        user's answer
    """
    return prompt.string('Your answer: ')


def print_excuse(users_answer, correct_answer):
    """Print excuse if user's answer is wrong.

    Args:
        users_answer: user's answer
        correct_answer: calculated correct answer
    """
    print(
        """'{ua}' is wrong answer ;(. Correct answer was '{ca}'
        """.format(ua=users_answer, ca=correct_answer),
    )


def print_greeting(name):
    """Print to try to play again.

    Args:
        name: user's name
    """
    print("Let's try again, {n}!".format(n=name))


def print_congratulation(name):
    """Print congratulation when user wins the game.

    Args:
        name: user's name
    """
    print('Congratulations, {n}!'.format(n=name))
