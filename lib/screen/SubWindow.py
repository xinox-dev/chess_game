import pygame
from lib.utils.Images import Images


class SubWindow:
    def __init__(self, title="Title", desc=None, buttons=None, layout_row=True):
        self.title = title
        self.desc = desc
        self.layout_row = layout_row
        self.pos_x, self.pos_y = 100, 150
        self.width, self.height = 700, 400
        self.press_cur_x, self.press_cur_y = -1, -1
        self.bg_image = Images.BTN_DEV
        self.buttons = self.set_buttons(buttons)

    def draw(self, window):
        window.blit(self.bg_image, (self.pos_x, self.pos_y))
        if self.buttons:
            self.draw_buttons(window)
        if self.desc:
            pass
            # TODO

    def action(self, cur_x, cur_y):
        self.set_cursor(cur_x, cur_y)
        self.check_on_click_in_btn()

    def draw_buttons(self, window):
        for i, btn in enumerate(self.buttons):
            btn.draw(window)

    def set_buttons(self, buttons):
        for i, btn in enumerate(buttons):
            btn.pos_x = self.pos_x + self.width/2 - (btn.width * len(buttons) + 50)/2 + i*(btn.width+50)
            btn.pos_y = self.pos_y + self.height/2 - btn.height/2

        return buttons

    def check_on_click_in_btn(self):
        for btn in self.buttons:
            if btn.pos_x <= self.press_cur_x <= btn.pos_x + btn.width \
                    and btn.pos_y <= self.press_cur_y <= btn.pos_y + btn.height:
                btn.on_click = True
                btn.use(btn.name)

    def set_cursor(self, cur_x, cur_y):
        self.press_cur_x = cur_x
        self.press_cur_y = cur_y
