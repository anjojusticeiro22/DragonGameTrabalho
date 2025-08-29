import pygame
from Const import ENTITY_SPEED, Tela_A, Tela_L
from Entity import Entity

class Player(Entity):
    def __init__(self,nome: str, position:tuple):
        super().__init__(nome, position)
        self.frames = [
            pygame.image.load(f"asset/{nome}.png").convert_alpha(),
            pygame.image.load(f"asset/{nome}move2.png").convert_alpha(),
            pygame.image.load(f"asset/{nome}move3.png").convert_alpha()
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