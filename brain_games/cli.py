"""File with foo to greet operator."""

import prompt


def greeting():
    """Just print a common greeting."""
    print('Welcome to the Brain Games!')


def welcome_user():
    """
    Take operator's name, greet him and return name value.

    Returns:
        Operator's name.
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    return name
