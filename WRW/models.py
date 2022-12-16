import settings as constant
from random import choice
import exceptions as exception


class Enemy:
    def __init__(self, level=1):
        self.level = level
        self.health_points = level

    @classmethod
    def level_up(cls, enemy):
        return cls(enemy.level + 1)

    def decrease_health(self):
        self.health_points -= 1
        if self.health_points < 1:
            raise exception.EnemyDownError(self.level)

    def select(self):
        return choice(constant.CHOICES)
    

class Player:
    def __init__(self, name):
        self.name = name
        self.health_poitns = constant.PLAYER_HEALTH
        self.score = constant.STARTING_SCORE
    
    def decrease_health(self):
        self.health_poitns -= 1
        if self.health_poitns < 1:
            raise exception.GameOverError(self)
    
    def select(self):
        while True:
            try:
                choice = int(input("Warrior-1, Robber-2, Wizard-3: "))
                if 0 < choice <= 3:
                    break
                else:
                    print("Enter 1 or 2 or 3")
            except ValueError:
                print("Enter an integer")
        return constant.CHOICES[choice-1]

    @staticmethod
    def fight(attacker, defender, turn):
        if attacker == defender:
            return constant.RESULT_LST[0]
        elif (attacker, defender) in constant.RESULT_DICT.items():
            return constant.RESULT_LST[1] if isinstance(turn, Player) else constant.RESULT_LST[2]
        else:
            return constant.RESULT_LST[3] if isinstance(turn, Player) else constant.RESULT_LST[4]

    def attack(self, enemy):
        result = self.fight(self.select(), enemy.select(), self)
        print(result)

        if result == constant.RESULT_LST[1]:
            self.score += 1
            enemy.decrease_health()

    def defence(self, enemy):
        result = self.fight(enemy.select(), self.select(), enemy)
        print(result)

        if result == constant.RESULT_LST[2]:
            self.decrease_health()
