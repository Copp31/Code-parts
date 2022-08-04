from tictactoe_board import TicTacToeBoard


def test_TicTacToeBoard_play():
    the_board = TicTacToeBoard()
    the_board.play("X", "5")
    assert the_board.board["5"] == "X"
    assert the_board.possible_wins[1] == "4X6"
    assert the_board.board == {'7': ' ', '8': ' ', '9': ' ',
                               '4': ' ', '5': 'X', '6': ' ',
                               '1': ' ', '2': ' ', '3': ' '}


def test_TicTacToeBoard_restart():
    the_board = TicTacToeBoard()
    the_board.play("X", "5")
    the_board.restart()
    assert the_board.choices == list("789456123")
    assert the_board.possible_wins == ["789", "456", "123", "741", "852", "963", "753", "159"]
    assert the_board.board == {'7': ' ', '8': ' ', '9': ' ',
                               '4': ' ', '5': ' ', '6': ' ',
                               '1': ' ', '2': ' ', '3': ' '}
