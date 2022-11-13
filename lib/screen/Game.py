from lib.board.Board import Board
from lib.utils.Constants import Constants
from lib.utils.Images import Images
from lib.screen.SubWindow import SubWindow
from AI.Bot import Bot
import pygame


class Game:
    def __init__(self, color, menu,  bot=False):
        self.press_cur_x, self.press_cur_y = (-1, -1)
        self.pos_on_board_x, self.pos_on_board_y = (-1, -1)
        self.p1_color = color
        self.board = Board(color)
        self.background_color = (58, 48, 66)
        self.color_of_turn = Constants.FIG_WHITE
        self.bot = self.set_bot(bot)
        self.checkmate = None
        self.first_bot_move()
        self.menu = menu

    def action(self, x, y):
        # set last position press cursor
        self.set_press_cursor(x, y)

        if self.board.check_move(self.pos_on_board_x, self.pos_on_board_y):
            if not self.checkmate:
                self.move_on_board()

        else:
            self.set_selected_figure()

    def draw(self, window):
        # background
        window.fill(self.background_color)
        # board
        window.blit(Images.BOARD_F, (Constants.POS_OF_BOARD_X-40, Constants.POS_OF_BOARD_Y-40))
        # figures
        self.board.draw_fields(window)
        # selected field
        if self.pos_on_board_x >= 0 and self.pos_on_board_y >= 0:
            self.draw_selected_field(window)
        # available moves
        if self.board.selected_figure:
            self.draw_possible_moves(window)
        # draw color_of_turn
        self.draw_turn_color(window)

    def set_press_cursor(self, x, y):
        self.press_cur_x, self.press_cur_y = x, y
        pos_on_board_x = (self.press_cur_x - Constants.POS_OF_BOARD_X) / Constants.SIZE_CELL_OF_BOARD
        pos_on_board_y = (self.press_cur_y - Constants.POS_OF_BOARD_Y) / Constants.SIZE_CELL_OF_BOARD

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
            self.board.select_figure(self.color_of_turn, self.pos_on_board_x, self.pos_on_board_y)

    def draw_selected_field(self, window):
        x = Constants.POS_OF_BOARD_X + self.pos_on_board_x * Constants.SIZE_CELL_OF_BOARD
        y = Constants.POS_OF_BOARD_Y + self.pos_on_board_y * Constants.SIZE_CELL_OF_BOARD
        window.blit(Images.SELECTED_SHADOW, (x, y))

    def draw_possible_moves(self, window):
        if not self.board.check_color:
            moves = self.board.selected_figure.possible_moves(self.board.fields)
        else:
            moves = []
            for available_move in self.board.available_moves_on_check:
                if available_move[0] == self.board.selected_figure:
                    moves.append(available_move[1])
        for m in moves:
            if self.board.white_on_top:
                pos_x = m[0]
                pos_y = m[1]
            else:
                pos_x = 7 - m[0]
                pos_y = 7 - m[1]
            x = Constants.POS_OF_BOARD_X + pos_x * Constants.SIZE_CELL_OF_BOARD
            y = Constants.POS_OF_BOARD_Y + pos_y * Constants.SIZE_CELL_OF_BOARD
            window.blit(Images.GREEN_SHADOW, (x, y))

    def draw_turn_color(self, window):
        x = Constants.POS_OF_BOARD_X + Constants.SIZE_CELL_OF_BOARD*8 + 100
        y = Constants.POS_OF_BOARD_Y + Constants.SIZE_CELL_OF_BOARD*8/2

        if self.color_of_turn == Constants.FIG_WHITE:
            pygame.draw.circle(window, Constants.BLACK, (x, y), 32)
            pygame.draw.circle(window, Constants.WHITE, (x, y), 30)
        else:
            pygame.draw.circle(window, Constants.WHITE, (x, y), 31)
            pygame.draw.circle(window, Constants.BLACK, (x, y), 30)

    def set_bot(self, bot):
        if bot:
            color = Constants.FIG_WHITE if self.p1_color != Constants.FIG_WHITE else Constants.FIG_BLACK
            return Bot(color)
        else:
            return None

    def move_on_board(self):
        if self.checking_castle():
            self.board.castle(self.pos_on_board_x, self.pos_on_board_y)
        else:
            self.board.move(self.pos_on_board_x, self.pos_on_board_y)
        self.color_of_turn = Constants.FIG_BLACK if self.color_of_turn == Constants.FIG_WHITE else Constants.FIG_WHITE
        # checking if there is a check or checkmate
        king = self.board.find_king(self.board.fields, self.color_of_turn)

        if king.check_pat(self.board.fields):
            self.checkmate = True
            title = f'Draw ..'
            desc = 'PAT xD'
            self.menu.endgame(title, desc)

        if king.check_check(self.board.fields):
            self.board.check_color = self.color_of_turn
            self.board.set_available_moves_on_check()
            if not self.board.available_moves_on_check:
                color_win = Constants.FIG_BLACK if self.color_of_turn == Constants.FIG_WHITE else Constants.FIG_WHITE
                self.checkmate = True
                title = f"{color_win.upper()}'S WIN !!!"
                desc = 'Check Mate'
                self.menu.endgame(title, desc)
        if not self.checkmate:
            if self.bot and self.bot.color == self.color_of_turn:
                self.bot_move()

    def bot_move(self):
        pos_fig, move = self.bot.get_move(self.board)
        p_x, p_y = pos_fig
        x, y = move
        if self.bot.color == Constants.FIG_BLACK:
            self.pos_on_board_x = 7 - p_x
            self.pos_on_board_y = 7 - p_y
            self.set_selected_figure()
            self.pos_on_board_x = 7 - x
            self.pos_on_board_y = 7 - y
        else:
            self.pos_on_board_x = p_x
            self.pos_on_board_y = p_y
            self.set_selected_figure()
            self.pos_on_board_x = x
            self.pos_on_board_y = y
        self.move_on_board()

    def first_bot_move(self):
        if self.bot and self.bot.color == self.color_of_turn:
            self.bot_move()

    def checking_castle(self):
        if (self.pos_on_board_x, self.pos_on_board_y) in [(0, 0), (7, 0), (0, 7), (7, 7)]:
            if self.board.selected_figure.symbol == 'k' and not self.board.kings_already_move[Constants.FIG_WHITE]:
                return True

            if self.board.selected_figure.symbol == 'K' and not self.board.kings_already_move[Constants.FIG_BLACK]:
                return True

        return False
