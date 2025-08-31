import pygame

# C
C_AMARELO = (255, 240, 15)
C_VERMELHO = (140, 8, 8)
C_LARANJA = (212, 84, 45)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Fase1_00': 0,
    'Fase1_01': 1,
    'Fase1_02': 2,
    'Fase1_03': 3,
    'Fase1_04': 4,
    'Fase2_00': 0,
    'Fase2_01': 1,
    'Fase2_02': 2,
    'Fase2_03': 3,
    'Fase2_04': 4,
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
    'Fase2_00': 0,
    'Fase2_01': 0,
    'Fase2_02': 0,
    'Fase2_03': 0,
    'Fase2_04': 0,
    'Play1': 1,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 1,
    'Play1shoot': 300,
    'Enemy1shoot': 300,
    'Enemy2shoot': 300,
    'Enemy3shoot': 300,
}
ENTITY_SCORE = {
    'Fase1_00': 0,
    'Fase1_01': 0,
    'Fase1_02': 0,
    'Fase1_03': 0,
    'Fase1_04': 0,
    'Fase2_00': 0,
    'Fase2_01': 0,
    'Fase2_02': 0,
    'Fase2_03': 0,
    'Fase2_04': 0,
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
    'Fase1_00': 9999,
    'Fase1_01': 9999,
    'Fase1_02': 9999,
    'Fase1_03': 9999,
    'Fase1_04': 9999,
    'Fase2_00': 9999,
    'Fase2_01': 9999,
    'Fase2_02': 9999,
    'Fase2_03': 9999,
    'Fase2_04': 9999,
    'Play1': 3000,
    'Play1shoot': 1,
    'Enemy1': 500,
    'Enemy2': 500,
    'Enemy3': 500,
    'Enemy1shoot': 1,
    'Enemy2shoot': 1,
    'Enemy3shoot': 1,
}

# M
MENU_OP = ('NOVO JOGO',
           'SCORE',
           'EXIT')

# S
SPAWN_ENEMY = 1500
SPAWN_ENEMY2 = 800
SCORE_POS = {
    'Title': (175, 200),
    'EnterName': (80, 350),
    'Name': (222, 400),
    'Label': (110, 300),
    0: (115, 400),
    1: (115, 440),
    2: (115, 480),
    3: (115, 520),
    4: (115, 560),
}

# T
Tela_L = 600
Tela_A = 800
TIME_SKIP = 0
TIME_STEP = 100
TIMEOUT_LEVEL = 10000
