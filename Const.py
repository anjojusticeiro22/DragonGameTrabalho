import pygame

Tela_L = 600
Tela_A = 800

C_AMARELO = (255, 240, 15)
C_VERMELHO = (140, 8, 8)
C_LARANJA = (212, 84, 45)

EVENT_ENEMY = pygame.USEREVENT + 1

SPAWN_ENEMY = 2500

ENTITY_SPEED = {
    'Fase1_00': 0,
    'Fase1_01': 1,
    'Fase1_02': 2,
    'Fase1_03': 3,
    'Fase1_04': 4,
    'Play1': 4,
    'Enemy1': 2,
    'Enemy2': 1.7,
    'Enemy3': 1.8,
    'Play1shoot': 3,
    'Enemy1shoot': 4,
    'Enemy2shoot': 4,
    'Enemy3shoot': 4,
}

ENTITY_SHOT_DELAY = {
    'Play1' : 20,
    'Enemy1' : 100,
    'Enemy2' : 100,
    'Enemy3' : 100,

}

ENTITY_LIFE = {
    'Fase1_00': 999,
    'Fase1_01': 999,
    'Fase1_02': 999,
    'Fase1_03': 999,
    'Fase1_04': 999,
    'Play1': 300,
    'Play1shoot': 1,
    'Enemy1': 50,
    'Enemy2': 50,
    'Enemy3': 50,
    'Enemy1shoot': 1,
    'Enemy2shoot': 1,
    'Enemy3shoot': 1,
}

MENU_OP = ('NOVO JOGO',
           'SCORE',
           'EXIT')
