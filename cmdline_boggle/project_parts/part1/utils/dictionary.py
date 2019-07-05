class Dictionary(object):
    def __init__(self, words_file, min_len=None, max_len=None):
        self.words_file = words_file
        self.min_len = min_len
        self.max_len = max_len
        self.words = self.read_words_file()

    def read_words_file(self):
        # TODO: Read self.words_file contents
        # 1. Create a list of all words read
        # 2. Open the file for reading and iterate line by line
        # 3. If the word is ONLY alphabetical characters and the length is okay, add it to our words list
        #   HINT: use the length_okay method defined below
        # 4. Return the list of all words
        pass

    def length_okay(self, word):
        # TODO: Determine if the word length is acceptable given the dictionary rules
        # Check that min_len <= len(word) <= max_len
        # NOTE: You may have to check that min_len/max_len were properly set first...
        pass

    def word_exists(self, word):
        # Binary search for word
        l = 0
        r = len(self.words) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if self.words[mid] == word:
                return True
            elif self.words[mid] < word:
                l = mid + 1
            else:
                r = mid - 1
        return False
