"""This module uses OOP to create a class for a game of Connect Four
and a game script to play the game using the class functions."""
class ConnectFour:
    """This class contains the functions needed to play a game of Connect Four."""
    def __init__(self):
        """The class initialises a turn counter, turn tracker and game board."""
        self.players = ['x', 'o']
        self.state = {'turn': 1, 'player': self.players[0]}
        self.game_board = [
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None]
                    ]

    def play(self):
        """The play function takes the player's input to insert their token."""
        while True:
            print("Choose a column from 1 to 7:")
            try:
                chosen_column = int(input()) - 1
                if not 0 <= chosen_column <= 6:
                    print("Invalid column. Please choose a number between 1 and 7.")
                    continue
            except ValueError:
                print("Invalid input. Choose a column from 1 to 7:")
                continue

            for row in reversed(self.game_board):
                if row[chosen_column] is None:
                    row[chosen_column] = self.state['player']
                    self.state['turn'] += 1
                    self.state['player'] = self.players[
                        (self.state['turn'] % len(self.players) -1 )]
                    return
            print ('This column is full!')

    def get_board(self):
        """This function returns the board in a visual board format."""
        for row in self.game_board:
            print("| " + " | ".join([' ' if cell is None else cell for cell in row]) + " |")
            print("-" * 29)

    def get_player(self):
        """This functions returns which player's turn it is."""
        print (f"It is {self.state['player']}'s turn")

    def reset_game(self):
        """This function resets the turn count, player turn and game board."""
        self.state = {'turn': 1, 'player': self.players[0]}
        self.game_board = [
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None]
                    ]
        print ("The game has been reset!")

    def check_winner(self):
        """This function checks the game board for 4 consecutive tokens."""
        for row in range(6):
            for column in range(7):
                if self.game_board[row][column] is None:
                    continue
                if (self._check_next(row, column, 1, 0) or
                    self._check_next(row, column, 0, 1) or
                    self._check_next(row, column, 1, 1) or
                    self._check_next(row, column, 1, -1)):
                    print (f"{self.game_board[row][column]} is the winner!")
                    return 1
        return None

    def _check_next(self, row, column, next_row, next_column):
        """This function is used in check_winner to check if the next single token is a match."""
        start_piece = self.game_board[row][column]
        for i in range(1, 4):
            r, c = row + i * next_row, column + i * next_column
            if not (0 <= r < 6 and 0 <= c < 7):
                return False
            if self.game_board[r][c] != start_piece:
                return False
        return True

    def check_tied_game(self):
        """This function checks if the game board is full, i.e. the game result is a tie."""
        tied_game = all(slot is not None for slot in self.game_board[0])
        if tied_game:
            print("It's a tie!")
        return tied_game

def connect_four_script():
    """This script uses the ConnectFour class to play the game smoothly."""
    while True:
        game = ConnectFour()
        while game.check_winner() is None:
            game.get_player()
            game.play()
            game.get_board()

        while True:
            next_game = input("Do you want to play another game? y/n")
            if next_game.lower() == "n":
                print ("Thanks for playing!")
                return
            if next_game.lower() == "y":
                game.reset_game()
                break

            print ("Invalid input, please input 'y' to play another game or 'n' to exit")

# connect_four_script()