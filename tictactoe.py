from data import *


class TicTacToe:
    def __init__(self):
        self.game = TICTACTOE
        self.mapped_spaces = ""
        self.mapped_value = ""
        self.mapped_key = None
        self.current_player = 1

    def available_spaces(self):
        available = []
        mapped_spaces = ""

        print(self.game)

        for index, char in enumerate(self.game):
            if char == ".":
                available.append(index)

        for key, value in SPACE_MAP.items():
            if key in available:
                mapped_spaces += value
                mapped_spaces += " "

        self.mapped_spaces = mapped_spaces

    def make_move(self):
        mapped_value = input(f"Choose a space from {self.mapped_spaces.replace(' ', ', ')[:-2]}:\n").upper()
        while mapped_value not in self.mapped_spaces.split():
            mapped_value = input(f"Invalid command. Choose a space from: {self.mapped_spaces}")

        for key, value in SPACE_MAP.items():
            if mapped_value == SPACE_MAP[key]:
                self.mapped_key = key

    def place_symbol(self):
        if self.current_player == 1:
            self.game = self.game[:self.mapped_key - 1] + " X" + self.game[self.mapped_key + 1:]
            self.current_player = 2
        elif self.current_player == 2:
            self.game = self.game[:self.mapped_key - 1] + " 0" + self.game[self.mapped_key + 1:]
            self.current_player = 1

    def evaluate_winner(self):
        round_result = {}
        for key, value in WIN_CONDITIONS.items():
            symbols = []
            for i in value:
                current_symbol = self.game[i]
                symbols.append(current_symbol)
            round_result[key] = symbols
        return round_result
