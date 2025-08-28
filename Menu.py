import pygame.image
from pygame import Rect

from Const import Tela_L, C_VERMELHO, C_AMARELO, MENU_OP


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu1.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer.music.load('asset/music/menu.wav')
        pygame.mixer_music.play(-1)
        self.window.blit(self.surf, self.rect)
        while True:
            self.menu_text(101, "Dragon", C_VERMELHO, ((Tela_L / 2), 100))
            self.menu_text(101, "Adventure", C_VERMELHO, ((Tela_L / 2), 200))
            self.menu_text(98, "Dragon", C_AMARELO, ((Tela_L / 2), 100))
            self.menu_text(98, "Adventure", C_AMARELO, ((Tela_L / 2), 200))

            for i in range(len(MENU_OP)):
                self.menu_text(51, MENU_OP[i], C_VERMELHO, ((Tela_L / 2), 490 + 70 * i))
                self.menu_text(48, MENU_OP[i], C_AMARELO, ((Tela_L / 2), 490 + 70 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Burn", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
