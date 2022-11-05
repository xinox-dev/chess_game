import pygame
from config import game_setings as cfg_main

pygame.init()
window = pygame.display.set_mode((cfg_main.WIN_WIDTH, cfg_main.WIN_HEIGHT))

pos_x, pos_y = (0, 0)

app_running = True
while app_running:
    window.fill((100, 130, 140))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos_x, pos_y = pygame.mouse.get_pos()
    square_color = (20, 200, 20)
    s_x, s_y = 100, 100
    for i in range(8):
        for j in range(8):
            a, b = s_x+80*j, s_y+80*i
            if a <= pos_x <= a+50 and b <= pos_y <= b+50:
                square_color = (200, 20, 200)
            else:
                square_color = (20, 200, 20)
            square = pygame.rect.Rect(a, b, 50, 50)
            pygame.draw.rect(window, square_color, square)

    pygame.display.update()
#
# if __name__ == "__main__":
#     main()




# from Board import Board
#
# board = Board()
# area = board.view_board()
#
# while True:
#     area = board.view_board()
#
#     print('  A  B  C  D  E  F  G  H')
#     print('|--------------------------|')
#     for i in range(8):
#         print('| ', end=' ')
#         for j in range(8):
#             print(area[j][i]+' ', sep='', end=' ')
#         print(f'| {i+1}', end='\n')
#
#     print('|--------------------------|')
#
#     s = input("Command:")
#
#     if s == '9':
#         break
#
#     if s == '8':
#         m = input('move:')
#         x, y, t_x, t_y = m.split(' ')
#         board.move(int(x), int(y), int(t_x), int(t_y))
#
