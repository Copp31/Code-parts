from typing import Optional

import random
from experta import *
from experta.fact import *

from tictactoe_board import TicTacToeBoard
from tictactoe_ai import TicTacToeAI


class GamesState(Fact):
    count = Field(int, default=0)
    state = Field(str, default="")


class Action(Fact):
    # exemples:
    # Action('get-computer-move')
    # Action('get-human-move')
    # Action('determine-results')
    # Action('determine-play-again')
    pass


class Test(Fact):
    """ Déclaré dans l'execution d'un test. sert essentiellement à éviter les lignes:
        random.choice(['O', 'X']) et n: str = input("O to play: ") """
    pass


class TicTacToeGame(KnowledgeEngine):
    def __init__(self, board: TicTacToeBoard, first_to_play: Optional[str] = None):
        self.first_to_play = first_to_play
        self.board: TicTacToeBoard = board
        self.winner: str = ''
        super().__init__()

    @Rule(Test('test'))
    def startup_test(self):
        print("Lets TEST Tic Tac Toe!!")
        self.declare(GamesState(count=self.board.turn, state="test"))
        self.declare(Action('checkwin'))

    @Rule(Test("test-x"))
    def startup_test_with_x_to_play(self):
        print("Lets TEST Tic Tac Toe -> X to play")
        self.declare(GamesState(count=self.board.turn, state="get-X-move"))
        self.declare(Action('get-X-move'))

    @Rule(NOT(Test()))
    def startup(self):
        print("Lets play Tic Tac Toe!!")
        self.declare(GamesState(count=self.board.turn))
        if not self.first_to_play:
            self.first_to_play = random.choice(['O', 'X'])
        self.declare(Action(f'get-{self.first_to_play}-move'))

    @Rule(AS.action << Action('get-O-move'),
          AS.gs << GamesState(count=MATCH.count))
    def o_move(self, action: Fact, gs: Fact):
        self.board.print()
        n: str = input("O to play: ")
        try:
            if self.board.board[n] == " ":
                self.board.play("O", str(n))
                self.retract(action)
                self.modify(gs, count=self.board.turn, state='get-X-move')
                self.declare(Action('checkwin'))
            else:
                print("Already taken, choose again")
                self.retract(action)
                self.declare(Action('get-O-move'))
        except KeyError:
            print("invalid choice!")
            self.retract(action)
            self.declare(Action('get-O-move'))

    @Rule(AS.action << Action('get-X-move'),
          AS.gs << GamesState(count=MATCH.cc))
    def x_move(self, action: Fact, gs: Fact):
        ia_move = TicTacToeAI(self.board)
        ia_move.reset()
        ia_move.run()
        self.retract(action)
        self.declare(Action('checkwin'))
        self.modify(gs, count=self.board.turn, state='get-O-move')

    @Rule(AS.action << Action('checkwin'),
          AS.gs << GamesState(count=MATCH.count, state=MATCH.turn))
    def check_win(self, action: Action):
        self.retract(action)
        win = False
        for possible_win in self.board.possible_wins:
            won: bool = all([possible_win[0] == possible_win[1] == possible_win[2]])
            if won:
                print(self.facts)
                self.winner: str = possible_win[0]
                self.board.print()
                win = True
                print(f"\n{self.winner} WON")
                break
        if not win:
            self.declare(Action("checktie"))

    @Rule(AS.action << Action('checktie'),
          AS.gs << GamesState(count=MATCH.count, state=MATCH.turn))
    def check_tie(self, action: Action, count: int):
        self.retract(action)
        if count < 10:
            self.declare(Action("change"))
        else:
            self.winner: str = "TIE"
            print(self.winner)

    @Rule(AS.action << Action('change'),
          AS.gs << GamesState(state=MATCH.turn),
          NOT(Test()))
    def next_to_play(self, action: Action, turn: int):
        self.retract(action)
        self.declare(Action(turn))
