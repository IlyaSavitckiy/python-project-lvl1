"""Engine of brain games."""


import prompt


def play(game):
    """Start engine and run brain games.

    Args:
        game: name of a game to run
    """
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {0}!'.format(name))
    rounds_count = 3
    while rounds_count > 0:
        correct_answer, question = game.prepare_question_and_calculate()
        print('Question: {0}'.format(question))
        users_answer = prompt.string('Your answer: ')
        if correct_answer != users_answer:
            print(
                """'{0}' is wrong answer ;(. Correct answer was '{1}'
                """.format(users_answer, correct_answer),
            )
            print("Let's try again, {0}!".format(name))
            return
        print('Correct!')
        rounds_count -= 1
    print('Congratulations, {0}!'.format(name))
