import pygame.image
from pygame import Rect, Surface
from pygame.font import Font

from game_code.Const import Tela_L, C_VERMELHO, C_AMARELO, MENU_OP, C_LARANJA


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu1.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.font_burn = "./asset/Burn.otf"

    def run(self, ):
        menu_op = 0  # índice da opção do menu selecionada
        pygame.mixer.music.load('./asset/menu.wav')
        pygame.mixer.music.play(-1)  # tocar música em loop

        while True:
            # desenhar fundo e título
            self.window.blit(self.surf, self.rect)
            self.menu_text(102, "Dragon", C_VERMELHO, ((Tela_L / 2), 100))
            self.menu_text(102, "Adventure", C_VERMELHO, ((Tela_L / 2), 200))
            self.menu_text(100, "Dragon", C_LARANJA, ((Tela_L / 2), 100))
            self.menu_text(100, "Adventure", C_LARANJA, ((Tela_L / 2), 200))
            self.menu_text(98, "Dragon", C_AMARELO, ((Tela_L / 2), 100))
            self.menu_text(98, "Adventure", C_AMARELO, ((Tela_L / 2), 200))

            for i in range(len(MENU_OP)):
                if i == menu_op:
                    # opção selecionada com cores diferentes (3 para dar um efeito)
                    self.menu_text(54, MENU_OP[i], C_AMARELO, ((Tela_L / 2), 490 + 70 * i))
                    self.menu_text(52, MENU_OP[i], C_VERMELHO, ((Tela_L / 2), 490 + 70 * i))
                    self.menu_text(50, MENU_OP[i], C_LARANJA, ((Tela_L / 2), 490 + 70 * i))
                else:
                    self.menu_text(51, MENU_OP[i], C_VERMELHO, ((Tela_L / 2), 490 + 70 * i))
                    self.menu_text(49, MENU_OP[i], C_LARANJA, ((Tela_L / 2), 490 + 70 * i))
                    self.menu_text(47, MENU_OP[i], C_AMARELO, ((Tela_L / 2), 490 + 70 * i))

            # verificar eventos do teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    # mover para cima e para baixo no menu
                    if event.key == pygame.K_DOWN:
                        menu_op = (menu_op + 1) % len(MENU_OP)
                    elif event.key == pygame.K_UP:
                        menu_op = (menu_op - 1) % len(MENU_OP)
                    elif event.key == pygame.K_RETURN:
                        return MENU_OP[menu_op]

            pygame.display.flip()  # atualizar a tela

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.Font(self.font_burn, text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
