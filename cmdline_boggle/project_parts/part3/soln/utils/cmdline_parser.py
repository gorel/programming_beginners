import argparse
import os

from utils import boggle_game


DEFAULT_MIN_WORD_LEN = 3
DEFAULT_SIZE = 4

# Utility files are one level above
BASE_DIRPATH = os.path.dirname(os.path.abspath(__file__))
DEFAULT_WORDS_FILENAME = os.path.join(BASE_DIRPATH, "..", "words.txt")

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

        # Subparser: play the game
        play_parser = subparsers.add_parser("play", help="Play Command-line Boggle")
        play_parser.add_argument("-p", "--winning_points", type=int, default=50, help="Points required to win the game")
        play_parser.add_argument("-r", "--rules", action="store_true", help="Just display the rules and quit")
        play_parser.add_argument("--show_solver", action="store_true", help="After each round, show the best words possible")
        play_parser.add_argument("-s", "--size", type=int, default=DEFAULT_SIZE, help="Boggle board size")
        play_parser.add_argument("--min_len", type=int, default=DEFAULT_MIN_WORD_LEN, help="Minimum word length (makes the game harder)")
        play_parser.add_argument("-w", "--words_file", default=DEFAULT_WORDS_FILENAME, help="filename storing valid words (one per line)")
        play_parser.add_argument("-b", "--board_type", choices=GAME_CHOICES, help="The kind of Boggle board to generate")
        play_parser.set_defaults(which="play")

        self.env = parser.parse_args()

    def get_winning_points_threshold(self):
        return self.env.winning_points

    def should_only_print_rules(self):
        return self.env.rules

    def should_show_solver(self):
        return self.env.show_solver

    def get_words_filename(self):
        return self.env.words_file

    def debug_print(self, *args, **kwargs):
        if self.env.debug:
            print(*args, **kwargs)

    def get_boggle_game(self):
        if self.env.board_type == "BasicBoggleBoard":
            return boggle_game.BasicBoggleBoard(
                self,
                self.env.words_file,
                self.env.min_len,
                self.env.size,
            )
        elif self.env.board_type == "WeightedBoggleBoard":
            return boggle_game.WeightedBoggleBoard(
                self,
                self.env.words_file,
                self.env.min_len,
                self.env.size,
            )
        else:
            return boggle_game.StandardBoggleBoard(
                self,
                self.env.words_file,
                self.env.min_len,
                self.env.size,
            )
