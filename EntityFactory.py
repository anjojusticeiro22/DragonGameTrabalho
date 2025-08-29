import random

from Background import Background
from Const import Tela_A, Tela_L
from Enemy import Enemy
from Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Fase1_0':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Fase1_0{i}',(0, 0)))
                    list_bg.append(Background(f'Fase1_0{i}', (0, Tela_A)))
                return list_bg
            case 'Play1':
                return Player('Play1', (250 , 700))
            case 'Enemy1':
                return Enemy('Enemy1', (random.randint(0,Tela_L-79),0-10,))
            case 'Enemy2':
                return Enemy('Enemy2', (random.randint(0,Tela_L-79),0-10,))
            case 'Enemy3':
                return Enemy('Enemy3', (random.randint(0,Tela_L-79),0-10,))
