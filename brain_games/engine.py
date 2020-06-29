"""Engine of brain games."""


import prompt


def start(game):
    """Start engine to run brain games.

    Args:
        game: name of a game to run
    """
    print('Welcome to the Brain Games!')
    print(game.RULES)
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {n}!'.format(n=name))
    rounds = 3
    while rounds > 0:
        correct_answer, question = game.ask_and_calculate()
        print('Question: {q}'.format(q=question))
        users_answer = prompt.string('Your answer: ')
        if correct_answer != users_answer:
            print(
                """'{ua}' is wrong answer ;(. Correct answer was '{ca}'
                """.format(ua=users_answer, ca=correct_answer),
            )
            print("Let's try again, {n}!".format(n=name))
            break
        print('Correct!')
        rounds -= 1
    if rounds == 0:
        print('Congratulations, {n}!'.format(n=name))
