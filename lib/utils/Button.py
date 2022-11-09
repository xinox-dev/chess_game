import pygame
from lib.utils.Images import Images


class Button:
    def __init__(self, pos_x, pos_y, function, name='Btn', img=Images.BTN_DEV, visible=True, text=True):
        self.name = name
        self.function = function
        self.img = img
        self.visible = visible
        self.pos_x, self.pos_y = pos_x, pos_y
        self.width, self.height = self.img.get_width(), self.img.get_height()
        self.on_click = False
        self.text = text

    def draw(self, window):
        window.blit(self.img, (self.pos_x, self.pos_y))
        if self.text:
            f = pygame.font.SysFont(None, 45)
            text = f.render(self.name, True, (255, 255, 255))
            window.blit(text, (self.pos_x+self.width/2-text.get_width()/2, self.pos_y+self.height/2-text.get_height()/2))
        # TODO add font to utils

    def set_visible(self,  boolean):
        self.visible = boolean

    def use(self, param=None):
        if self.on_click:
            if param:
                self.function(param)
            else:
                self.function()
            self.on_click = False
