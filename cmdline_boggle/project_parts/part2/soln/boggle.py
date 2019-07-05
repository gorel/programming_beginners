from utils import boggle_game
from utils import solver
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

    show_solver = input("Would you like to see the words you missed [y/n]? ")
    if show_solver[0].lower() == "y":
        board_solver = solver.Solver(game)
        all_words = board_solver.solve()
        missing_words = sorted(all_words - set(timer.answers), key=lambda word: len(word))
        print("Here are the words you missed:")
        for word in missing_words:
            print(f"  {word} ({game.score_word(word)} points)")
    return round_score


def play_full_game():
    print("What type of boggle board would you like to use (recommend: 3)")
    board_type = input("1. BasicBoggleBoard, 2. WeightedBoggleBoard, 3. StandardBoggleBoard: ")
    if board_type == "1":
        game = boggle_game.BasicBoggleBoard(WORDS_FILENAME, MIN_WORD_LEN, BOARD_SIZE)
    elif board_type == "2":
        game = boggle_game.WeightedBoggleBoard(WORDS_FILENAME, MIN_WORD_LEN, BOARD_SIZE)
    else:
        game = boggle_game.StandardBoggleBoard(WORDS_FILENAME, MIN_WORD_LEN, BOARD_SIZE)
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
