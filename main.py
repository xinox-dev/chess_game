import pygame
from config import game_setings
from chesslogic.Board import Board
from config.game_setings import POS_OF_BOARD_X, POS_OF_BOARD_Y, RGB_SELECTED_CELL
from assets.load_assets import img_figures, img_board
from config.board import EMPTY, WHITES, BLACKS, FIGURES

# start settings for pygame window application
pygame.init()
window = pygame.display.set_mode((game_setings.WIN_WIDTH, game_setings.WIN_HEIGHT))
app_running = True
cursor_x, cursor_y = (0, 0)
set_fps = pygame.time.Clock().tick

# init board
board = Board()
available_moves = []
turn_whites = True
is_select = False
selected_figure = (-1, -1)
cur_board_x, cur_board_y = -1, -1


def set_cursor_on_board():
    global cur_board_x, cur_board_y

    x = (cursor_x - POS_OF_BOARD_X) / game_setings.FIGURE_IMG_SIZE
    y = (cursor_y - POS_OF_BOARD_Y) / game_setings.FIGURE_IMG_SIZE
    cur_board_x = int(x) if x >= 0 else -1
    cur_board_y = int(y) if y >= 0 else -1


def set_available_moves():
    global available_moves

    x, y = selected_figure[0], selected_figure[1]
    if 0 <= x <= 7 and 0 <= y <= 7:
        available_moves = board.check_available_move(x, y)
    else:
        available_moves = []


def set_selected_figure():
    global selected_figure, is_select

    x, y = cur_board_x, cur_board_y
    if 0 <= x <= 7 and 0 <= y <= 7 and board.view_board()[x][y] in FIGURES[turn_color]:
        selected_figure = (x, y)
        is_select = True
    else:
        selected_figure = (-1, -1)
        is_select = False


def move_on_board():
    global board, turn_whites

    if is_select and (cur_board_x, cur_board_y) in available_moves:
        board.move(selected_figure[0], selected_figure[1], cur_board_x, cur_board_y)
        turn_whites = not turn_whites


def draw_board(v_board):
    for i in range(8):
        for j in range(8):
            x, y = POS_OF_BOARD_X + game_setings.FIGURE_IMG_SIZE * j, POS_OF_BOARD_Y + game_setings.FIGURE_IMG_SIZE * i
        # draw available moves
            if (j, i) in available_moves:
                square_color = game_setings.RGB_ALLOWED_CELL
                square = pygame.rect.Rect(x, y, game_setings.FIGURE_IMG_SIZE, game_setings.FIGURE_IMG_SIZE)
                pygame.draw.rect(window, square_color, square)
        # draw selected cell
            if x <= cursor_x <= x + game_setings.FIGURE_IMG_SIZE and y <= cursor_y <= y + game_setings.FIGURE_IMG_SIZE:
                square_color = RGB_SELECTED_CELL
                square = pygame.rect.Rect(x, y, game_setings.FIGURE_IMG_SIZE, game_setings.FIGURE_IMG_SIZE)
                pygame.draw.rect(window, square_color, square)

        # draw figures
            if v_board[j][i] != EMPTY:
                window.blit(img_figures[v_board[j][i]], (x, y))


def check_event(events):
    global app_running, available_moves, cursor_y, cursor_x

    for e in events:
        if e.type == pygame.QUIT:
            app_running = False
        if e.type == pygame.MOUSEBUTTONUP:
            cursor_x, cursor_y = pygame.mouse.get_pos()


while app_running:
    area = board.view_board()
    turn_color = WHITES if turn_whites else BLACKS

    set_fps(game_setings.FPS)
    set_available_moves()
    set_cursor_on_board()
    move_on_board()
    set_selected_figure()

    check_event(pygame.event.get())

    window.fill(game_setings.RGB_BACKGROUND)
    window.blit(img_board, (POS_OF_BOARD_X - 33, POS_OF_BOARD_Y - 34))
    draw_board(area)
    pygame.display.update()

# if __name__ == "__main__":
#     main()




