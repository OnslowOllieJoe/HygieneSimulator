##
# Name: Ollie Joe
# Date: 07/06/022
# Description: RPG battle simulator which teaches dental hygiene.

import random
from time import sleep

# Constants
MAX_HP = 100
SEPARATOR = "-" * 40
SPACE_LENGTH = 13
weaken_weapons = [
               ["Toothbrush", 25],
               ["Dental Floss", 25],
               ["Mouthwash", 25]
               ]
kill_weapons = [
             ["Dental Scaler", 1],
             ["Filling", 1],
             ]


class characters():
    def __init__(self, type, health, base_dmg, money):
        self.type = type
        self.health = health
        self.base_dmg = base_dmg
        self.money = money


def user_info():
    print(f"{SEPARATOR}\n")
    print("              Player:\n")
    print(f"    Health:           {player.health}/{MAX_HP} HP")
    print(f"    Wallet:           ${player.money}")
    print("\n    Main Weapons:")
    for count, value in enumerate(weaken_weapons, start=1):
        sleep(0.2)
        print(f"      {count}: " + value[0])
    sleep(0.5)
    print("\n    Finishing Weapons:")
    for count, value in enumerate(kill_weapons, start=1):
        sleep(0.2)
        print(f"      {count}: " + value[0])


def enemy_info():
    print(f"\n{SEPARATOR}\n")
    sleep(1)
    print("              Enemies:\n")
    for count, i in enumerate(range(len(enemies_list)), start=1):
        sleep(0.5)
        print(f"    {count}: {enemies_list[i].type} " +
              (" " * (SPACE_LENGTH - (len(enemies_list[i].type)))) +
              f"{str(enemies_list[i].health)}/{MAX_HP} HP")
    sleep(0.5)
    print("\n" + SEPARATOR + "\n")


def weapon_selection():
    print("\n" + SEPARATOR)
    while True:
        sleep(0.5)
        try:
            print("\n    Main Weapons:")
            for count, value in enumerate(weaken_weapons, start=1):
                print(f"    {count}: " + value[0])
            print("\n" + SEPARATOR)
            chosen_weapon = int(input("\nEnter a number " +
                                      "to select a weapon : "))
            if chosen_weapon in range(1, len(weaken_weapons) + 1):
                print(f"You have chosen " +
                      f"{weaken_weapons[chosen_weapon - 1][0]}!")
                print("\n" + SEPARATOR)
                return chosen_weapon - 1
            else:
                print("Please enter a number from {} to {}."
                      .format(1, len(weaken_weapons)))
                print("Sorry, that is not a valid choice.")
        except Exception:
            print("Sorry, that is not a valid choice.")
            print("\n" + SEPARATOR + "\n")


def chosen_enemy():
    sleep(0.5)
    while True:
        try:
            target_enemy = int(input("Select an enemy's number to attack: "))
            if target_enemy in range(1, len(enemies_list) + 1):
                print(f"You have chosen enemy {target_enemy}, " +
                      f"{enemies_list[target_enemy-1].type}!")
                return target_enemy - 1
            else:
                print(f"Please enter a number from {1} to " +
                      f"{len(enemies_list)}.")
                enemy_info()
        except ValueError:
            print(f"Please enter a number from {1} to " +
                  f"{len(enemies_list)}.")
            enemy_info()


player = characters("Player", 100, 0, 0)
plaque = characters("Plaque", 100, 3, 0)
tartar = characters("Tartar", 100, 3, 0)
tooth_decay = characters("Tooth Decay", 100, 3, 0)
enemies_list = [plaque,
                tartar,
                tooth_decay]
for i in range(3):
    enemies_list.append(enemies_list[random.randint(0, 2)])
    enemies_list = enemies_list[-3:]

player_defense = 0
enemy = 2
# # PLAYER RANDOM DAMAGE MULTIPLIER.
# # critical_hit = int(10 * (random.randint(1, 2) + (random.randint(0, 9) * 0.1))
# #                    if random.randint(1, 3) == 1 else 0)
# # current_attack = weaken_weapons[player.base_dmg][1] + critical_hit

enemy_attack = (int(enemies_list[enemy].base_dmg * (random.randint(0, 30))/10)
                if random.randint(1, 2) == 1 else 3)

print(enemy_attack)


def battle():
    round = 1
    if len(enemies_list) != 0 and round <= 5:
        user_info()
        sleep(1)
        print(f"\n{SEPARATOR}\n")
        print(f"              ROUND {round}!")
        enemy_info()
        enemy = chosen_enemy()
        player.base_dmg = weapon_selection()
        round += 1
    elif round == 6:
        print("")


battle()
