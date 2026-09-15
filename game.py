from goblin import Goblin
from hero import Hero
import time

ARENA_NAME = "The Golden Triangle"

def battle(protag, antag):
    round = 1

    if protag.is_alive() and antag.is_alive():
        living = True
    else:
        living = False

    while living:
    
        print()
        time.sleep(1)
        print(f"{protag.name} battles {antag.name} - ROUND {round}")
        time.sleep(1)
        print()

        for i in range(1):
            print(f"\r{protag.name} is attacking", end="")
            time.sleep(0.5)
            print(f"\r{protag.name} is attacking.", end="")
            time.sleep(0.5)
            print(f"\r{protag.name} is attacking..", end="")
            time.sleep(0.5)
            print(f"\r{protag.name} is attacking...", end="")
            time.sleep(0.5)
        print()
        
        attack = protag.attack()
        antag.take_damage(attack)
        print(f"{protag.name} attacks {antag.name} and deals {attack} damage! {antag.name} has {antag.health} health remaining.")

        if antag.is_alive():
            print()
            for i in range(1):
                print(f"\r{antag.name} is attacking", end="")
                time.sleep(0.5)
                print(f"\r{antag.name} is attacking.", end="")
                time.sleep(0.5)
                print(f"\r{antag.name} is attacking..", end="")
                time.sleep(0.5)
                print(f"\r{antag.name} is attacking...", end="")
                time.sleep(0.5)
            print()

            attack = antag.attack()
            protag.take_damage(attack)
            print(f"{antag.name} attacks {protag.name} and deals {attack} damage! {protag.name} has {protag.health} health remaining.")
            print(f"{protag.name} - '{protag.battle_cry()}'")

        round += 1
        time.sleep(2)

        if protag.is_alive() and antag.is_alive():
            living = True
        else:
            if not protag.is_alive():
                print()
                print(f"{protag.name} has been defeated by {antag.name}!")
            elif not antag.is_alive():
                print()
                print(f"{antag.name} has been defeated by {protag.name}!")
            
            living = False

def main():
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

    battle(hero, goblin)

if __name__ == "__main__":
    main()