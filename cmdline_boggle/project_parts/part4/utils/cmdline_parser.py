import argparse
import os

from utils import boggle_game
from utils import scoring


DEFAULT_MIN_WORD_LEN = 3
DEFAULT_SIZE = 4

# Utility files are one level above
BASE_DIRPATH = os.path.dirname(os.path.abspath(__file__))
DEFAULT_HIGH_SCORES_FILENAME = os.path.join(BASE_DIRPATH, "..", "high_scores.bgm")
DEFAULT_WORDS_FILENAME = os.path.join(BASE_DIRPATH, "..", "words.txt")

GAME_CHOICES = [
    "BasicBoggleBoard",
    "WeightedBoggleBoard",
    "StandardBoggleBoard",
]

class CmdlineParser(object):
    def __init__(self):
        parser = argparse.ArgumentParser(description="Command-line Boggle game")
        # TODO: Add an argument "scores_file" for the file we will use for high scores (DEFAULT_HIGH_SCORES_FILENAME as default)
        parser.add_argument("--debug", action="store_true", help="Adds additional debug printing")

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
        # TODO: Add an argument "no_high_scores" which stores a boolean if the user wants to ignore high score tracking for this game
        play_parser.set_defaults(which="play")

        # Subparser: show high scores
        # TODO: Add a new parser to the subparsers list for "highscores" that will simply be used to show the list of highscores and exit

        self.env = parser.parse_args()

    def get_winning_points_threshold(self):
        return self.env.winning_points

    def should_only_print_rules(self):
        return self.env.rules

    def should_show_solver(self):
        return self.env.show_solver

    def get_words_filename(self):
        return self.env.words_file

    def should_only_print_highscores(self):
        return self.env.which == "highscores"

    def debug_print(self, *args, **kwargs):
        if self.env.debug:
            print(*args, **kwargs)

    def get_high_scores_object(self):
        # Ignore the flag if the user chose "highscores"
        if self.env.which != "highscores" and self.env.no_high_scores:
            return scoring.DummyHighScores()
        else:
            return scoring.HighScores(self.env.scores_file)

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
