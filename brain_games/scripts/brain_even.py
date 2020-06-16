"""This is the script of brain even game."""


from brain_games import cli, even


def main():
    """Script to play the game."""
    cli.greeting()
    print(even.RULES)
    name = cli.welcome_user()  # takes user's name and greet him
    even.even_game(name)


if __name__ == '__main__':
    main()
