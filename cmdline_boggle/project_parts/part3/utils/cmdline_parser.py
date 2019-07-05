import argparse
import os

from utils import boggle_game


DEFAULT_MIN_WORD_LEN = 3
DEFAULT_SIZE = 4

# Utility files are one level above
BASE_DIRPATH = os.path.dirname(os.path.abspath(__file__))
# TODO: The last argument here should be the name of your dictionary filename
DEFAULT_WORDS_FILENAME = os.path.join(BASE_DIRPATH, "..", "YOUR DICTIONARY FILENAME HERE")

GAME_CHOICES = [
    "BasicBoggleBoard",
    "WeightedBoggleBoard",
    "StandardBoggleBoard",
]

class CmdlineParser(object):
    def __init__(self):
        parser = argparse.ArgumentParser(description="Command-line Boggle game")
        parser.add_argument("--debug", action="store_true", help="Adds additional debug printing")

        # This doesn't matter for now, but it will after the last part of the project
        subparsers = parser.add_subparsers(dest="mode", help="Mode in which to run the program")
        subparsers.required = True
        play_parser = subparsers.add_parser("play", help="Play Command-line Boggle")

        # Subparser: play the game
        # TODO: Add arguments to the play parser
        # 1. winning_points -> points required to win the game
        # 2. rules -> if set to true, just print out the rules of the game (don't play)
        # 3. show_solver -> if set to true, show the solver after every round
        # 4. size -> the board size (use DEFAULT_SIZE as default)
        # 5. min_len -> minimum word length (use DEFAULT_MIN_WORD_LEN as default)
        # 6. words_file -> allow the user to overwrite the dictionary file (use DEFAULT_WORDS_FILENAME as default)
        # 7. board_type -> a choice of which board to play (see GAME_CHOICES above)
        pass

        self.env = parser.parse_args()

    def get_winning_points_threshold(self):
        # TODO: Return the value of the winning_points argument
        pass

    def should_only_print_rules(self):
        # TODO: Return the value of the rules argument
        pass

    def should_show_solver(self):
        # TODO: Return the value of the show_solver argument
        pass

    def get_words_filename(self):
        # TODO: Return the value of the words_file argument
        pass

    def debug_print(self, *args, **kwargs):
        if self.env.debug:
            print(*args, **kwargs)

    def get_boggle_game(self):
        # TODO: Create a new boggle game based on the board_type argument
        pass
