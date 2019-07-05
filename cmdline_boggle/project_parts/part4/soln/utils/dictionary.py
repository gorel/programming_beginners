class Dictionary(object):
    def __init__(self, words_file, min_len=None, max_len=None):
        self.words_file = words_file
        self.min_len = min_len
        self.max_len = max_len
        self.words = self.read_words_file()

    def read_words_file(self):
        all_words = []
        with open(self.words_file) as f:
            for line in f:
                word = line.strip().lower()
                if word.isalpha() and self.length_okay(word):
                    all_words.append(word)
        return all_words

    def length_okay(self, word):
        if self.min_len is not None and len(word) < self.min_len:
            return False
        if self.max_len is not None and len(word) > self.max_len:
            return False
        return True

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

    def prefix_exists(self, prefix):
        # Binary search for prefix
        l = 0
        r = len(self.words) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if self.words[mid].startswith(prefix):
                return True
            elif self.words[mid] < prefix:
                l = mid + 1
            else:
                r = mid - 1
        return False
