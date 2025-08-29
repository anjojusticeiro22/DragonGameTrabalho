from Const import ENTITY_SPEED
from Entity import Entity


class PlayerShoot(Entity):

    def __init__(self,name: str, position:tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centery -= ENTITY_SPEED[self.name]