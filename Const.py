import pygame

Tela_L=600
Tela_A=800

C_AMARELO=(255, 240, 15)
C_VERMELHO=(140, 8, 8)
C_LARANJA=(212, 84, 45)

EVENT_ENEMY = pygame.USEREVENT + 1

SPAWN_ENEMY = 2500

ENTITY_SPEED = {
    'Fase1_00': 0,
    'Fase1_01': 1,
    'Fase1_02': 2,
    'Fase1_03': 3,
    'Fase1_04': 4,
    'Play1' : 6,
    'Enemy1' : 2,
    'Enemy2': 1.7,
    'Enemy3': 1.8,

}

MENU_OP = ('NOVO JOGO',
           'SCORE',
           'EXIT')