from Const import ENTITY_SPEED, Tela_A
from Entity import Entity


class Enemy(Entity):
    def __init__(self,nome: str, position:tuple):
        super().__init__(nome, position)




    def move(self):
        self.rect.y += ENTITY_SPEED[self.name]
        if self.rect.top >= Tela_A:
            self.rect.bottom = 0