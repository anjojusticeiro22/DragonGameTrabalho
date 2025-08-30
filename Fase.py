import random

import pygame
from pygame import Surface, Rect
from pygame.font import Font
from Const import C_VERMELHO, C_AMARELO, EVENT_ENEMY, SPAWN_ENEMY
from Enemy import Enemy
from Entity import Entity
from EntityFactory import EntityFactory
from EntityMediator import EntityMediator
from Player import Player


class Fase:
    def __init__(self, window, name):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Fase1_0'))
        self.entity_list.append(EntityFactory.get_entity('Play1'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_ENEMY)

    def run(self, ):
        pygame.mixer.init()
        som = pygame.mixer.Sound("asset/menu.wav")
        arr = pygame.sndarray.array(som)
        arr_fast = arr[::2].copy()
        som_rapido = pygame.sndarray.make_sound(arr_fast)
        som_rapido.play(loops=-1)
        self.som_rapido = som_rapido
        clock = pygame.time.Clock()
        while True:
            dt = clock.tick(60)
            for ent in self.entity_list:
                if hasattr(ent, "update"):
                    ent.update(dt)
                self.window.blit(ent.surf, ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                    if ent.name == 'Play1':
                        self.fase_text(28, f'Life : {ent.life}', C_VERMELHO, (260, 75))
                        self.fase_text(27, f'Life : {ent.life}', C_AMARELO, (260, 75))
                        self.fase_text(28, f'Score : {ent.score}', C_VERMELHO, (260, 100))
                        self.fase_text(27, f'Score : {ent.score}', C_AMARELO, (260, 100))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2', 'Enemy3'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.fase_text(29, f'{self.name}', C_VERMELHO, (272, 10))
            self.fase_text(29, f'Timeout: {self.timeout / 1000 :.1f}s', C_VERMELHO, (220, 40))
            self.fase_text(28, f'{self.name}', C_AMARELO, (274, 10))
            self.fase_text(28, f'Timeout: {self.timeout / 1000 :.1f}s', C_AMARELO, (222, 40))
            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_life(entity_list=self.entity_list)
        pass

    def fase_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Impact", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
