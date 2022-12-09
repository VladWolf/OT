import settings as constant
from random import randint
import exceptions as exception


class Enemy:
    def __init__(self, level = constant.STARTING_LVL):
        self.level = level
        self.health_points = level

    def decrease_health(self):
        self.health_points -= 1
        if self.health_points == 0:
            raise exception.EnemyDown

    def select(self):
        return constant.CHOICES[randint(0, 2)]


class Player:
    def __init__(self, name):
        self.name = name
        self.health_poitns = constant.PLAYER_HEALTH
        self.score = constant.STARTING_SCORE
    
    def decrease_health(self):
        self.health_poitns -= 1
        if self.health_poitns == 0:
            raise exception.GameOver
    
    def select(self):
        choice = 0
        while choice not in (1, 2, 3):
            try:
                choice = int(input("Warrior-1, Robber-2, Wizard-3: "))
                if 1 > choice or choice > 3:
                    print("Enter 1 or 2 or 3")
            except ValueError:
                print("Enter an integer")
        return constant.CHOICES[choice-1]

    @staticmethod
    def fight(player, bot):
        """0 - player victory, 1 - bot victory, 2 - draw"""
        if player == bot:
            return 2
        else:
            return 0 if (player, bot) in list(zip(constant.CHOICES, constant.ENEEMY_LIST)) else 1
 

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
