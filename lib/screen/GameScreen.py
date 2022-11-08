from lib.board.Board import Board
from lib.utils.Constants import Constants
import pygame


class GameScreen:
    def __init__(self):
        self.press_cur_x, self.press_cur_y = (-1, -1)
        self.pos_of_board_x, self.pos_of_board_y = (100, 100)
        self.pos_on_board_x, self.pos_on_board_y = (-1, -1)
        self.board = Board(Constants.WHITE)
        self.background_color = (100, 100, 100)
        self.turn = Constants.WHITE

    def action(self, x, y):
        print(self.board.available_moves_on_check)
        self.set_press_cursor(x, y)
        if self.board.check_move(self.pos_on_board_x, self.pos_on_board_y):
            self.board.move(self.pos_on_board_x, self.pos_on_board_y)
            self.turn = Constants.BLACK if self.turn == Constants.WHITE else Constants.WHITE

            king = self.board.find_king(self.turn)
            if king.check_check(self.board.fields):
                self.board.check_color = self.turn
                self.board.set_available_moves_on_check()
                if not self.board.available_moves_on_check:
                    print("SZACH MAT!!!")

        else:
            self.set_selected_figure()

    def draw_screen(self, window):
        window.fill(self.background_color)

        if self.pos_on_board_x >= 0 and self.pos_on_board_y >= 0:
            self.draw_selected_field(window)

        if self.board.selected_figure:
            pygame.draw.rect(window, (100, 150, 10), self.create_rect_selected_figure())
            self.draw_possible_moves(window)

        self.board.draw_fields(window)

    def set_press_cursor(self, x, y):
        self.press_cur_x, self.press_cur_y = x, y
        pos_on_board_x = (self.press_cur_x - self.pos_of_board_x) / Constants.SIZE_CELL_OF_BOARD
        pos_on_board_y = (self.press_cur_y - self.pos_of_board_y) / Constants.SIZE_CELL_OF_BOARD

        if 0 <= pos_on_board_x < 8:
            self.pos_on_board_x = int(pos_on_board_x)
        else:
            self.pos_on_board_x = -1

        if 0 <= pos_on_board_y < 8:
            self.pos_on_board_y = int(pos_on_board_y)
        else:
            self.pos_on_board_y = -1

    def set_selected_figure(self):
        if self.pos_on_board_x >= 0 and self.pos_on_board_y >= 0:
            self.board.select_figure(self.turn, self.pos_on_board_x, self.pos_on_board_y)

    def create_rect_selected_figure(self):
        x = self.pos_of_board_x + self.board.selected_figure.pos_x * 80
        y = self.pos_of_board_y + self.board.selected_figure.pos_y * 80
        return pygame.rect.Rect(x, y, 80, 80)

    def draw_selected_field(self, window):
        x = Constants.POS_OF_BOARD_X + self.pos_on_board_x * 80
        y = Constants.POS_OF_BOARD_Y + self.pos_on_board_y * 80
        square = pygame.rect.Rect(x, y, 80, 80)
        pygame.draw.rect(window, (100, 1, 1), square)

    def draw_possible_moves(self, window):
        moves = self.board.selected_figure.possible_moves(self.board.fields)
        for m in moves:
            if self.board.white_on_top:
                pos_x = m[0]
                pos_y = m[1]
            else:
                pos_x = 7 - m[0]
                pos_y = 7 - m[1]
            x = Constants.POS_OF_BOARD_X + pos_x * 80
            y = Constants.POS_OF_BOARD_Y + pos_y * 80
            square = pygame.rect.Rect(x, y, 80, 80)
            pygame.draw.rect(window, (100, 1, 1), square)
