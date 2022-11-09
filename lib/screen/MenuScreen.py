import pygame
from lib.utils.Button import Button


class MenuScreen:
    def __init__(self):
        self.is_on = True
        self.b_color = (0, 0, 0)
        self.pos_fields_x, self.pos_fields_y = 1000, 500
        self.fields = [
            {
                'name': 'New Game',
                'action': self.newgame()
            },
            {
                'name': 'About',
                'action': self.about()
            },
            {
                'name': 'Exit',
                'action': self.exit()
            }
        ]
        self.buttons = self.create_menu_buttons()

    def draw_menu(self, window):
        window.fill(self.b_color)
        for btn in self.buttons:
            btn.draw(window)

    def create_menu_buttons(self):
        buttons = []
        for i, field in enumerate(self.fields):
            btn = Button(self.pos_fields_x, self.pos_fields_y + i * 70, function=field['action'], name=field['name'])
            buttons.append(btn)
        return buttons

    def newgame(self):
        # TODO
        print('newgame')

    def about(self):
        # TODO
        print('about')

    def exit(self):
        # TODO
        print('Take scissors and cut cable of computer :) It work, I promise.')

