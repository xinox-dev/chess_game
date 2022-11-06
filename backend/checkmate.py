from backend.show_available_moves import show_move
from config import board as cfg_board


def mate(color: str, board: any):
    figure = cfg_board.W_KING if color == cfg_board.WHITES else cfg_board.B_KING
    ally_figures = cfg_board.FIGURES[color]
    ally_shield = True
    king_pos = ()
    for i in range(8):
        for j in range(8):
            if board[i][j] == figure:
                king_pos = (i, j)

    if king_pos:
        x, y = king_pos
        potential_move = [(x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1), (x-1, y), (x-1, y-1)]
        for m in potential_move:
            m_x, m_y = m
            f = board[m_x][m_y]
            if x < 0 or x > 7 or y < 0 or y > 7 or f in ally_figures:
                continue
            else:
                ally_shield = False
        if ally_shield:
            return False
        else:
            moves = show_move(board, x, y)
            if not moves:
                return True
            else:
                return False
    else:
        return False


def check(color: str, board: any):
    figure = cfg_board.W_KING if color == cfg_board.WHITES else cfg_board.B_KING
    enemy_figures = cfg_board.ENEMY_FIGURES[color]
    k_x, k_y= 0, 0
    save_zone = [[cfg_board.EMPTY for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if board[i][j] == figure:
                k_x, k_y = i, j

    for k in range(8):
        for n in range(8):
            fig = board[k][n]
            if fig in enemy_figures:
                enemy_moves = show_move(board, k, n)
                for mov in enemy_moves:
                    mov_x, mov_y = mov
                    save_zone[mov_x][mov_y] = 'X'

    if save_zone[k_x][k_y] != cfg_board.EMPTY:
        return True
    else:
        return False

