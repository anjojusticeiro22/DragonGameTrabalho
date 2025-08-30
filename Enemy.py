from Const import ENTITY_SPEED, Tela_A, ENTITY_SHOOT_DELAY
from EnemyShoot import EnemyShoot
from Entity import Entity


class Enemy(Entity):
    def __init__(self,name: str, position:tuple):
        super().__init__(name, position)
        self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]




    def move(self):
        self.rect.centery += ENTITY_SPEED[self.name]

    def shoot(self):
        self.shoot_delay -= 1
        if self.shoot_delay == 0:
            self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
            return EnemyShoot(name=f'{self.name}shoot', position=(self.rect.centerx, self.rect.centery+40))