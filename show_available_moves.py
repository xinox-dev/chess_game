from config import board as cfg_board


def show_moves_pawn(player: str, x: int, y: int, board: any):  # Check move for any Pawn
    moves = []
    if player == cfg_board.WHITES:
        if board[x][y+1] == cfg_board.EMPTY:
            moves.append((x, y+1))
            if y <= 5:
                if board[x][y+2] == cfg_board.EMPTY and y == 1:
                    moves.append((x, y+2))
                # check if player have opponent
                if  x <= 5 and board[x+1][y+1] != cfg_board.EMPTY :
                    if board[x+1][y+1] in cfg_board.FIGURES[cfg_board.BLACKS] and board[x + 2][y + 2] == cfg_board.EMPTY:
                        moves.append((x+2, y+2))
                if x >= 2 and board[x-1][y+1] != cfg_board.EMPTY:
                    if board[x-1][y+1] in cfg_board.FIGURES[cfg_board.BLACKS] and board[x - 2][y + 2] == cfg_board.EMPTY:
                        moves.append((x-2, y+2))

    elif player == cfg_board.BLACKS:
        if board[x][y - 1] == cfg_board.EMPTY:
            moves.append((x, y-1))
            if y >= 2:
                if board[x][y-2] == cfg_board.EMPTY and y == 6:
                    moves.append((x, y-2))
                # check if player have opponent
                if x >= 2 and board[x-1][y-1] != cfg_board.EMPTY:
                    if board[x-1][y-1] in cfg_board.FIGURES[cfg_board.WHITES] and board[x - 2][y + -2] == cfg_board.EMPTY:
                        moves.append((x-2, y-2))
                if x <= 5 and board[x+1][y-1] != cfg_board.EMPTY:
                    if board[x+1][y-1] in cfg_board.FIGURES[cfg_board.WHITES] and board[x + 2][y - 2] == cfg_board.EMPTY:
                        moves.append((x+2, y-2))

    return moves


# Check move for any Tower
def show_moves_tower(player: str, x: int, y: int, board: any):
    moves = []
    enemy_figures = cfg_board.ENEMY_FIGURES[player]
    # check moves to upper
    for i in range(x-1, -1, -1):
        if board[i][y] == cfg_board.EMPTY:
            moves.append((i, y))
        elif board[i][y] in enemy_figures:
            moves.append((i, y))
            break
        elif board[i][y] != cfg_board.EMPTY:
            break
    # check moves to bottom
    for i in range(x+1, 8):
        if board[i][y] == cfg_board.EMPTY:
            moves.append((i, y))
        elif board[i][y] in enemy_figures:
            moves.append((i, y))
            break
        elif board[i][y] != cfg_board.EMPTY:
            break
    # check moves to left
    for i in range(y-1, -1, -1):
        if board[x][i] == cfg_board.EMPTY:
            moves.append((x, i))
        elif board[x][i] in enemy_figures:
            moves.append((x, i))
            break
        elif board[x][i] != cfg_board.EMPTY:
            break
    # check moves to right
    for i in range(y+1, 8):
        if board[x][i] == cfg_board.EMPTY:
            moves.append((x, i))
        elif board[x][i] in enemy_figures:
            moves.append((x, i))
            break
        elif board[x][i] != cfg_board.EMPTY:
            break
    return moves


# Check move for any Knight
def show_moves_knight(player: str, x: int, y: int, board: any):
    ally_figures = cfg_board.FIGURES[player]
    potential_move = [(x-2, y+1), (x-1, y+2), (x+1, y+2), (x+2, y+1), (x+2, y-1), (x+1, y-2), (x-1, y-2), (x-2, y-1)]
    moves = []
    for m in potential_move:
        x, y = m
        if x < 0 or x > 7 or y < 0 or y > 7:
            continue
        f = board[x][y]
        if f in ally_figures:
            continue
        moves.append((x, y))
    return moves


# Check move for any Bishop
def show_moves_bishop(player: str, x: int, y: int, board: any):
    moves = []
    enemy_figures = cfg_board.ENEMY_FIGURES[player]
    # check south-east
    for i in range(1, 8):
        if x+i > 7 or y+i > 7:
            break
        f = board[x+i][y+i]
        if f == cfg_board.EMPTY:
            moves.append((x + i, y + i))
        elif f in enemy_figures:
            moves.append((x + i, y + i))
            break
        else:
            break

    # check south-west
    for i in range(1, 8):
        if x+i > 7 or y-i < 0:
            break
        f = board[x+i][y-i]
        if f == cfg_board.EMPTY:
            moves.append((x + i, y - i))
        elif f in enemy_figures:
            moves.append((x + i, y - i))
            break
        else:
            break

    # check north-west
    for i in range(1, 8):
        if x - i < 0 or y - i < 0:
            break
        f = board[x - i][y - i]
        if f == cfg_board.EMPTY:
            moves.append((x - i, y - i))
        elif f in enemy_figures:
            moves.append((x - i, y - i))
            break
        else:
            break

    # check north-east
    for i in range(1, 8):
        if x - i < 0 or y + i > 7:
            break
        f = board[x - i][y + i]
        if f == cfg_board.EMPTY:
            moves.append((x - i, y + i))
        elif f in enemy_figures:
            moves.append((x - i, y + i))
            break
        else:
            break

    return moves


# Check moves for any Queen
def show_moves_queen(player: str, x: int, y: int, board: any):
    return show_moves_bishop(player, x, y, board) + show_moves_tower(player, x, y, board)


# Check moves for any King
def show_moves_king(player: str, x: int, y: int, board: any):
    moves = []
    enemy_figures = cfg_board.ENEMY_FIGURES[player]
    ally_figures = cfg_board.FIGURES[player]
    potential_move = [(x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1), (x-1, y), (x-1, y-1)]
    near_enemy = []

    def set_save_zone(subboard: any):
        zone = [[cfg_board.EMPTY for _ in range(8)] for _ in range(8)]
        for k in range(8):
            for n in range(8):
                fig = subboard[k][n]
                if fig == cfg_board.B_KING or fig == cfg_board.W_KING:
                    continue
                if fig in enemy_figures:
                    enemy_moves = show_move(subboard, k, n)
                    for mov in enemy_moves:
                        mov_x, mov_y = mov
                        zone[mov_x][mov_y] = 'X'
        return zone

    # set near_enemy
    for i in range(8):
        for j in range(8):
            f = board[i][j]
            if f in enemy_figures:
                for m in potential_move:
                    m_x, m_y = m
                    if x < 0 or x > 7 or y < 0 or y > 7:
                        continue
                    if (i, j) == (m_x, m_y):
                        near_enemy.append((i, j))

    # check far enemy range
    save_zone = set_save_zone(board)

    # check near range enemy
    for m in near_enemy:
        m_x, m_y = m
        buffor = board[m_x][m_y]
        board[m_x][m_y] = cfg_board.EMPTY
        sub_zone = set_save_zone(board)
        save_zone[m_x][m_y] = sub_zone[m_x][m_y]
        board[m_x][m_y] = buffor

    for m in potential_move:
        m_x, m_y = m
        if m_x < 0 or m_x > 7 or m_y < 0 or m_y > 7:
            continue
        f = board[m_x][m_y]

        dangerous = save_zone[m_x][m_y]
        if f in ally_figures or dangerous != cfg_board.EMPTY:
            continue
        moves.append((m_x, m_y))
    return moves


def show_move(board, x, y):
    pawn = board[x][y]
    moves = []
    color = cfg_board.WHITES if pawn in cfg_board.FIGURES[cfg_board.WHITES] else cfg_board.BLACKS
    if pawn == cfg_board.W_PAWN or pawn == cfg_board.B_PAWN:
        moves = show_moves_pawn(color, x, y, board)

    elif pawn == cfg_board.W_ROOK or pawn == cfg_board.B_ROOK:
        moves = show_moves_tower(color, x, y, board)

    elif pawn == cfg_board.W_KNIGHT or pawn == cfg_board.B_KNIGHT:
        moves = show_moves_knight(color, x, y, board)

    elif pawn == cfg_board.W_BISHOP or pawn == cfg_board.B_BISHOP:
        moves = show_moves_bishop(color, x, y, board)

    elif pawn == cfg_board.W_QUEEN or pawn == cfg_board.B_QUEEN:
        moves = show_moves_queen(color, x, y, board)

    elif pawn == cfg_board.W_KING or pawn == cfg_board.B_KING:
        moves = show_moves_king(color, x, y, board)

    return moves
