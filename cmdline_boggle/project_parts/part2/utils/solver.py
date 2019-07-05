import copy


class Solver(object):
    def __init__(self, game):
        self.game = game
        self.env = game.env
        self.env.debug_print("Initializing solver...", end='')
        old_len = len(game.dictionary.words)
        self.dictionary = copy.deepcopy(game.dictionary)
        self.prune_dictionary()
        new_len = len(self.dictionary.words)
        self.env.debug_print(f" Dictionary pruned ({old_len} -> {new_len} words)")

    def prune_dictionary(self):
        # TODO: Prune our dictionary so it only has valid words for the current game
        # This is an optimization so the computer can find possible words faster
        # 1. Create a set of all the available letters in the game
        # 2. Create a new list of the "pruned words" that are possible given that letter set
        #   3. Read through the full dictionary (self.dictionary)
        #   4. For each word in the dictionary,
        #       5. if there are letters in the word that AREN'T in this game board, the word is impossible
        #       6. Otherwise, this is a valid word
        #           7. As an added constraint to the solver, add the word in UPPERCASE to the pruned word list
        # 8. Overwrite self.dictionary.words with your pruned word list
        pass
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
        # TODO: Find all possible words in the board by utilizing the find_words helper function
        # 1. Create an empty set of all words possible in this game (let's define this as all_words)
        # 2. iterate over all the possible starting positions in the grid (square 0, 0; square 0, 1; etc)
        #   Let's define the space here as (row, column)
        #   3. Call self.find_words(row, column, all_words, "")
        #       -> this will find all possible words starting at (square row, column) and insert them into all_words
        # 4. Return the set of words
        pass
        all_words = set()
        i = 1
        for row in range(self.game.size):
            for col in range(self.game.size):
                self.env.debug_print(f"[{i} / {self.game.size * self.game.size}] solving...")
                self.find_words(row, col, all_words, "")
                i += 1
        self.env.debug_print(f"Solver found {len(all_words)} words")
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
            self.env.debug_print(f"Short circuit because prefix for {cur_builder} fails")
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
