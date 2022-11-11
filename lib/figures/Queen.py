from lib.utils.Constants import Constants
from lib.utils.Images import Images


class Queen:
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

        # check moves to upper
        for i in range(pos_x - 1, -1, -1):
            if board[i][pos_y].empty:
                moves.append((i, pos_y))
            elif board[i][pos_y].figure.color != self.color:
                moves.append((i, pos_y))
                break
            else:
                break
            # check moves to bottom
        for i in range(pos_x + 1, 8):
            if board[i][pos_y].empty:
                moves.append((i, pos_y))
            elif board[i][pos_y].figure.color != self.color:
                moves.append((i, pos_y))
                break
            else:
                break
            # check moves to left
        for i in range(pos_y - 1, -1, -1):
            if board[pos_x][i].empty:
                moves.append((pos_x, i))
            elif board[pos_x][i].figure.color != self.color:
                moves.append((pos_x, i))
                break
            else:
                break
            # check moves to right
        for i in range(pos_y + 1, 8):
            if board[pos_x][i].empty:
                moves.append((pos_x, i))
            elif board[pos_x][i].figure.color != self.color:
                moves.append((pos_x, i))
                break
            else:
                break
        return moves

    def set_image(self):
        if self.color == Constants.FIG_WHITE:
            return Images.W_QUEEN
        else:
            return Images.B_QUEEN
