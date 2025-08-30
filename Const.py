import pygame

Tela_L = 600
Tela_A = 800

C_AMARELO = (255, 240, 15)
C_VERMELHO = (140, 8, 8)
C_LARANJA = (212, 84, 45)



EVENT_ENEMY = pygame.USEREVENT + 1

SPAWN_ENEMY = 2000

ENTITY_SPEED = {
    'Fase1_00': 0,
    'Fase1_01': 1,
    'Fase1_02': 2,
    'Fase1_03': 3,
    'Fase1_04': 4,
    'Play1': 5,
    'Enemy1': 2,
    'Enemy2': 1.7,
    'Enemy3': 1.8,
    'Play1shoot': 5,
    'Enemy1shoot': 4,
    'Enemy2shoot': 4,
    'Enemy3shoot': 4,
}

ENTITY_DANO = {
    'Fase1_00': 0,
    'Fase1_01': 0,
    'Fase1_02': 0,
    'Fase1_03': 0,
    'Fase1_04': 0,
    'Play1': 1,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 1,
    'Play1shoot': 30,
    'Enemy1shoot': 20,
    'Enemy2shoot': 20,
    'Enemy3shoot': 20,
}

ENTITY_SCORE = {
    'Fase1_00': 0,
    'Fase1_01': 0,
    'Fase1_02': 0,
    'Fase1_03': 0,
    'Fase1_04': 0,
    'Play1': 0,
    'Enemy1': 10,
    'Enemy2': 10,
    'Enemy3': 10,
    'Play1shoot': 0,
    'Enemy1shoot': 0,
    'Enemy2shoot': 0,
    'Enemy3shoot': 0,
}

ENTITY_SHOOT_DELAY = {
    'Play1': 40,
    'Enemy1': 80,
    'Enemy2': 80,
    'Enemy3': 80,

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
