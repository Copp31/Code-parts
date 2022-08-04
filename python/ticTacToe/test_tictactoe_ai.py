from tictactoe_board import TicTacToeBoard
from tictactoe_ai import TicTacToeAI


def test_TicTacToeAI_play_random():
    the_board = TicTacToeBoard()
    play_random = TicTacToeAI(the_board)
    play_random.reset()
    play_random.run()
    assert len(the_board.choices) == 8
    assert the_board.board.values() != [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def test_TicTacToeAI_play_to_win():
    the_board = TicTacToeBoard()
    the_board.play('X', '1')
    the_board.play('O', '5')
    the_board.play('X', '2')
    the_board.play('O', '4')
    play_to_win = TicTacToeAI(the_board)
    play_to_win.reset()
    play_to_win.run()
    assert the_board.choices == list("7896")


def test_TicTacToeAI_play_to_block():
    the_board = TicTacToeBoard()
    the_board.play('O', '1')
    the_board.play('X', '5')
    the_board.play('O', '2')
    play_to_block = TicTacToeAI(the_board)
    play_to_block.reset()
    play_to_block.run()
    assert the_board.choices == ['7', '8', '9', '4', '6']
    assert the_board.board == {'7': ' ', '8': ' ', '9': ' ', '4': ' ', '5': 'X', '6': ' ', '1': 'O', '2': 'O', '3': 'X'}


def test_TicTacToeGame_erase_remaining_fact_when_win_and_block_simultaneously():
    the_board = TicTacToeBoard()
    the_board.play('X', '9')
    the_board.play('O', '1')
    the_board.play('X', '7')
    the_board.play('O', '8')
    the_board.play('X', '2')
    the_board.play('O', '5')
    the_board.play('X', '3')
    the_board.play('O', '4')
    x_move = TicTacToeAI(the_board)
    x_move.reset()
    x_move.run()
    print(x_move.facts)
    assert list(x_move.facts) == [0]


def test_TicTacToeGame_erase_remaining_fact_when_win_and_block_simultaneously2():
    # O->518273
    the_board = TicTacToeBoard()
    the_board.play('O', '5')
    the_board.play('X', '1')
    the_board.play('O', '8')
    the_board.play('X', '2')
    the_board.play('O', '7')
    # the_board.play('X', '3')
    x_move = TicTacToeAI(the_board)
    x_move.reset()
    x_move.run()
    print(x_move.facts)
    assert list(x_move.facts) == [0]
