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
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OP[0]:
                player = EntityFactory.get_entity('Play1')
                player_score = [0]
                fase = Fase(self.window, 'Fase1', player, score_start=player_score[0], spawn_time=SPAWN_ENEMY)
                pygame.mixer.music.stop()
                fase_return = fase.run(player_score)
                if fase_return == 'completa':
                    fase = Fase(self.window, 'Fase2', player, score_start=player_score[0], spawn_time=SPAWN_ENEMY2)
                    fase_return = fase.run(player_score)
                    if fase_return == 'completa':
                        score.save(menu_return, player_score)
                    if fase_return == 'gameover':
                        continue
                elif fase_return == 'gameover':
                    continue
            if menu_return == MENU_OP[1]:
                score.show()

            elif menu_return == MENU_OP[2]:
                pygame.quit()
                quit()
            else:
                pass
