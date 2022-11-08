from lib.utils.Constants import Constants
from lib.utils.Images import Images


class Pawn:
    def __init__(self, color):
        self.color = color
        self.img = self.set_image()

    def get_possible_moves(self, board, pos_x, pos_y):
        moves = []
        if self.color == Constants.WHITE:
            if pos_y <= 6 and board[pos_x][pos_y + 1].empty:
                moves.append((pos_x, pos_y + 1))

            if pos_y == 1 and board[pos_x][pos_y + 2].empty and board[pos_x][pos_y + 1].empty:
                moves.append((pos_x, pos_y + 2))

            if pos_y <= 6 and pos_x <= 6 and not board[pos_x + 1][pos_y + 1].empty \
                    and board[pos_x + 1][pos_y + 1].figure.color == Constants.BLACK:
                moves.append((pos_x + 1, pos_y + 1))

            if pos_y <= 6 and pos_x >= 1 and not board[pos_x - 1][pos_y + 1].empty \
                    and board[pos_x - 1][pos_y + 1].figure.color == Constants.BLACK:
                moves.append((pos_x - 1, pos_y + 1))

        if self.color == Constants.BLACK:
            if pos_y >= 1 and board[pos_x][pos_y - 1].empty:
                moves.append((pos_x, pos_y - 1))

            if pos_y == 6 and board[pos_x][pos_y - 2].empty and board[pos_x][pos_y - 1].empty:
                moves.append((pos_x, pos_y - 2))

            if pos_y >= 1 and pos_x <= 6 and not board[pos_x + 1][pos_y - 1].empty \
                    and board[pos_x + 1][pos_y - 1].figure.color == Constants.WHITE:
                moves.append((pos_x + 1, pos_y - 1))

            if pos_y >= 1 and pos_x >= 1 and not board[pos_x - 1][pos_y - 1].empty \
                    and board[pos_x - 1][pos_y - 1].figure.color == Constants.WHITE:
                moves.append((pos_x - 1, pos_y - 1))

        return moves

    def set_image(self):
        if self.color == Constants.WHITE:
            return Images.W_PAWN
        else:
            return Images.B_PAWN
