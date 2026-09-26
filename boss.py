from enemy import Enemy


class Boss(Enemy):
    """A stronger enemy with a powered-up attack."""

    def __init__(self, name):
        super().__init__(name, health=300, attack_power=25)

    def attack(self):
        damage = super().attack()
        bonus_damage = 10
        print(f"{self.name} unleashes a crushing blow!")
        return damage + bonus_damage