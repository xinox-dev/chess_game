import pygame
from lib.utils.Images import Images


class Button:
    def __init__(self, pos_x, pos_y, function, name='Btn', img=Images.BTN_DEV, visible=True):
        self.pos_x, self.pos_y = pos_x, pos_y
        self.name = name
        self.function = function
        self.img = img
        self.visible = visible

    def draw(self, window):
        window.blit(self.img, (self.pos_x, self.pos_y))

    def set_visible(self,  boolean):
        self.visible = boolean

    def use(self):
        return self.function()
