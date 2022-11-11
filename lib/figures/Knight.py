from lib.utils.Constants import Constants
from lib.utils.Images import Images


class Knight:
    def __init__(self, color):
        self.color = color
        self.img = self.set_image()
    
    def get_possible_moves(self, board, pos_x, pos_y):
        moves = []
        potential_move = [(pos_x-2, pos_y+1), (pos_x-1, pos_y+2), (pos_x+1, pos_y+2), (pos_x+2, pos_y+1),
                          (pos_x+2, pos_y-1), (pos_x+1, pos_y-2), (pos_x-1, pos_y-2), (pos_x-2, pos_y-1)]
        for m in potential_move:
            x, y = m
            if 0 <= x <= 7 and 0 <= y <= 7:
                field = board[x][y]
                if field.empty:
                    moves.append((x, y))
                else:
                    if field.figure.color != self.color:
                        moves.append((x, y))

        return moves

    def set_image(self):
        if self.color == Constants.FIG_WHITE:
            return Images.W_KNIGHT
        else:
            return Images.B_KNIGHT
