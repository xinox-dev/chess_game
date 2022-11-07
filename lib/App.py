import pygame
from lib.screen.GameScreen import GameScreen


class App:
    def __init__(self):
        self.window = pygame.display.set_mode((1200, 800))
        self.fps = pygame.time.Clock().tick
        self.game = GameScreen()
        self.app_runs = True

    def run_app(self):
        pygame.init()
        while self.app_runs:
            self.fps(60)
            self.check_event(pygame.event.get())

            self.game.draw_screen(self.window)
            pygame.display.update()

    def check_event(self, events):
        for e in events:
            if e.type == pygame.QUIT:
                self.app_runs = False
            if e.type == pygame.MOUSEBUTTONUP:
                cursor_x, cursor_y = pygame.mouse.get_pos()
                self.game.action(cursor_x, cursor_y)
