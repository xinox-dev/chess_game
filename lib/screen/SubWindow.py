import pygame
from lib.utils.Images import Images
from lib.utils.Constants import Constants
from lib.utils.Button import Button


class SubWindow:
    def __init__(self, close_functon, title="Title", desc=None, buttons=None, layout_row=True):
        self.title = title
        self.desc = desc
        self.layout_row = layout_row
        self.pos_x, self.pos_y = 70, 150
        self.width, self.height = 700, 400
        self.press_cur_x, self.press_cur_y = -1, -1
        self.bg_image = Images.SUBWIN_BG
        self.buttons = self.set_buttons(buttons)
        self.close_btn = Button(self.pos_x + self.width - 50, self.pos_y,
                                function=close_functon, img=Images.CLOSE, text=False)

    def draw(self, window):
        # draw bg image
        window.blit(self.bg_image, (self.pos_x, self.pos_y))
        # draw title
        self.draw_title(window)
        # draw buttons - optional
        if self.buttons:
            self.draw_buttons(window)
        # draw description - optional
        if self.desc:
            self.draw_desc(window)
        # draw close button
        self.close_btn.draw(window)

    def action(self, cur_x, cur_y):
        self.set_cursor(cur_x, cur_y)
        self.check_on_click_in_btn()

    def draw_buttons(self, window):
        for i, btn in enumerate(self.buttons):
            btn.draw(window)

    def draw_title(self, window):
        font = pygame.font.SysFont(None, 60)
        text = font.render(self.title, True, Constants.GREY_10)
        window.blit(text, (self.pos_x + self.width/2 - text.get_width()/2, self.pos_y + 40))

    def draw_desc(self, window):
        if self.desc:
            font = pygame.font.SysFont(None, 25)
            text = font.render(self.desc, True, Constants.GREY_10)
            w, h = text.get_size()
            window.blit(text, (self.pos_x + self.width / 2 - w / 2, self.pos_y + self.height / 2 - h / 2))

    def set_buttons(self, buttons):
        if buttons:
            for i, btn in enumerate(buttons):
                le = len(buttons)
                w, h = btn.width, btn.height
                btn.pos_x = self.pos_x + self.width / 2 - (w * le + (50 * (le - 1))) / 2 + i * (w + 50)
                btn.pos_y = self.pos_y + self.height / 2 - h / 2

            return buttons
        else:
            return None

    def check_on_click_in_btn(self):
        if self.buttons:
            for btn in self.buttons:
                if btn.pos_x <= self.press_cur_x <= btn.pos_x + btn.width \
                        and btn.pos_y <= self.press_cur_y <= btn.pos_y + btn.height:
                    btn.on_click = True
                    btn.use(btn.name)
        if self.close_btn.pos_x <= self.press_cur_x <= self.close_btn.pos_x + self.close_btn.width \
                and self.close_btn.pos_y <= self.press_cur_y <= self.close_btn.pos_y + self.close_btn.height:
            self.close_btn.on_click = True
            self.close_btn.use()

    def set_cursor(self, cur_x, cur_y):
        self.press_cur_x = cur_x
        self.press_cur_y = cur_y

