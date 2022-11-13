from lib.utils.Constants import Constants
from copy import copy, deepcopy
from lib.board.Field import Field


class Bot:
    def __init__(self, color):
        self.color = color
        self.available_moves = None
        self.fields = None
        self.orginal_f = None
        self.evaluation = 0

    def set_available_moves(self):
        pass

    def get_move(self, board):
        self.orginal_f = copy(board.fields)
        x = copy(board)
        x.fields[0][0] = Field(0, 0)
        print(id(board.fields[0][0]))
        print(id(x.fields[0][0]))
        min = -999
        move = None
        fig_pos = None
        if not board.check_color == self.color:
            for row in board.fields:
                for field in row:
                    if not field.empty and field.figure.color == self.color:
                        for m in field.possible_moves(board.fields):
                            subboard = self.make_move_simulation(field, m)
                            self.set_evaluation(subboard)
                            king = board.find_king(subboard, field.figure.color)
                            if not king.check_check(subboard):
                                if self.evaluation > min:
                                    min = self.evaluation
                                    fig_pos = (field.pos_x, field.pos_y)
                                    move = m
        else:
            for moves in board.available_moves_on_check:
                fie, mov = moves
                subboard = self.make_move_simulation(fie, mov)
                self.set_evaluation(subboard)
                king = board.find_king(subboard, fie.figure.color)

                if self.evaluation != min:
                    min = self.evaluation
                    fig_pos = (fie.pos_x, fie.pos_y)
                    move = mov
        return fig_pos, move

    def set_evaluation(self, fields):
        evaluation = 0
        for i, row in enumerate(fields):
            for j, field in enumerate(row):
                if not field.empty:
                    symbol = field.symbol
                    color = field.figure.color
                    x, y = i, j
                    if color == Constants.FIG_WHITE:
                        evalll_fig = Constants.EVALUATION_FIG[symbol]
                        e = evalll_fig['value']
                        e_pos = evalll_fig['evalu'][x][y]
                    else:
                        evalll_fig = Constants.EVALUATION_FIG[symbol.lower()]
                        e = evalll_fig['value'] * -1
                        e_pos = [ar[::-1] for ar in evalll_fig['evalu'][::-1]][x][y] * -1
                    evaluation += e + e_pos
        self.evaluation = evaluation

    def make_move_simulation(self, field, move):
        subboard = [[None for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                subboard[i][j] = copy(self.orginal_f[i][j])

        subboard[move[0]][move[1]] = field
        x, y = field.pos_x, field.pos_y
        subboard[x][y] = Field(x, y)
        return subboard


