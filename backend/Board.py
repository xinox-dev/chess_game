from config import board as cfg_board
from backend.show_available_moves import show_move
from backend.checkmate import check, mate
from backend.move_on_board import figure_movement


class Board:
    def __init__(self):
        self.area = cfg_board.BOARD_SET

    def check_available_move(self, x: int, y: int):
        return show_move(self.area, x, y)

    def check_check(self, color: str):
        return check(color, self.area)

    def check_checkmate(self, color: str):
        return mate(color, self.area)

    def move(self, x, y, target_x, target_y):
        board, kill, is_success = figure_movement(x, y, target_x, target_y, self.area)
        print(is_success)
        if is_success:
            self.area = board
            return kill

    def view_board(self):
        return self.area
