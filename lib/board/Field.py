from lib.figures.Pawn import Pawn
from lib.figures.Knight import Knight
from lib.figures.Bishop import Bishop
from lib.figures.Rook import Rook
from lib.figures.Queen import Queen
from lib.figures.King import King
from lib.utils.Constants import Constants


class Field:
    def __init__(self, pos_x, pos_y, symbol=None):
        self.symbol = symbol
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.figure = self.set_figure()
        self.empty = False if self.symbol else True

    def set_empty(self):
        if self.symbol:
            self.empty = False
        else:
            self.empty = True

    def draw_figure(self, screen, row, col):
        x = Constants.POS_OF_BOARD_X + row * 80
        y = Constants.POS_OF_BOARD_Y + col * 80
        screen.blit(self.figure.img, (x, y))

    def possible_moves(self, board):
        moves = self.figure.get_possible_moves(board, self.pos_x, self.pos_y)
        if not moves:
            return []
        else:
            return moves

    def set_figure(self):
        if self.symbol == 'p':
            return Pawn(Constants.WHITE)
        elif self.symbol == 'P':
            return Pawn(Constants.BLACK)
        elif self.symbol == 'w':
            return Rook(Constants.WHITE)
        elif self.symbol == 'W':
            return Rook(Constants.BLACK)
        elif self.symbol == 's':
            return Knight(Constants.WHITE)
        elif self.symbol == 'S':
            return Knight(Constants.BLACK)
        elif self.symbol == 'g':
            return Bishop(Constants.WHITE)
        elif self.symbol == 'G':
            return Bishop(Constants.BLACK)
        elif self.symbol == 'h':
            return Queen(Constants.WHITE)
        elif self.symbol == 'H':
            return Queen(Constants.BLACK)
        elif self.symbol == 'k':
            return King(Constants.WHITE)
        elif self.symbol == 'K':
            return King(Constants.BLACK)



