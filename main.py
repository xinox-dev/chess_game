import pygame
from config import game_setings
from backend.Board import Board
from config.game_setings import POS_OF_BOARD_X, POS_OF_BOARD_Y, RGB_SELECTED_CELL
from load_assets import img_figures
from config.board import EMPTY, WHITES, BLACKS, FIGURES
from backend.show_available_moves import show_move
# start settings for pygame window application
pygame.init()
window = pygame.display.set_mode((game_setings.WIN_WIDTH, game_setings.WIN_HEIGHT))
app_running = True
cursor_x, cursor_y = (0, 0)

# init board
board = Board()
available_moves = []
turn_whites = True
is_select = False
selected_figure = (-1, -1)


def gameplay(cur_x, cur_y):
    global selected_figure, is_select, turn_whites, available_moves
    global board
    for i in range(8):
        for j in range(8):
            if is_select and cur_x == j and cur_y == i:
                if (j, i) in available_moves:
                    board.move(selected_figure[0], selected_figure[1], j, i)
                    turn_whites = not turn_whites
            if cur_x == j and cur_y == i:
                if board.view_board()[j][i] in FIGURES[turn_color]:
                    selected_figure = (j, i)
                    is_select = True
                    available_moves = board.check_available_move(j, i)
                else:
                    selected_figure = (0, 0)
                    is_select = False
                    available_moves = []


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


while app_running:
    area = board.view_board()
    turn_color = WHITES if turn_whites else BLACKS
    pygame.time.Clock().tick(game_setings.FPS)
    cur_board_x = int((cursor_x - POS_OF_BOARD_X) / game_setings.FIGURE_IMG_SIZE)
    cur_board_y = int((cursor_y - POS_OF_BOARD_Y) / game_setings.FIGURE_IMG_SIZE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_running = False
        if event.type == pygame.MOUSEBUTTONUP:
            cursor_x, cursor_y = pygame.mouse.get_pos()
            if not POS_OF_BOARD_X <= cursor_x <= POS_OF_BOARD_X + game_setings.FIGURE_IMG_SIZE * 8 \
                    or not POS_OF_BOARD_Y <= cursor_y <= POS_OF_BOARD_Y + game_setings.FIGURE_IMG_SIZE * 8:
                available_moves = []

    window.fill((100, 130, 140))

    gameplay(cur_board_x, cur_board_y)
    draw_board(area)

    pygame.display.update()

# if __name__ == "__main__":
#     main()




