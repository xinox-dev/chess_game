from lib.utils.Constants import Constants
from lib.utils.Images import Images
from copy import copy


class King:
    def __init__(self, color):
        self.color = color
        self.img = self.set_image()
        self.first_move = False

    def get_possible_moves(self, board, pos_x, pos_y):
        moves = []
        potential_move = [(pos_x, pos_y - 1), (pos_x + 1, pos_y - 1), (pos_x + 1, pos_y), (pos_x + 1, pos_y + 1),
                          (pos_x, pos_y + 1), (pos_x - 1, pos_y + 1),
                          (pos_x - 1, pos_y), (pos_x - 1, pos_y - 1)]

        # check potential move
        for possible_move in potential_move:
            x, y = possible_move
            if 0 <= x <= 7 and 0 <= y <= 7:
                # if it is my friend, skip
                if not board[x][y].empty and board[x][y].figure.color == self.color:
                    continue

                # create copy of board
                subboard = [[None for _ in range(8)] for _ in range(8)]
                for i in range(8):
                    for j in range(8):
                        subboard[i][j] = copy(board[i][j])

                # simulation when king take this field
                subboard[x][y] = board[pos_x][pos_y]
                subboard[pos_x][pos_y].symbol = None
                subboard[pos_x][pos_y].set_empty()
                dangerous_zone = []
                for i, row in enumerate(subboard):
                    for j, field in enumerate(row):
                        if field.empty or field.figure.color == self.color:
                            continue

                        # king does not touch order king
                        if field.symbol == 'k' or field.symbol == 'K':
                            dangerous_zone += [(field.pos_x, field.pos_y - 1), (field.pos_x + 1, field.pos_y - 1),
                                               (field.pos_x + 1, field.pos_y),(field.pos_x + 1, field.pos_y + 1),
                                               (field.pos_x, field.pos_y + 1), (field.pos_x - 1, field.pos_y + 1),
                                               (field.pos_x - 1, field.pos_y), (field.pos_x - 1, field.pos_y - 1)]
                            continue

                        dangerous_zone += field.possible_moves(subboard)

                if possible_move in dangerous_zone:
                    continue

                moves.append(possible_move)

        # check possible castle (rotation with rook)
        if not self.first_move:
            if (pos_x, pos_y) == (3, 0):
                # white short castle
                if not board[0][0].empty and board[0][0].symbol == 'w' and board[1][0].empty and board[2][0].empty:
                    moves.append((0, 0))
                # white long castle
                if not board[7][0].empty and board[7][0].symbol == 'w' and board[6][0].empty \
                        and board[5][0].empty and board[4][0].empty:
                    moves.append((7, 0))

            if (pos_x, pos_y) == (3, 7):
                # black short castle
                if not board[0][7].empty and board[0][7].symbol == 'W' and board[1][7].empty and board[2][7].empty:
                    moves.append((0, 7))
                # black long castle
                if not board[7][7].empty and board[7][7].symbol == 'W' and board[6][7].empty \
                        and board[5][7].empty and board[4][7].empty:
                    moves.append((7, 7))

        return moves

    def check(self, board, pos_x, pos_y):
        dangerous_zone = []
        for i,row in enumerate(board):
            for j, field in enumerate(row):
                if not field.empty:
                    if field.figure.color == self.color or field.symbol == 'k' or field.symbol == 'K':
                        continue
                    dangerous_zone += field.possible_moves(board)

        if (pos_x, pos_y) in dangerous_zone:
            return True
        else:
            return False

    def check_pat(self, board, pos_x, pos_y):
        if not self.get_possible_moves(board, pos_x, pos_y):
            is_pat = True
            for i, row in enumerate(board):
                for j, field in enumerate(row):
                    if not field.empty and field.figure.color == self.color:
                        if field.possible_moves(board):
                            is_pat = False

            return is_pat
        else:
            return False

    def set_image(self):
        if self.color == Constants.FIG_WHITE:
            return Images.W_KING
        else:
            return Images.B_KING
