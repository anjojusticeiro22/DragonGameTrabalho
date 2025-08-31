import pygame

from game_code.Const import ENTITY_SPEED, Tela_A, Tela_L, ENTITY_SHOOT_DELAY
from game_code.Entity import Entity
from game_code.PlayerShoot import PlayerShoot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.last_shot_time = 0
        # tempo de atraso entre os tiros
        self.shoot_delay = ENTITY_SHOOT_DELAY[self.name] * (1000// 60)
        # lista de imagens do player para fazer a animação
        self.frames = [
            pygame.image.load(f"asset/{name}.png").convert_alpha(),
            pygame.image.load(f"asset/{name}move2.png").convert_alpha(),
            pygame.image.load(f"asset/{name}move3.png").convert_alpha()
        ]
        # controle da animação do personagem
        self.frame_index = 0
        self.frame_timer = 0
        self.frame_delay = 150

    def update(self, dt):
        # acumula o tempo que passou
        self.frame_timer += dt
        # quando passa do tempo definido o frame é trocado
        if self.frame_timer >= self.frame_delay:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.surf = self.frames[self.frame_index]

    def move(self):
        # verifica quais teclas estão pressionadas e aplica movimento
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < Tela_A:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right < Tela_L:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

    def shoot(self):
        #tiro baseado em (ms)
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_delay:
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_SPACE]:
                self.last_shot_time = current_time
                return PlayerShoot(
                    name=f'{self.name}shoot',
                    position=(self.rect.centerx, self.rect.centery - 60)
                )
        return None