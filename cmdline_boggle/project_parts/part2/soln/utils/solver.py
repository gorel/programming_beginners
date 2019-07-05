import copy


class Solver(object):
    def __init__(self, game):
        self.game = game
        old_len = len(game.dictionary.words)
        self.dictionary = copy.deepcopy(game.dictionary)
        self.prune_dictionary()
        new_len = len(self.dictionary.words)

    def prune_dictionary(self):
        available_letters = set()

        for row in range(self.game.size):
            for col in range(self.game.size):
                available_letters.add(self.game.board[row][col].lower())

        pruned_words = []
        for word in self.dictionary.words:
            if set(word) - available_letters == set():
                # Minor optimzation: due to mismatch of lower/upper letters,
                # we can avoid a conversion later by adding the UPPERCASE word here
                pruned_words.append(word.upper())
        self.dictionary.words = pruned_words

    def solve(self):
        all_words = set()
        i = 1
        for row in range(self.game.size):
            for col in range(self.game.size):
                self.find_words(row, col, all_words, "")
                i += 1
        return set(word.lower() for word in all_words)

    def find_words(self, row, col, all_words, cur_builder):
        # Bounds checking
        if row < 0 or col < 0 or row >= self.game.size or col >= self.game.size:
            return

        # Backtrack checking
        this_char = self.game.board[row][col]
        if this_char is None:
            return

        # Build and continue
        cur_builder += this_char

        # Maybe add a new word
        if self.dictionary.word_exists(cur_builder):
            all_words.add(cur_builder)

        # If this prefix won't yield anything, end early
        if not self.dictionary.prefix_exists(cur_builder):
            return

        # Try each direction
        dirs = [-1, 0, 1]
        for row_dir in dirs:
            for col_dir in dirs:
                new_row = row + row_dir
                new_col = col + col_dir

                # Temporarily set this space as None so we won't backtrack on it
                self.game.board[row][col] = None
                self.find_words(new_row, new_col, all_words, cur_builder)
                # Reset this space
                self.game.board[row][col] = this_char
