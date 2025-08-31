import pygame

from game_code.Fase import Fase
from game_code.Menu import Menu
from game_code.Const import Tela_L, Tela_A, MENU_OP, SPAWN_ENEMY, SPAWN_ENEMY2
from game_code.EntityFactory import EntityFactory
from game_code.Score  import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(Tela_L, Tela_A))

    def run(self):
        while True:
            score = Score(self.window)  # cria tela de score
            menu = Menu(self.window)  # cria menu
            menu_return = menu.run()

            if menu_return == MENU_OP[0]:
                player = EntityFactory.get_entity('Play1')
                player_score = [0]
                # cria fase 1, usando tempo de spawn definido em SPAWN_ENEMY
                fase = Fase(self.window, 'Fase1', player, score_start=player_score[0], spawn_time=SPAWN_ENEMY)
                pygame.mixer.music.stop()
                fase_return = fase.run(player_score)
                if fase_return == 'completa':
                    # se fase 1 for completa, cria fase 2 com spawn mais rápido (SPAWN_ENEMY2)
                    fase = Fase(self.window, 'Fase2', player, score_start=player_score[0], spawn_time=SPAWN_ENEMY2)
                    fase_return = fase.run(player_score)
                    if fase_return == 'completa':
                        score.save(menu_return, player_score)
                    if fase_return == 'gameover':
                        continue
                elif fase_return == 'gameover':
                    continue
            # se escolher "Ver Scores"
            if menu_return == MENU_OP[1]:
                score.show() # mostra tabela de scores

            # se escolher "Sair"
            elif menu_return == MENU_OP[2]:
                pygame.quit()
                quit()
            else:
                pass
