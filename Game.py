
import pygame

from Menu import Menu
from Const import Tela_L, Tela_A

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(Tela_L, Tela_A))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass



