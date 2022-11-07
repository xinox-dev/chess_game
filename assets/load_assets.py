import pygame
from config.board import W_PAWN, W_ROOK, W_KNIGHT, W_BISHOP, W_QUEEN, W_KING, B_PAWN, B_ROOK, B_KNIGHT, B_BISHOP, B_QUEEN, B_KING
from lib.utils.game_setings import FIGURE_IMG_SIZE


def load_figure(figure):
    img = pygame.image.load(rf'assets/{figure}.png')
    scale = pygame.transform.scale(img, (FIGURE_IMG_SIZE, FIGURE_IMG_SIZE))
    return scale


img_figures = {
    W_PAWN: load_figure(W_PAWN),
    B_PAWN: load_figure(B_PAWN),
    W_ROOK: load_figure(W_ROOK),
    B_ROOK: load_figure(B_ROOK),
    W_KNIGHT: load_figure(W_KNIGHT),
    B_KNIGHT: load_figure(B_KNIGHT),
    W_BISHOP: load_figure(W_BISHOP),
    B_BISHOP: load_figure(B_BISHOP),
    W_QUEEN: load_figure(W_QUEEN),
    B_QUEEN: load_figure(B_QUEEN),
    W_KING: load_figure(W_KING),
    B_KING: load_figure(B_KING),
}
img_board = pygame.transform.scale(pygame.image.load('assets/board.jpg'), (705, 705))
