import pygame
from Const import ENTITY_SPEED, Tela_A, Tela_L, ENTITY_SHOT_DELAY
from Entity import Entity
from PlayerShoot import PlayerShoot


class Player(Entity):
    def __init__(self,name: str, position:tuple):
        super().__init__(name, position)
        self.shoot_delay = ENTITY_SHOT_DELAY[self.name]
        self.frames = [
            pygame.image.load(f"asset/{name}.png").convert_alpha(),
            pygame.image.load(f"asset/{name}move2.png").convert_alpha(),
            pygame.image.load(f"asset/{name}move3.png").convert_alpha()
        ]
        self.frame_index = 0
        self.frame_timer = 0
        self.frame_delay = 150

    def update(self, dt):
        self.frame_timer += dt
        if self.frame_timer >= self.frame_delay:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.surf = self.frames[self.frame_index]



    def move(self):
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
        self.shoot_delay -= 1
        if self.shoot_delay == 0:
            self.shoot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_SPACE]:
               return PlayerShoot(name=f'{self.name}shoot', position=(self.rect.centerx, self.rect.centery))

