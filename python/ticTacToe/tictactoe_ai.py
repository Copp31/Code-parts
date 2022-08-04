import random
from experta import *

from tictactoe_board import TicTacToeBoard


class StrategicFact(Fact):
    pass


class PossibleWin(Fact):
    pass


class TicTacToeAI(KnowledgeEngine):
    def __init__(self, board: TicTacToeBoard, player: str = "X"):
        self.player: str = player
        self.board: TicTacToeBoard = board
        super().__init__()

    @Rule()
    def look_at_board(self):
        print("*AI Looking at board*")
        go_random: bool = True
        print(self.board.possible_wins)
        for possible_win in self.board.possible_wins:
            # self.declare(PossibleWin(possible_win))
            if possible_win.count("X") == 2 and possible_win.replace("X", "").isdigit():
                go_random = False
                self.declare(StrategicFact("can-win"))
                print(f'StrategicFact("can-win") declared for {possible_win}')

            elif possible_win.count("O") == 2 and possible_win.replace("O", "").isdigit():
                go_random = False
                self.declare(StrategicFact("need-block"))
                print(f'StrategicFact("need-block") declared for {possible_win}')

            elif "X" in possible_win and possible_win.replace("X", "").isdigit():
                go_random = False
                self.declare(StrategicFact("logic-move"))
                print(f'StrategicFact("logic-move") declared for {possible_win}')

        if go_random:
            self.declare(StrategicFact("can-random"))
            print('StrategicFact("can-random") declared')
        print(self.facts)

    @Rule(AS.fact1 << StrategicFact('can-random'))
    def play_random(self, fact1):
        print("*AI playing randomly*")
        random_move: str = random.choice(self.board.choices)
        for possible_win in self.board.possible_wins:
            if "X" in possible_win and "O" not in possible_win:
                possible_win = possible_win.replace("X", "")
                random_move: str = random.choice(list(possible_win))
                break
        print(f"AI plays {random_move}")
        self.board.play(self.player, str(random_move))
        self.retract(fact1)

    @Rule(AS.fact1 << StrategicFact('logic-move'))
    def play_random_with_logic(self):
        """ aller dans le sens du jeu, completer une ligne.
        Limiter les combinaisons à celles ou l'AI a déja joué et
        que le joueur n'a toujours pas bloqué"""
        print("*AI playing randomly with some logic*")
        logic_move: str = random.choice(self.board.choices)
        for possible_win in self.board.possible_wins:
            if "X" in possible_win and "O" not in possible_win:
                possible_win = possible_win.replace("X", "")
                logic_move: str = random.choice(list(possible_win))
                break

        print(f"AI plays {logic_move}")
        self.board.play(self.player, str(logic_move))
        # self.retract(fact1)
        for f in list(self.facts)[1:]:
            self.retract(f)

    @Rule(AS.f1 << StrategicFact('can-win'))
    def play_to_win(self):
        print("*AI playing to win*")
        for possible_win in self.board.possible_wins:
            if possible_win.count("X") == 2 and possible_win.replace("X", "").isdigit():
                win_move: str = possible_win.replace("X", "")
                print(f"AI plays {win_move}")
                self.board.play(self.player, win_move)
                for f in list(self.facts)[1:]:
                    self.retract(f)
                # self.retract(f1)
                break

    @Rule(AS.f1 << StrategicFact('need-block'))
    def play_to_block(self):
        print("*AI playing to block*")
        for possible_win in self.board.possible_wins:
            if possible_win.count("O") == 2 and possible_win.replace("O", "").isdigit():
                block_move: str = possible_win.replace("O", "")
                print(f"AI plays {block_move}")
                self.board.play(self.player, block_move)
                for f in list(self.facts)[1:]:
                    self.retract(f)

    @Rule(AND(AS.f1 << StrategicFact('can-win'),
              AS.f2 << StrategicFact('need-block'),
              AS.f3 << StrategicFact('logic-move')))
    def play_to_win_not_block(self):
        print("*AI playing to win not to block*")
        for possible_win in self.board.possible_wins:
            if possible_win.count("X") == 2 and possible_win.replace("X", "").isdigit():
                win_move: str = possible_win.replace("X", "")
                print(f"AI plays {win_move}")
                self.board.play(self.player, win_move)
                # self.retract(f1)
                # self.retract(f2)
                for f in list(self.facts)[1:]:
                    self.retract(f)
                break
