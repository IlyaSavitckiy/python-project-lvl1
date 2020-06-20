"""Engine of all brain games."""


from brain_games import cli


def start(game):
    """Run engine to run brain games.

    Args:
        game: name of a game to run
    """
    cli.greeting()
    game.print_rules()
    name = cli.welcome_user()
    rounds = 3
    while rounds > 0:
        game_parts = game.set_parameters()
        game.ask_question(game_parts)
        users_answer = game.take_answer()
        correct_answer = game.get_correct_answer(game_parts)
        if correct_answer != users_answer:
            cli.print_excuse(users_answer, correct_answer)
            cli.print_greeting(name)
            break
        cli.print_correct()
        rounds -= 1
    if rounds == 0:
        cli.print_congratulation(name)
