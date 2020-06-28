"""Engine of brain games."""


import prompt


def print_rules(rules):
    """Print rules of the game.

    Args:
        rules: string with rules
    """
    print(rules)


def welcome_user():
    """Take user's name, greet him and return user's name.

    Returns:
        user's name
    """
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {n}!'.format(n=name))
    return name


def take_answer():
    """Take user's answer and return it.

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
    """Print greeting to try to play again.

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


def start(game):
    """Start engine to run brain games.

    Args:
        game: name of a game to run
    """
    print('Welcome to the Brain Games!')
    print_rules(game.RULES)
    name = welcome_user()
    rounds = 3
    while rounds > 0:
        game_parts = game.set_parameters()
        game.ask_question(game_parts)
        users_answer = take_answer()
        correct_answer = game.get_correct_answer(game_parts)
        if correct_answer != users_answer:
            print_excuse(users_answer, correct_answer)
            print_greeting(name)
            break
        print('Correct!')
        rounds -= 1
    if rounds == 0:
        print_congratulation(name)
