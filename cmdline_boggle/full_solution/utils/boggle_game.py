import random
import string

from utils import dictionary
from utils import scoring


MAX_WORD_LEN = 16


class BasicBoggleBoard(object):
    def __init__(self, env, words_filename, min_word_len, board_size):
        self.env = env
        self.dictionary = dictionary.Dictionary(words_filename, min_word_len, MAX_WORD_LEN)
        self.size = board_size
        self.gen_board()

    def gen_board(self):
        self.board = []
        for _ in range(self.size):
            next_row = []
            for _ in range(self.size):
                next_row.append(random.choice(string.ascii_uppercase))
            self.board.append(next_row)

    def is_word_possible_on_board(self, word):
        # Inefficient, but board size is usually small, so we don't really care right now
        # First change word to uppercase since that's how our board is represented
        word = word.upper()
        for start_row in range(self.size):
            for start_col in range(self.size):
                if self.find_path(start_row, start_col, word):
                    return True
        return False

    def find_path(self, row, col, word):
        # base case
        if word == "":
            return True
        # Bounds checking
        if row < 0 or col < 0 or row >= len(self.board) or col >= len(self.board):
            return False
        # Doesn't work here
        target_char = word[0]
        if self.board[row][col] != target_char:
            return False

        # Try each direction
        dirs = [-1, 0, 1]
        for row_dir in dirs:
            for col_dir in dirs:
                if row_dir == 0 and col_dir == 0:
                    continue
                new_row = row + row_dir
                new_col = col + col_dir
                # Temporarily set this space as None so we won't backtrack on it
                self.board[row][col] = None
                possible = self.find_path(new_row, new_col, word[1:])
                # Reset this space
                self.board[row][col] = target_char
                if possible:
                    return True
        # No path yielded a solution
        return False

    def score_words(self, words, high_scores):
        total = 0
        for word in words:
            if self.dictionary.word_exists(word):
                if not self.is_word_possible_on_board(word):
                    print(f"Uh oh, it doesn't look like it's possible to get {word} on this board!")
                    continue
                score = self.score_word(word)

                # Check for new best word score
                high_scores.maybe_insert_new_high_score(self, scoring.TOP_WORD_KEY, score, word)

                total += score
                point_plural = "point"
                if score > 1:
                    point_plural = "points"
                print(f"{word} is worth {score} {point_plural} (now at {total})")
            else:
                print(f"Sorry, but {word} is not a word in the dictionary!")

        points_plural = "point"
        if total != 1:
            points_plural = "points"
        print(f"In total, you scored {total} {points_plural} this round!")
        return total

    def score_word(self, word):
        if len(word) < 3:
            return 0
        if len(word) == 3 or len(word) == 4:
            return 1
        elif len(word) == 5:
            return 2
        elif len(word) == 6:
            return 3
        elif len(word) == 7:
            return 5
        else:
            return 11

    def __str__(self):
        res = ""
        return "\n".join(
            " ".join(row)
            for row in self.board
        )

class WeightedBoggleBoard(BasicBoggleBoard):
    WEIGHTS = {
        'A': 6, 'B': 2, 'C': 2, 'D': 3,
        'E': 11, 'F': 2, 'G': 2, 'H': 5,
        'I': 6, 'J': 1, 'K': 1, 'L': 4,
        'M': 3, 'N': 6, 'O': 7, 'P': 2,
        # 'Q' is unused
        'R': 5, 'S': 6, 'T': 9, 'U': 3,
        'V': 2, 'W': 3, 'X': 1, 'Y': 3,
        'Z': 1,
    }

    def __init__(self, env, words_filename, min_word_len, board_size):
        super().__init__(env, words_filename, min_word_len, board_size)

    def weighted_choice(self, weighted_dict):
        random_value = random.uniform(sum(weighted_dict.values()))
        current_value = 0
        for letter, weight in weighted_dict.items():
            if current_value + weight >= random_value:
                return letter
            current_value += weight

    # override
    def gen_board(self):
        self.board = []
        for _ in range(self.size):
            next_row = []
            for _ in range(self.size):
                next_row.append(self.weighted_choice(self.WEIGHTS))
            self.board.append(next_row)


class StandardBoggleBoard(BasicBoggleBoard):
    DICE = [
        ['H', 'Z', 'L', 'R', 'N', 'N'],
        ['E', 'E', 'U', 'S', 'N', 'I'],
        ['M', 'U', 'O', 'C', 'I', 'T'],
        ['S', 'T', 'Y', 'T', 'I', 'D'],
        ['L', 'E', 'R', 'T', 'T', 'Y'],
        ['Y', 'E', 'R', 'D', 'L', 'V'],
        ['W', 'O', 'O', 'T', 'T', 'A'],
        ['A', 'N', 'G', 'A', 'E', 'E'],
        ['H', 'U', 'N', 'I', 'M', 'M'],
        ['T', 'O', 'I', 'S', 'E', 'S'],
        ['G', 'H', 'E', 'N', 'E', 'W'],
        ['H', 'E', 'T', 'W', 'V', 'R'],
        ['O', 'O', 'A', 'J', 'B', 'B'],
        ['D', 'I', 'L', 'R', 'E', 'X'],
        ['F', 'A', 'S', 'K', 'F', 'P'],
        ['C', 'A', 'P', 'O', 'H', 'S'],
    ]

    def __init__(self, env, words_filename, min_word_len, board_size):
        super().__init__(env, words_filename, min_word_len, board_size)

    # override
    def gen_board(self):
        self.board = []
        random.shuffle(self.DICE)
        die_iter = iter(self.DICE)
        for _ in range(self.size):
            next_row = []
            for _ in range(self.size):
                next_die = next(die_iter)
                next_row.append(random.choice(next_die))
            self.board.append(next_row)
