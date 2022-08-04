class TicTacToeBoard:
    def __init__(self):
        self.choices: list[str] = list("789456123")
        self.turn = 10-len(self.choices)
        self.possible_wins: list[str] = ["789", "456", "123",
                                         "741", "852", "963",
                                         "753", "159"]
        self.board: dict = {'7': ' ', '8': ' ', '9': ' ',
                            '4': ' ', '5': ' ', '6': ' ',
                            '1': ' ', '2': ' ', '3': ' '}

    def play(self, player: str, spot: str):
        self.choices.remove(spot)
        self.turn = 10 - len(self.choices)
        self.board[spot] = player

        wins: list = []
        for win in self.possible_wins:
            wins.append(win.replace(spot, player))
        self.possible_wins: list[str] = wins

    def restart(self):
        self.__init__()

    def print(self):
        print(self.board['7'] + ' | ' + self.board['8'] +
              ' | ' + self.board['9'])
        print('--+---+--')
        print(self.board['4'] + ' | ' + self.board['5'] +
              ' | ' + self.board['6'])
        print('--+---+--')
        print(self.board['1'] + ' | ' + self.board['2'] +
              ' | ' + self.board['3'])
