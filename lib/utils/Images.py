from pygame import image
from os import path


class Images:
    ROOT_PATH = path.abspath(path.join(path.dirname(__file__), "..\..", ""))
    # Figures
    W_PAWN = image.load(ROOT_PATH + '\\assets\\white_pawn.png')
    B_PAWN = image.load(ROOT_PATH + '\\assets\\black_pawn.png')
    W_ROOK = image.load(ROOT_PATH + '\\assets\\white_rook.png')
    B_ROOK = image.load(ROOT_PATH + '\\assets\\black_rook.png')
    W_KNIGHT = image.load(ROOT_PATH + '\\assets\\white_knight.png')
    B_KNIGHT = image.load(ROOT_PATH + '\\assets\\black_knight.png')
    W_BISHOP = image.load(ROOT_PATH + '\\assets\\white_bishop.png')
    B_BISHOP = image.load(ROOT_PATH + '\\assets\\black_bishop.png')
    W_QUEEN = image.load(ROOT_PATH + '\\assets\\white_queen.png')
    B_QUEEN = image.load(ROOT_PATH + '\\assets\\black_queen.png')
    W_KING = image.load(ROOT_PATH + '\\assets\\white_king.png')
    B_KING = image.load(ROOT_PATH + '\\assets\\black_king.png')

    # Board
    BOARD = image.load(ROOT_PATH + '\\assets\\board.jpg')
