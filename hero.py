import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health  = 150
        self.attack_power = 15

    def attack(self):
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)

    def is_alive(self):
        return self.health > 0

    def battle_cry(self):
        if self.health > 110 and self.health <= 150:
            return "Your attack is a mere scar! I will defeat you!"
        
        elif self.health > 70 and self.health <= 110:
            return "You might have damaged me, but I am still strong!"

        elif self.health > 30 and self.health <= 70:
            return "Aagh! I have been deeply wounded, but I'm not dead yet!"

        elif self.health > 0 and self.health <= 30:
            return "AAGH!!! You dastardly devil! I will not be vanquished!"

        else:
            return "I have been defeated! Aagh..."