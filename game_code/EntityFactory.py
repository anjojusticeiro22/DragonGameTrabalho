import random

from game_code.Background import Background
from game_code.Const import Tela_A, Tela_L
from game_code.Enemy import Enemy
from game_code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, ):
        match entity_name:
            case 'Fase1_0':
                # Cria uma lista de fundos para a fase 1
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Fase1_0{i}', (0, 0)))
                    list_bg.append(Background(f'Fase1_0{i}', (0, Tela_A)))
                return list_bg
            case 'Fase2_0':
                # Cria uma lista de fundos para a fase 2
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Fase2_0{i}', (0, 0)))
                    list_bg.append(Background(f'Fase2_0{i}', (0, Tela_A)))
                return list_bg
            case 'Play1':
                # Cria o jogador
                return Player('Play1', (250, 700))
         # Cria inimigos
            case 'Enemy1':
                return Enemy('Enemy1', (random.randint(0, Tela_L - 79), 0 - 80,))
            case 'Enemy2':
                return Enemy('Enemy2', (random.randint(0, Tela_L - 79), 0 - 80,))
            case 'Enemy3':
                return Enemy('Enemy3', (random.randint(0, Tela_L - 79), 0 - 80,))
        return None
