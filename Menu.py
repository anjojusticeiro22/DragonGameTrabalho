import pygame.image
from pygame import Rect

from Const import Tela_L, C_VERMELHO, C_AMARELO, MENU_OP, C_LARANJA


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu1.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_op = 0
        pygame.mixer.music.load('asset/menu.wav')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(self.surf, self.rect)
            self.menu_text(102, "Dragon", C_VERMELHO, ((Tela_L / 2), 100))
            self.menu_text(102, "Adventure", C_VERMELHO, ((Tela_L / 2), 200))
            self.menu_text(100, "Dragon", C_LARANJA, ((Tela_L / 2), 100))
            self.menu_text(100, "Adventure", C_LARANJA, ((Tela_L / 2), 200))
            self.menu_text(98, "Dragon", C_AMARELO, ((Tela_L / 2), 100))
            self.menu_text(98, "Adventure", C_AMARELO, ((Tela_L / 2), 200))

            for i in range(len(MENU_OP)):
                if i == menu_op:
                    self.menu_text(54, MENU_OP[i], C_AMARELO, ((Tela_L / 2), 490 + 70 * i))
                    self.menu_text(52, MENU_OP[i], C_VERMELHO, ((Tela_L / 2), 490 + 70 * i))
                    self.menu_text(50, MENU_OP[i], C_LARANJA, ((Tela_L / 2), 490 + 70 * i))
                else:
                    self.menu_text(51, MENU_OP[i], C_VERMELHO, ((Tela_L / 2), 490 + 70 * i))
                    self.menu_text(49, MENU_OP[i], C_LARANJA, ((Tela_L / 2), 490 + 70 * i))
                    self.menu_text(47, MENU_OP[i], C_AMARELO, ((Tela_L / 2), 490 + 70 * i))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_op < len(MENU_OP) - 1:
                            menu_op += 1
                        else:
                            menu_op = 0
                    if event.key == pygame.K_UP:
                        if menu_op > 0:
                            menu_op -= 1
                        else:
                            menu_op = len(MENU_OP) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OP[menu_op]

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Burn", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
