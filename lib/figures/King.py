from lib.utils.Constants import Constants
from lib.utils.Images import Images


class King:
    def __init__(self, color):
        self.color = color
        self.img = self.set_image()

    def get_possible_moves(self, board, pos_x, pos_y):
        moves = []
        # TODO
        return moves

    def set_image(self):
        if self.color == Constants.WHITE:
            return Images.W_KING
        else:
            return Images.B_KING
