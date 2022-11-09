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
        # window.fill(self.background)
        for btn in self.buttons:
            btn.draw(window)

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
        random_color = random.choice([Constants.WHITE, Constants.BLACK])
        btn_choose_white = Button(-1, -1, self.create_game, img=Images.WHITE_CHOOSE, name=Constants.WHITE, text=False)
        btn_choose_black = Button(-1, -1, self.create_game, img=Images.BLACK_CHOOSE, name=Constants.BLACK, text=False)
        btn_choose_random = Button(-1, -1, self.create_game, img=Images.RANDOM_CHOOSE, name=random_color, text=False)

        subwin = SubWindow('Choose color.', buttons=[btn_choose_white, btn_choose_black, btn_choose_random])
        self.subwindow = subwin

    def about(self):
        # TODO
        print('about')

    def exit(self):
        # TODO
        print('Take scissors and cut cable of computer :) It work, I promise.')

    def set_cursor(self, cur_x, cur_y):
        self.press_cur_x = cur_x
        self.press_cur_y = cur_y

    def check_on_click_in_btn(self):
        for btn in self.buttons:
            if btn.pos_x <= self.press_cur_x <= btn.pos_x + btn.width \
                    and btn.pos_y <= self.press_cur_y <= btn.pos_y + btn.height:
                btn.on_click = True
                btn.use()

