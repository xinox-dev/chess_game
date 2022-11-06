from config import board as cfg_board
from backend.show_available_moves import show_move


def figure_movement(current_x: int, current_y: int, target_x: int, target_y: int, board: any):
    c_x, c_y, t_x, t_y = current_x, current_y, target_x, target_y
    figure = board[c_x][c_y]
    print(figure)
    kill = cfg_board.EMPTY
    available_moves = show_move(board, c_x, c_y)
    print(available_moves)
    if (t_x, t_y) in available_moves:
        if figure == cfg_board.B_PAWN or figure == cfg_board.W_PAWN:
            if c_x != t_x:
                x, y = int((c_x + t_x) / 2), int((c_y + t_y) / 2)
                kill = board[x][y]
                board[x][y] = cfg_board.EMPTY

        elif figure in cfg_board.FIGURES[cfg_board.WHITES] or figure in cfg_board.FIGURES[cfg_board.BLACKS]:
            target = board[t_x][t_y]
            if target != cfg_board.EMPTY:
                kill = board[t_x][t_y]
                board[t_x][t_y] = cfg_board.EMPTY

        else:
            return board, kill, False

        board[c_x][c_y] = cfg_board.EMPTY
        board[t_x][t_y] = figure

        return board, kill, True

    else:
        return board, kill, False
