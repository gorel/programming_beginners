import base64
import hashlib
import os

MIN_ALIAS_LEN = 3
NUM_SCORES_TO_KEEP = 15
TOP_OVERALL_KEY = "TOP OVERALL"
TOP_ROUND_KEY = "TOP ROUND"
TOP_WORD_KEY = "TOP WORD"


class ScoreRecord(object):
    NUM_FIELDS = 5
    def __init__(self, key_type, alias, game_board_str, score, extra_info=""):
        # TODO: Store these variables in `self` as type `str`
        pass

    def serialize(self):
        # TODO: Come up with a scheme for serializing this data to a file
        pass

    @classmethod
    def from_line(cls, line):
        # TODO: Given a serialized ScoreRecord (a string line), return a new ScoreRecord object
        pass

    @staticmethod
    def serialize_game_board(game_board):
        # TODO: Return a serialized string for the game board (do NOT use newline in your serialization)
        # In other words, given a 2d game board, how might you represent it on one line?
        pass


class HighScores(object):
    def __init__(self, filename):
        self.filename = filename
        self.all_top_scores = self.try_to_read_file()

    def try_to_read_file(self):
        all_top_scores = {TOP_OVERALL_KEY: [], TOP_ROUND_KEY: [], TOP_WORD_KEY: []}
        current_topic = None
        if os.path.exists(self.filename):
            with open(self.filename) as f:
                contents = f.read()
                # TODO: If you're using HighScore encryption, here you'll need to add the following:
                # contents = self.decrypt(contents)
                for line in contents.split("\n"):
                    record = ScoreRecord.from_line(line)
                    if record is not None:
                        all_top_scores[record.key_type].append(record)
        return all_top_scores

    def encrypt(self, s):
        # Encrypts string s using the hash of this file as the key
        # Implementation of a simple Vigenere cipher
        with open(os.path.abspath(__file__)) as f:
            key = hashlib.md5(f.read().encode()).hexdigest()
        encoded_chars = []
        for i in range(len(s)):
            key_c = key[i % len(key)]
            encoded_c = chr(ord(s[i]) + ord(key_c) % 256)
            encoded_chars.append(encoded_c)
        return "".join(encoded_chars)

    def decrypt(self, s):
        # Decrypts string s using the hash of this file as the key
        # Implementation of a simple Vigenere cipher
        with open(os.path.abspath(__file__)) as f:
            key = hashlib.md5(f.read().encode()).hexdigest()
        encoded_chars = []
        for i in range(len(s)):
            key_c = key[i % len(key)]
            encoded_c = chr((ord(s[i]) - ord(key_c)) % 256)
            encoded_chars.append(encoded_c)
        return "".join(encoded_chars)

    def save(self):
        # TODO: Save this HighScores object to file
        # NOTE: Once you get the basic functionality working, call the above encrypt method so people can't
        #       tamper with your HighScores files!
        pass

    def get_alias_for_scores(self):
        prompt = "Please type your alias for the high scores list> "
        user_input = input(prompt)
        while len(user_input) < MIN_ALIAS_LEN:
            print(f"Please supply an alias at least {MIN_ALIAS_LEN} characters long")
            user_input = input(prompt)
        return user_input

    def maybe_insert_new_high_score(self, game, key_type, score, extra_info=""):
        # Score must be strictly positive
        if score <= 0:
            return

        game_board_str = ScoreRecord.serialize_game_board(game.board)
        record_list = self.all_top_scores[key_type]

        # Go up to len(record_list) instead of NUM_SCORES_TO_KEEP in case we don't have that many scores yet
        inserted = False
        for i in range(len(record_list)):
            this_record = record_list[i]
            # Records are stored as str, so cast back to int
            if score > int(this_record.score):
                print(f"That's a new high score for category [{key_type}]")
                alias = self.get_alias_for_scores()
                new_record = ScoreRecord(key_type, alias, game_board_str, score, extra_info)
                # Insert the new record
                record_list.insert(i, new_record)
                inserted = True
                # Immediately break so we don't keep inserting into the record list
                break

        # Edge case: If the list is not full and we haven't inserted yet, do that now
        if len(record_list) < NUM_SCORES_TO_KEEP and not inserted:
            print(f"That's a new high score for category [{key_type}]")
            alias = self.get_alias_for_scores()
            new_record = ScoreRecord(key_type, alias, game_board_str, score, extra_info)
            record_list.append(new_record)
            inserted = True

        # Delete the last record from the list if we have more than NUM_SCORES_TO_KEEP
        if len(record_list) > NUM_SCORES_TO_KEEP:
            record_list.pop()

        # Always save the scores to disk if we modified any record
        if inserted:
            self.save()

    def print_records(self):
        # TODO: Print the high scores
        # Start with overall, then round, then word
        pass

class DummyHighScores(HighScores):
    def __init__(self):
        # Intentionally do nothing
        return

    def maybe_insert_new_high_score(self, game, key_type, score, extra_info=""):
        # Intentionally do nothing
        return

    def __str__(self):
        return ""
