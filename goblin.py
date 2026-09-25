import random
from enemy import Enemy

class Goblin(Enemy):

    def __init__(self, name):
        super().__init__(name, 100, 7)
        self.gold = 0

    def stealGold(self, hero):
        print("Give me the Bread!")
        self.gold = self.gold + hero.gold
        hero.gold = 0