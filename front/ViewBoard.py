from config import game_setings
from config.board import EMPTY
from config.game_setings import POS_OF_BOARD
from load_assets import img_figures
import pygame


class ViewBoard:
    def __int__(self, area):
        self.area = area
        self.pos_board_x, self.pos_board_y = POS_OF_BOARD



