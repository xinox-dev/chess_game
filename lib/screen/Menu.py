import pygame
import random
from lib.utils.Button import Button
from lib.utils.Images import Images
from lib.screen.SubWindow import SubWindow
from lib.utils.Constants import Constants
from lib.screen.Game import Game


class Menu:
    def __init__(self, fun_create_game):
        self.is_on = True
        self.background = (0, 0, 0)
        self.pos_fields_x, self.pos_fields_y = 930, 550
        self.press_cur_x, self.press_cur_y = -1, -1
        self.subwindow: SubWindow = None
        self.create_game = fun_create_game
        self.fields = [
            {
                'name': 'New Game',
                'action': self.newgame
            },
            {
                'name': 'About',
                'action': self.about
            },
            {
                'name': 'Exit',
                'action': self.exit
            }
        ]
        self.buttons = self.create_menu_buttons()

    def draw(self, window):
        # draw transparently bg
        if self.is_on:
            s = pygame.Surface((1200, 800))
            s.set_alpha(200)
            s.fill(Constants.BLACK)
            window.blit(s, (0, 0))
        # draw main buttons
        for btn in self.buttons:
            btn.draw(window)
        # draw window with sub menu
        if self.subwindow:
            self.subwindow.draw(window)

    def create_menu_buttons(self):
        buttons = []
        for i, field in enumerate(self.fields):
            btn = Button(self.pos_fields_x, self.pos_fields_y + i * 70, function=field['action'], name=field['name'])
            buttons.append(btn)
        return buttons

    def action(self, cur_x, cur_y):
        self.set_cursor(cur_x, cur_y)
        self.check_on_click_in_btn()
        if self.subwindow:
            self.subwindow.action(cur_x, cur_y)

    def newgame(self):
        self.is_on = True
        random_color = random.choice([Constants.FIG_WHITE, Constants.FIG_BLACK])
        btn_white = Button(-1, -1, self.create_game, img=Images.WHITE_CHOOSE, name=Constants.FIG_WHITE, text=False)
        btn_black = Button(-1, -1, self.create_game, img=Images.BLACK_CHOOSE, name=Constants.FIG_BLACK, text=False)
        btn_random = Button(-1, -1, self.create_game, img=Images.RANDOM_CHOOSE, name=random_color, text=False)
        buttons = [btn_white, btn_black, btn_random]

        subwin = SubWindow(close_functon=self.close_subwindow, title='Take color', buttons=buttons)
        self.subwindow = subwin

    def about(self):
        # TODO
        print('about')

    def exit(self):
        self.is_on = True
        desc = 'Take scissors and cut cable of computer :)'
        subwin = SubWindow(close_functon=self.close_subwindow, title='Are you sure?', desc=desc)
        self.subwindow = subwin

    def set_cursor(self, cur_x, cur_y):
        self.press_cur_x = cur_x
        self.press_cur_y = cur_y

    def check_on_click_in_btn(self):
        for btn in self.buttons:
            if btn.pos_x <= self.press_cur_x <= btn.pos_x + btn.width \
                    and btn.pos_y <= self.press_cur_y <= btn.pos_y + btn.height:
                btn.on_click = True
                btn.use()

    def close_subwindow(self):
        self.subwindow = None
        self.is_on = False
