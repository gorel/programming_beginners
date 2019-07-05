from utils import boggle_game
# TODO: Import the solver module here
from utils import timed_input


WORDS_FILENAME = "words.txt"
MIN_WORD_LEN = 3
BOARD_SIZE = 4
INPUT_PROMPT = "Next word> "
TIMEOUT_MSG = "Time's up! Hit enter now (your current word won't count, unfortunately)"
TIMEOUT_SECONDS = 60


def print_instructions():
    print("--------------------------------------------------------------------------------")
    print("|                          Welcome to cmdline Boggle!                          |")
    print("|                                                                              |")
    print("| I'll generate a random boggle board for you in a Boggle grid.                |")
    print("| You need to make as many words as possible according to the rules of Boggle. |")
    print("| Although this version isn't multiplayer, it's still fun to play alone.       |")
    print("| See how quickly you can get to the winning score.                            |")
    print("| This might also be good practice to find words faster.                       |")
    print("| You can immediately end a round by typing in all caps: END ROUND             |")
    print("|                                                                              |")
    print("|                           Good luck and have fun!                            |")
    print("--------------------------------------------------------------------------------")
    # Extra newlines at the end to clearly separate the rules
    print("\n")


def game_loop(game):
    print(game)
    timer = timed_input.TimedInput(INPUT_PROMPT, TIMEOUT_SECONDS, TIMEOUT_MSG)
    timer.start()
    print("\nLet's see how you did...")
    round_score = game.score_words(timer.answers)
    # TODO: If you're implementing a solver, it would be added here
    # 1. Ask the user if they'd like to see a solution for words they missed
    # 2. Probably also ask if there's a minimum word length of missed words
    # 3. Create a new board solver object
    # 4. Call the .solve() method of your board solver
    # 5. Sort the missing words by their length
    # 6. Print out the missing words on each line
    return round_score


def play_full_game():
    # TODO Ask the user if they want to play a BasicBoggleBoard, WeightedBoggleBoard, or StandardBoggleBoard
    #   Change the game type based on their response
    game = boggle_game.BasicBoggleBoard(WORDS_FILENAME, MIN_WORD_LEN, BOARD_SIZE)
    winning_score = int(input("What should be the winning score? "))
    current_score = 0

    round_number = 0
    while current_score < winning_score:
        round_number += 1
        print(f"\nNow starting round {round_number} [{current_score} / {winning_score} points]")
        input("Press enter to start the round...")
        current_score += game_loop(game)
        # Reset the board
        game.gen_board()

    rounds_plural = "round"
    if round_number != 1:
        rounds_plural = "rounds"
    print(f"\nFinished! You earned {current_score} points in {round_number} {rounds_plural}.")


if __name__ == "__main__":
    print_instructions()
    play_full_game()
