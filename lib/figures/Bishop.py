from lib.utils.Constants import Constants
from lib.utils.Images import Images


class Bishop:
    def __init__(self, color):
        self.color = color
        self.img = self.set_image()

    def get_possible_moves(self, board, pos_x, pos_y):
        moves = []
        # check south-east
        for i in range(1, 8):
            if pos_x + i <= 7 and pos_y + i <= 7:
                if board[pos_x + i][pos_y + i].empty:
                    moves.append((pos_x + i, pos_y + i))
                elif board[pos_x + i][pos_y + i].figure.color != self.color:
                    moves.append((pos_x + i, pos_y + i))
                    break
                else:
                    break
            else:
                break
        # check south-west
        for i in range(1, 8):
            if pos_x + i <= 7 and pos_y - i >= 0:
                if board[pos_x + i][pos_y - i].empty:
                    moves.append((pos_x + i, pos_y - i))
                elif board[pos_x + i][pos_y - i].figure.color != self.color:
                    moves.append((pos_x + i, pos_y - i))
                    break
                else:
                    break
            else:
                break
        # check north-west
        for i in range(1, 8):
            if pos_x - i >= 0 and pos_y - i >= 0:
                if board[pos_x - i][pos_y - i].empty:
                    moves.append((pos_x - i, pos_y - i))
                elif board[pos_x - i][pos_y - i].figure.color != self.color:
                    moves.append((pos_x - i, pos_y - i))
                    break
                else:
                    break
            else:
                break
        # check north-east
        for i in range(1, 8):
            if pos_x - i >= 0 and pos_y + i <= 7:
                if board[pos_x - i][pos_y + i].empty:
                    moves.append((pos_x - i, pos_y + i))
                elif board[pos_x - i][pos_y + i].figure.color != self.color:
                    moves.append((pos_x - i, pos_y + i))
                    break
                else:
                    break
            else:
                break
        return moves

    def set_image(self):
        if self.color == Constants.FIG_WHITE:
            return Images.W_BISHOP
        else:
            return Images.B_BISHOP
