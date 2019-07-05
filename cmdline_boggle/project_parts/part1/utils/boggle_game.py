import random
import string

from utils import dictionary


MAX_WORD_LEN = 16


class BasicBoggleBoard(object):
    def __init__(self, words_filename, min_word_len, board_size):
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

    def score_words(self, words):
        # TODO: Find the sum total score of the given words
        # 1. Start a running total of words
        # 2. Iterate through the list of words
        #   HINT: You'll want some kind of loop
        # 3. If the word is in the dictionary AND is possible on the board:
        #   4. Add the word's score to the total
        # 5. Return the total number of points scored
        # BONUS: Tell the user how many points each word is worth
        pass

    def score_word(self, word):
        # TODO: Find the score for a single word
        # Given a word, return how many points it's worth
        #   HINT: This is similar to our code for BMI, isn't it...
        # less than 3-letter words: 0 points
        # 3-letter words: 1 point
        # 4-letter words: 1 points
        # 5-letter words: 2 points
        # 6-letter words: 3 points
        # 7-letter words: 5 points
        # 8+ letter words: 11 points
        pass

    def __str__(self):
        # TODO: return a string representation of a boggle board
        # This is a "magic method"
        #   HINT: Write a boggle board on paper and imagine how you'd translate that to code
        pass

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
        # TODO: Generate a boggle board
        # Look at BasicBoggleBoard for a general sense of what to do
        # Instead of calling random.choice, you should use the weighted_choice method defined above
        pass


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
        # TODO: Generate a boggle board where you have individual dice (like the normal game)
        # 1. Shuffle the order of the dice (this simulates shaking the Boggle box)
        #   HINT: look at the functions available in the random module
        # 2. Get an iterator of the dice
        #   HINT: Read this site https://www.programiz.com/python-programming/methods/built-in/iter
        # 3. For each space, get the next die, get a random character on that die, then continue
        #   HINT: Given a list of items, how do you select a random one? Look at the other gen_board methods
        pass
