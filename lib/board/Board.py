from lib.utils.Constants import Constants
from lib.board.Field import Field


class Board:
    def __init__(self, color):
        self.fields = self.set_fields()
        self.pos_board_x = 100
        self.pos_board_y = 100
        self.white_on_top = False if color == Constants.WHITE else True
        self.selected_figure = None

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
            self.selected_figure = field

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

        #
