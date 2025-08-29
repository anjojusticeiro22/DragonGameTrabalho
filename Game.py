import pygame

from Fase import Fase
from Menu import Menu
from Const import Tela_L, Tela_A, MENU_OP


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(Tela_L, Tela_A))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OP[0]:
                fase = Fase(self.window, 'Level 1')
                pygame.mixer.music.stop()
                fase_return = fase.run()

            elif menu_return == MENU_OP[2]:
                pygame.quit()
                quit()
            else :
                pass




