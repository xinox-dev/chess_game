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
    BOARD = image.load(ROOT_PATH + '\\assets\\board.png')

    # shadows
    GREEN_SHADOW = image.load(ROOT_PATH + '\\assets\\green_shadow.png')
    SELECTED_SHADOW = image.load(ROOT_PATH + '\\assets\\selected_shadow.png')

    # buttons
    BTN_DEV = image.load(ROOT_PATH + '\\assets\\btn.png')
    BTN_DEV_A = image.load(ROOT_PATH + '\\assets\\btn_a.png')
    P_VS_AI = image.load(ROOT_PATH + '\\assets\\per_ai_choose.png')
    P_VS_P = image.load(ROOT_PATH + '\\assets\\per_per_choose.png')
    WHITE_CHOOSE = image.load(ROOT_PATH + '\\assets\\white_choose.png')
    BLACK_CHOOSE = image.load(ROOT_PATH + '\\assets\\black_choose.png')
    RANDOM_CHOOSE = image.load(ROOT_PATH + '\\assets\\random_choose.png')
