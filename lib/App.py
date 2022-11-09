import pygame
from lib.screen.Game import Game
from lib.screen.Menu import Menu
from lib.utils.Constants import Constants

class App:
    def __init__(self):
        self.window = pygame.display.set_mode((1200, 800))
        self.fps = pygame.time.Clock().tick
        self.game = Game(Constants.WHITE)
        self.menu = Menu(fun_create_game=self.create_game)
        self.app_runs = True
        self.menu_active = True

    def run_app(self):
        pygame.init()
        while self.app_runs:
            self.fps(60)
            self.check_event(pygame.event.get())
            self.game.draw(self.window)
            self.menu.draw(self.window)
            pygame.display.update()

    def check_event(self, events):
        for e in events:
            if e.type == pygame.QUIT:
                self.app_runs = False
            if e.type == pygame.MOUSEBUTTONUP:
                cursor_x, cursor_y = pygame.mouse.get_pos()
                if not self.menu_active:
                    self.game.action(cursor_x, cursor_y)
                self.menu.action(cursor_x, cursor_y)

    def create_game(self, color):
        self.game = Game(color)
        self.menu.subwindow = None

