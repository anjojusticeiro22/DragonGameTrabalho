from abc import ABC, abstractmethod

import pygame.image

from game_code.Const import ENTITY_LIFE, ENTITY_DANO, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.life = ENTITY_LIFE[self.name]
        self.dano = ENTITY_DANO[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

    @abstractmethod
    def move(self, ):
        pass
