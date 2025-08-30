from Enemy import Enemy
from EnemyShoot import EnemyShoot
from Entity import Entity
from Player import Player
from PlayerShoot import PlayerShoot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.bottom <= 0:
                ent.life = 0
            if isinstance(ent, PlayerShoot):
                if ent.rect.top <= 0:
                    ent.life = 0
            if isinstance(ent, EnemyShoot):
                if ent.rect.bottom <= 0:
                    ent.life = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShoot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShoot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShoot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShoot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.top <= ent2.rect.bottom and
                    ent1.rect.bottom >= ent2.rect.top):
                ent1.life -= ent2.dano
                ent2.life -= ent1.dano
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Play1shoot':
            for ent in entity_list:
                if ent.name == 'Play1':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_life(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.life <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
