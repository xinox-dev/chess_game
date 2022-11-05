import pygame
from config import game_setings as cfg_main
from Board import Board
from load_assets import img_figures
from config.board import EMPTY

# start settings for pygame window application
pygame.init()
window = pygame.display.set_mode((cfg_main.WIN_WIDTH, cfg_main.WIN_HEIGHT))
app_running = True

# init board
board = Board()
area = board.view_board()

pos_x, pos_y = (0, 0)
test = pygame.image.load("assets/black_king.png")

def draw_current_cell():
    for i in range(8):
        for j in range(8):
            f_width, f_height = cfg_main.FIGURE_IMG_SIZE
            x, y = s_x+f_width*j, s_y+f_height*i
            if x <= pos_x <= x+f_width and y <= pos_y <= y+f_height:
                square_color = (200, 20, 200)
                square = pygame.rect.Rect(x, y, f_width, f_height)
                pygame.draw.rect(window, square_color, square)

def draw_figures():
    for i in range(8):
        for j in range(8):
            f_width, f_height = cfg_main.FIGURE_IMG_SIZE
            x, y = s_x + f_width * j, s_y + f_height * i
            if area[j][i] != EMPTY:
                window.blit(img_figures[area[j][i]], (x, y))


while app_running:
    pygame.time.Clock().tick(cfg_main.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos_x, pos_y = pygame.mouse.get_pos()

    window.fill((100, 130, 140))
    s_x, s_y = 100, 100
    draw_current_cell()
    draw_figures()

    pygame.display.update()

# if __name__ == "__main__":
#     main()




