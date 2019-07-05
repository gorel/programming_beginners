# Features to add:
# Encryption of high scores file

from utils import boggle_game
from utils import timed_input


# TODO: Set this to your dictionary words filename
WORDS_FILENAME = "TODO: Put your words filename here"
MIN_WORD_LEN = 3
BOARD_SIZE = 4
INPUT_PROMPT = "Next word> "
TIMEOUT_MSG = "Time's up! Hit enter now (your current word won't count, unfortunately)"
TIMEOUT_SECONDS = 60


def print_instructions():
    # TODO: Tell the user how to play
    pass


def game_loop(game):
    # TODO: Create the main logic for one iteration of the game loop
    # 1. print the game board
    #   HINT: Look at the methods defined in the BoggleGame object
    # 2. create a TimedInput object
    #   HINT: How do we construct objects? Look at the TimedInput class
    # 3. start the timer
    #   HINT: Look at the methods defined for TimedInput
    # 4. calculate the round score
    #   HINT: Look at the methods defined in the BoggleGame object
    # 5. return the round score
    # BONUS: Add some other prints to make the game feel more interactive
    pass


def play_full_game():
    # TODO: Play a full game of Boggle
    # 1. Create a boggle game (BasicBoggleBoard)
    # 2. Get input from the user for what the winning score should be
    # 3. While the user's current score is less than the winning score, do the following:
    #   4. Print what round number is starting
    #   5. Play another round of the game (call the game_loop function)
    # 6. Tell the user how many points they earned at the end of the game
    # BONUS: Make the user press enter befre a round starts
    # BONUS: How would you output singular "round" instead of "rounds" if the user beat the game in 1 round?
    pass

if __name__ == "__main__":
    # TODO: Write the main functionality of the program
    # 1. print the game instructions
    # 2. play a game of boggle
    pass
