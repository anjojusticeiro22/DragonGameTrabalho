import random
import pygame

from pygame import Surface, Rect
from pygame.font import Font

from game_code.Const import C_VERMELHO, C_AMARELO, EVENT_ENEMY, SPAWN_ENEMY, EVENT_TIMEOUT, TIME_STEP, TIMEOUT_LEVEL, TIME_SKIP
from game_code.Enemy import Enemy
from game_code.Entity import Entity
from game_code.EntityFactory import EntityFactory
from game_code.EntityMediator import EntityMediator
from game_code.Player import Player


class Fase:
    def __init__(self, window: Surface, name: str, player: Player, score_start=0,
                 spawn_time=SPAWN_ENEMY):
        self.som_rapido = None
        self.timeout = TIMEOUT_LEVEL  # tempo regressivo da fase
        self.window = window
        self.name = name
        self.start_score = score_start
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + '_0'))  # adiciona entidades iniciais
        self.entity_list.append(player)  # adiciona o jogador
        self.img_gameover = pygame.image.load("./asset/Gameover.png").convert_alpha()
        # configura timer para spawn de inimigos e tempo da fase
        pygame.time.set_timer(EVENT_ENEMY, spawn_time)
        pygame.time.set_timer(EVENT_TIMEOUT, TIME_STEP)

    # função que mostra a tela de Game Over
    def mostrar_gameover(self):
        rect = self.img_gameover.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2))
        self.window.blit(self.img_gameover, rect)
        pygame.display.flip()
        pygame.time.wait(3000)

    def run(self, player_score: list[int]):
        pygame.mixer.init()
        som = pygame.mixer.Sound("./asset/menu.wav")
        arr = pygame.sndarray.array(som)
        arr_fast = arr[::2].copy()   # deixa o som mais rápido
        som_rapido = pygame.sndarray.make_sound(arr_fast)
        som_rapido.play(loops=-1)
        self.som_rapido = som_rapido
        clock = pygame.time.Clock()

        while True:
            dt = clock.tick(60)  # controla o FPS da fase
            for ent in self.entity_list:
                if hasattr(ent, "update"):
                    ent.update(dt)
                self.window.blit(ent.surf, ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                    if ent.name == 'Play1':  # mostra vida e score do jogador
                        self.fase_text(28, f'Life : {ent.life}', C_VERMELHO, (246, 70))
                        self.fase_text(27, f'Life : {ent.life}', C_AMARELO, (248, 70))
                        self.fase_text(28, f'Score : {ent.score}', C_VERMELHO, (250, 98))
                        self.fase_text(27, f'Score : {ent.score}', C_AMARELO, (252, 98))

            # mostrar nome da fase e tempo restante
            self.fase_text(29, f'{self.name}', C_VERMELHO, (266, 10))
            self.fase_text(29, f'Timeout: {self.timeout / 1000 :.1f}s', C_VERMELHO, (220, 38))
            self.fase_text(28, f'{self.name}', C_AMARELO, (268, 10))
            self.fase_text(28, f'Timeout: {self.timeout / 1000 :.1f}s', C_AMARELO, (222, 38))
            self.fase_text(10, f'Entidades: {len(self.entity_list)}', C_AMARELO, (10, 10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY: # spawn de inimigos
                    choice = random.choice(('Enemy1', 'Enemy2', 'Enemy3'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIME_STEP

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player) and ent.name == "Play1":
                        found_player = True
                        # se o tempo zerar avança
                        if self.timeout <= TIME_SKIP:
                            player_score[0] = ent.score
                            self.som_rapido.stop()
                            return "completa"
                # se o jogador morrer game over
                if not found_player:
                    self.som_rapido.stop()
                    self.mostrar_gameover()
                    return "gameover"

            pygame.display.flip()

            # verifica colisões e vida das entidades
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_life(entity_list=self.entity_list)

    def fase_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Impact", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
