# ---------------------------------------------- Import Statements --------------------------------------------------- #
from tictactoe import TicTacToe


# ---------------------------------------------- Function Definition ------------------------------------------------- #
def yesno_check(input_decision):
    while input_decision not in ["y", "n"]:
        input_decision = input("Invalid input. Type 'y' or 'n'.").lower()


# ----------------------------------------------- Class Instantiation ------------------------------------------------ #
tictactoe = TicTacToe()


# ---------------------------------------------------- Game Logic ---------------------------------------------------- #
start_game = False

start_program = input("Do you want to launch the Tic Tac Toe? (Type 'y' or 'n')\n").lower()
yesno_check(start_program)

if start_program == "y":
    start_game = True

while start_game:
    tictactoe.available_spaces()
    tictactoe.make_move()
    tictactoe.place_symbol()
    evaluation = tictactoe.evaluate_winner()

    for key, value in evaluation.items():
        if "." not in value:
            if "X" in value:
                print("Player 1 won")
                print(tictactoe.game)
                again = input("Do you want to play again?\n")
                yesno_check(again)
                start_game = False
            else:
                print("Player 2 won")
                print(tictactoe.game)
                again = input("Do you want to play again?\n")
                yesno_check(again)
                start_game = False
        else:
            continue

print("Goodbye!")
