from Enemy import Enemy
from EnemyShoot import EnemyShoot
from Entity import Entity
from PlayerShoot import PlayerShoot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.bottom < 0:
                ent.life = 0
            if isinstance(ent, PlayerShoot):
                if ent.rect.top < 0:
                    ent.life = 0
            if isinstance(ent, EnemyShoot):
                if ent.rect.bottom < 0:
                    ent.life = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_life(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.life <= 0:
                entity_list.remove(ent)
