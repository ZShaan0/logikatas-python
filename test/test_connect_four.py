from src.connect_four import ConnectFour
import pytest
from unittest.mock import patch

class TestConnectFour:
    def test_play_drops_a_counter(self):
        test_game = ConnectFour()
        with patch("builtins.input", return_value="1"):
            test_game.play()
        assert test_game.game_board == [
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None],
                        ['x', None, None, None, None, None, None]
                    ]
    
    def test_alternates_players(self):
        test_game = ConnectFour()
        with patch("builtins.input", side_effect=['1', '1', '1', '1']):
            test_game.play()
            test_game.play()
            test_game.play()
            test_game.play()

        assert test_game.game_board == [
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None],
                        ['o', None, None, None, None, None, None],
                        ['x', None, None, None, None, None, None],
                        ['o', None, None, None, None, None, None],
                        ['x', None, None, None, None, None, None]
                    ]
    
    def test_get_player_alternates(self, capsys):
        test_game = ConnectFour()
        test_game.get_player()
        captured = capsys.readouterr()
        assert captured.out[:-1] == "It is x's turn"
        
        with patch("builtins.input", side_effect=['1']):
            test_game.play()
        test_game.get_player()
        
        captured = capsys.readouterr()
        assert captured.out[29:-1] == "It is o's turn"

    def test_handles_full_column(self, capsys):
        test_game = ConnectFour()
        with patch("builtins.input", side_effect=['1', '1', '1', '1', '1', '1', '1', '2']):
            test_game.play()
            test_game.play()
            test_game.play()
            test_game.play()
            test_game.play()
            test_game.play()
            test_game.play()

        captured = capsys.readouterr()
        assert captured.out[-50:-30] == "This column is full!"


    def test_handles_invalid_input(self, capsys):
        test_game = ConnectFour()
        with patch("builtins.input", side_effect=['10', 'a', '1']):
            test_game.play()

        captured = capsys.readouterr()
        assert captured.out[29:84] == "Invalid column. Please choose a number between 1 and 7."
        assert captured.out[114:157] == "Invalid input. Choose a column from 1 to 7:"

    def test_finds_winner(self, capsys):
        test_game = ConnectFour()
        with patch("builtins.input", side_effect=['1', '2', '1', '2', '1', '2', '1']):
            test_game.play()
            test_game.play()
            test_game.play()
            test_game.play()
            test_game.play()
            test_game.play()
            test_game.play()
        
        test_game.check_winner()

        captured = capsys.readouterr()
        assert captured.out[-17:-1] == "x is the winner!"


    def test_board_turn_player_reset(self, capsys):
        test_game = ConnectFour()
        with patch("builtins.input", side_effect=['1']):
            test_game.play()
        test_game.reset_game()

        assert test_game.game_board == [
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None]
                    ]

        assert test_game.state == {'turn': 1, 'player': 'x'}

        captured = capsys.readouterr()
        assert captured.out[-25:-1] == "The game has been reset!"