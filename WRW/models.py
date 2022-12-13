import settings as constant
from random import choice
import exceptions as exception


class Enemy:
    def __init__(self, level=1):
        self.level = level
        self.health_points = level

    @classmethod
    def level_up(cls, enemy):
        return cls(enemy.level+1)

    def decrease_health(self):
        self.health_points -= 1
        if self.health_points <= 0:
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
        if self.health_poitns <= 0:
            raise exception.GameOverError(self.name, self.score)
    
    def select(self):
        while True:
            try:
                choice = int(input("Warrior-1, Robber-2, Wizard-3: "))
                if 1 > choice or choice > 3:
                    print("Enter 1 or 2 or 3")
                else:
                    break
            except ValueError:
                print("Enter an integer")
        return constant.CHOICES[choice-1]

    @staticmethod
    def fight(player, bot):
        """0 - player victory, 1 - bot victory, 2 - draw"""
        if player == bot:
            return 2
        else:
            return 0 if (player, bot) in list(zip(constant.CHOICES, ('Robber', 'Wizard', 'Warrior'))) else 1
 

    def attack(self, enemy):
        result = self.fight(self.select(), enemy.select())
        print(constant.ATTACK_RESULT[result])

        if result == 0:
            self.score += 1
            enemy.decrease_health()

    def defence(self, enemy):
        result = self.fight(enemy.select(), self.select())
        print(constant.DEFENCE_RESULT[result])

        if result == 1:
            self.decrease_health()
