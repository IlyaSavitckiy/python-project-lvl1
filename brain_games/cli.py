"""File with foo to greet operator."""

import prompt


def welcome_user():
    """Foo that greet people."""
    name = prompt.string('May I have your name? ')
    print('Hello, {a}!'.format(a=name))
