"""Module."""

from brain_games import cli


def main():
    """Take user's name and greet him."""
    print('Welcome to the Brain Games!')
    cli.welcome_user()


if __name__ == '__main__':
    main()
