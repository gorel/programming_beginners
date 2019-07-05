# Features to add:
# Encryption of high scores file

from utils import cmdline_parser
from utils import scoring
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


def game_loop(game, high_scores):
    print(game)
    timer = timed_input.TimedInput(INPUT_PROMPT, TIMEOUT_SECONDS, TIMEOUT_MSG)
    timer.start()
    print("\nLet's see how you did...")
    round_score = game.score_words(timer.answers, high_scores)
    high_scores.maybe_insert_new_high_score(game, scoring.TOP_ROUND_KEY, round_score)

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
    high_scores = env.get_high_scores_object()
    winning_score = env.get_winning_points_threshold()
    current_score = 0

    round_number = 0
    while current_score < winning_score:
        round_number += 1
        print(f"\nNow starting round {round_number} [{current_score} / {winning_score} points]")
        input("Press enter to start the round...")
        current_score += game_loop(game, high_scores)
        # Reset the board
        game.gen_board()
    high_scores.maybe_insert_new_high_score(game, scoring.TOP_OVERALL_KEY, current_score)

    rounds_plural = "round"
    if round_number != 1:
        rounds_plural = "rounds"
    print(f"\nFinished! You earned {current_score} points in {round_number} {rounds_plural}.")


if __name__ == "__main__":
    environment = cmdline_parser.CmdlineParser()

    if environment.should_only_print_highscores():
        environment.get_high_scores_object().print_records()
    else:
        print_instructions()
        if not environment.should_only_print_rules():
            play_full_game(environment)
