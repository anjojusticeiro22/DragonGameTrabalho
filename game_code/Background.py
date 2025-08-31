from game_code.Const import Tela_A, ENTITY_SPEED
from game_code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.y += ENTITY_SPEED[self.name]

        if self.rect.top >= Tela_A:
            self.rect.bottom = 0
        pass
