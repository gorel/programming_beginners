from utils import cmdline_parser
# TODO: Import the scoring module
from utils import solver
from utils import timed_input


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


# TODO: This function should also take a high_scores object
def game_loop(game):
    print(game)
    timer = timed_input.TimedInput(INPUT_PROMPT, TIMEOUT_SECONDS, TIMEOUT_MSG)
    timer.start()
    print("\nLet's see how you did...")
    # TODO: The score_words function also takes a high_scores object now
    round_score = game.score_words(timer.answers)
    # TODO: Check for new best round score
    # Look in the methods defined in scoring to maybe insert a new top round score

    if game.env.should_show_solver():
        board_solver = solver.Solver(game)
        all_words = board_solver.solve()
        missing_words = sorted(all_words - set(timer.answers), key=lambda word: len(word))
        print("Here are the words you missed:")
        for word in missing_words:
            print(f"  {word} ({game.score_word(word)} points)")
    return round_score


def play_full_game(env):
    game = env.get_boggle_game()
    # TODO: Get a high scores object from the cmdline parser
    winning_score = env.get_winning_points_threshold()
    current_score = 0

    round_number = 0
    while current_score < winning_score:
        round_number += 1
        print(f"\nNow starting round {round_number} [{current_score} / {winning_score} points]")
        input("Press enter to start the round...")
        # TODO: The game_loop function also takes a high_scores object now
        current_score += game_loop(game)
        # Reset the board
        game.gen_board()
    # TODO: Check for new best overall score
    # Look in the methods defined in scoring to maybe insert a new top overall score

    rounds_plural = "round"
    if round_number != 1:
        rounds_plural = "rounds"
    print(f"\nFinished! You earned {current_score} points in {round_number} {rounds_plural}.")


if __name__ == "__main__":
    environment = cmdline_parser.CmdlineParser()

    # TODO: If the user only wanted to print highscores, do that
    # Otherwise, we play the game like normal (previous functionality)
    print_instructions()
    if not environment.should_only_print_rules():
        play_full_game(environment)
