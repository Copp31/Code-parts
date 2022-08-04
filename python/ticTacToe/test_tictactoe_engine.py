from tictactoe_engine import *
from tictactoe_board import TicTacToeBoard


def test_TicTacToeGame_test():
    theBoard = TicTacToeBoard()
    game = TicTacToeGame(theBoard)
    game.reset()
    game.declare(Test())
    game.run()
    assert game.board.turn == 1
    assert game.board.choices == list("789456123")


def test_TicTacToeGame_check_win():
    the_board = TicTacToeBoard()
    the_board.play('O', '1')
    the_board.play('X', '5')
    the_board.play('O', '9')
    the_board.play('X', '7')
    the_board.play('O', '8')
    the_board.play('X', '3')
    game = TicTacToeGame(the_board)
    game.reset()
    game.declare(Test('test'))
    game.run()
    assert game.winner == 'X'


def test_TicTacToeGame_check_win2():
    theBoard = TicTacToeBoard()
    theBoard.play('X', '2')
    theBoard.play('O', '6')
    theBoard.play('X', '7')
    theBoard.play('O', '5')
    theBoard.play('X', '4')
    theBoard.play('O', '9')
    theBoard.play('X', '1')
    game = TicTacToeGame(theBoard)
    game.reset()
    game.declare(Test('test'))
    game.run()
    assert game.winner == 'X'


def test_TicTacToeGame_tie():
    theBoard = TicTacToeBoard()
    theBoard.play('X', '1')
    theBoard.play('O', '3')
    theBoard.play('X', '7')
    theBoard.play('O', '4')
    theBoard.play('X', '6')
    theBoard.play('O', '5')
    theBoard.play('X', '9')
    theBoard.play('O', '8')
    theBoard.play('X', '2')
    game = TicTacToeGame(theBoard)
    game.reset()
    game.declare(Test("test"))
    game.run()
    print(game.facts)
    theBoard.print()
    print(game.winner)
    assert game.winner == "TIE"


def test_TicTacToeGame_tie_vs_checkwin_on_last_turn():
    pass


def test_TicTacToeGame_O51286437_X_wins_with_7():
    theBoard = TicTacToeBoard()
    theBoard.play('O', '5')
    theBoard.play('X', '1')
    theBoard.play('O', '2')
    theBoard.play('X', '8')
    theBoard.play('O', '6')
    theBoard.play('X', '4')
    theBoard.play('O', '3')
    game = TicTacToeGame(theBoard)
    game.reset()
    game.declare(Test('test-x'))
    game.run()
    assert game.board.board['7'] == "X"
    assert game.winner == 'X'