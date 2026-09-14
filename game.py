from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Golden Triangle"

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")
    print()

    goblin = Goblin("Prapple")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblin2 = Goblin("Ploop")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")

    hero = Hero("Mateo")
    print(f"{hero.name} enters the arena with {hero.health} health.")

    print()
    attack = hero.attack()
    goblin.take_damage(attack)
    print(f"{hero.name} attacks {goblin.name} and deals {attack} damage! {goblin.name} has {goblin.health} health remaining.")

    if goblin.is_alive != True:
        print()
        attack = goblin.attack()
        hero.take_damage(attack)
        print(f"{goblin.name} attacks {hero.name} and deals {attack} damage! {hero.name} has {hero.health} health remaining.")
        print(f"{hero.name} - '{hero.battle_cry()}'")

if __name__ == "__main__":
    main()