from code.Menu import Menu

import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(480, 600))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass



