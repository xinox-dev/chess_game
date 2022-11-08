from lib.utils.Constants import Constants
from lib.board.Field import Field
from copy import copy

class Board:
    def __init__(self, color):
        self.fields = self.set_fields()
        self.pos_board_x = 100
        self.pos_board_y = 100
        self.white_on_top = False if color == Constants.WHITE else True
        self.selected_figure = None
        self.check_color = None
        self.available_moves_on_check = []

    @staticmethod
    def set_fields():
        board = [[] for _ in range(8)]
        for pos_x, row in enumerate(Constants.BOARD_SETUP):
            for pos_y, symbol in enumerate(row):
                if symbol != '':
                    field = Field(pos_x, pos_y, symbol)
                else:
                    field = Field(pos_x, pos_y)

                board[pos_x].append(field)
        return board

    def draw_fields(self, screen):
        if self.white_on_top:
            course = 1
        else:
            course = -1

        for i, row in enumerate(self.fields[::course]):
            for j, field in enumerate(row[::course]):
                if not field.empty:
                    field.draw_figure(screen, i, j)

    def select_figure(self, color, pos_x: int, pos_y: int):

            if self.white_on_top:
                field: Field = self.fields[pos_x][pos_y]
            else:
                field: Field = self.fields[7 - pos_x][7 - pos_y]

            if field.empty or field.figure.color != color:
                self.selected_figure = None
            else:
                if not self.check_color:
                    self.selected_figure = field
                else:
                    select_figure: None = None
                    for available_move in self.available_moves_on_check:
                        if available_move[0] == field:
                            select_figure = field
                            break
                    if not select_figure:
                        self.selected_figure = None
                    else:
                        self.selected_figure = select_figure

    def check_move(self, pos_x, pos_y):
        if not self.white_on_top:
            pos_x = 7 - pos_x
            pos_y = 7 - pos_y
        if self.selected_figure and (pos_x, pos_y) in self.selected_figure.possible_moves(self.fields):
            return True
        else:
            return False

    def move(self, target_x, target_y):
        if not self.white_on_top:
            target_x = 7 - target_x
            target_y = 7 - target_y
        old_x: int = self.selected_figure.pos_x
        old_y: int = self.selected_figure.pos_y
        clear_field = Field(old_x, old_y)

        # move figure to new position
        self.selected_figure.pos_x = target_x
        self.selected_figure.pos_y = target_y
        self.fields[target_x][target_y] = self.selected_figure

        # clear old figure position
        self.fields[old_x][old_y] = clear_field

        # clear selected figure
        self.selected_figure = None

        # clear check status
        self.check_color = None

    def find_king(self, color):
        for row in self.fields:
            for field in row:
                if field.symbol == 'k' and color == Constants.WHITE:
                    return field
                if field.symbol == 'K' and color == Constants.BLACK:
                    return field

    def set_available_moves_on_check(self):
        available_moves_on_check = []
        for row in self.fields:
            for field in row:
                if not field.empty and field.figure.color == self.check_color:
                    if field.symbol == 'k' or field.symbol == 'K':
                        moves = field.possible_moves(self.fields)
                        for m in moves:
                            available_moves_on_check.append((field, m))
                    else:
                        moves = field.possible_moves(self.fields)
                        for move in moves:
                            subboard = [[None for _ in range(8)] for _ in range(8)]
                            for i in range(8):
                                for j in range(8):
                                    subboard[i][j] = copy(self.fields[i][j])

                            subboard[move[0]][move[1]] = field
                            x, y = field.pos_x, field.pos_y
                            subboard[x][y] = Field(x, y)

                            # find king
                            for subrow in subboard:
                                for subfield in subrow:
                                    if subfield.symbol == 'k' and subfield.figure.color == self.check_color:
                                        king = subfield
                                    if subfield.symbol == 'K' and subfield.figure.color == self.check_color:
                                        king = subfield

                            if not king.check_check(subboard):
                                available_moves_on_check.append((field, move))

        self.available_moves_on_check = available_moves_on_check
