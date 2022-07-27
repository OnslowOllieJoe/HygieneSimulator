##
# Name: Ollie Joe
# Date: 07/06/022
# Description: RPG battle simulator which teaches dental hygiene.

from random import randint
from time import sleep
import os
import sys

# Constants
MAX_HP = 100
SEPARATOR = "-" * 55
SPACE_LENGTH = 13
weaken_weapons = [
               ["Toothbrush", 25],
               ["Dental Floss", 25],
               ["Mouthwash", 25]
               ]
kill_weapons = [
             ["Dental Scaler", 0],
             ["Filling", 0],
             ]
MAX_MULTIPLIER = 30


# class enemy():
#     def __init__(self, health):
#         self.health = health


# one = enemy(100)
# two = enemy(100)
# three = enemy(100)

# enemies = [one, two, three]
# dead = []
# while len(enemies) > 0:
#     en = int(input("Enemy: ")) - 1
#     enemies[en].health -= randint(25, 75)
#     if enemies[en].health <= 0:
#         enemies[en].health = 0
#         dead.append(enemies[en])
#         if enemies[en] in dead:
#             print("That enemy has already been defeated.")
#     for i in range(len(enemies)):
#         print(enemies[i].health)


class characters():
    def __init__(self, type, health, base_dmg, money):
        self.type = type
        self.health = health
        self.base_dmg = base_dmg
        self.money = money


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def user_info():
    print(f"{SEPARATOR}\n")
    print("              Player:\n")
    print(f"    Health:           {player.health}/{MAX_HP} HP")
    print(f"    Wallet:           ${player.money}")
    print("\n    Main Damage Weapons:")
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
    sleep(0.5)
    print("              Enemies:\n")
    for count, i in enumerate(range(len(enemies_list[1])), start=1):
        sleep(0.3)
        print(f"    {count}: {enemies_list[1][i].type} " +
              (" " * (SPACE_LENGTH - (len(enemies_list[1][i].type)))) +
              f"{str(enemies_list[1][i].health)}/{MAX_HP} HP")
    print("\n" + SEPARATOR + "\n")
    sleep(0.5)


def weapon_selection():
    print("\n" + SEPARATOR)
    while True:
        sleep(0.5)
        try:
            print("\n    Main Weapons:")
            for count, value in enumerate(weaken_weapons, start=1):
                sleep(0.3)
                print(f"    {count}: " + value[0])
            sleep(0.1)
            print("\n" + SEPARATOR)
            chosen_weapon = int(input("\nEnter a number " +
                                      "to select a weapon : "))
            if chosen_weapon in range(1, len(weaken_weapons) + 1):
                print(f"\nYou have chosen " +
                      f"{weaken_weapons[chosen_weapon - 1][0]}!")
                print("\n" + SEPARATOR)
                return chosen_weapon - 1
            else:
                print("Please enter a number from {} to {}."
                      .format(1, len(weaken_weapons)))
                print("\n" + SEPARATOR)
        except Exception:
            print("Sorry, that is not a valid choice.")
            print("\n" + SEPARATOR)


def chosen_enemy():
    sleep(0.5)
    while True:
        try:
            target_enemy = int(input("Select an enemy's number to attack: "))
            if target_enemy in range(1, len(enemies_list[1]) + 1):
                print(f"\nYou have chosen enemy {target_enemy}, " +
                      f"{enemies_list[1][target_enemy-1].type}!")
                return target_enemy - 1
            else:
                print(f"Please enter a number from {1} to " +
                      f"{len(enemies_list[1])}.")
                enemy_info()
        except ValueError:
            print(f"Please enter a number from {1} to " +
                  f"{len(enemies_list[1])}.")
            enemy_info()


player = characters("Player", 100, 0, 0)
plaque = characters("Plaque", 100, 3, 0)
tartar = characters("Tartar", 100, 3, 0)
tooth_decay = characters("Tooth Decay", 100, 3, 0)

enemies_list = [[plaque,
                tartar,
                tooth_decay],
                []]
for i in range(3):
    enemies_list[1].append(enemies_list[0]
                           [randint(0, len(enemies_list))])


# CLEAR THE LIST AT THE END OF EACH ROUND.
def dodge(enemy):
    while True:
        random_num = randint(1, 2)
        try:
            player_guess = int(input("\nGuess a number between" +
                                     " 1 and 2 to dodge the attack: "))
            if player_guess == random_num:
                print("\nCORRECT! You have dodged the enemy's attack.")
                print(f"\n        {enemies_list[1][enemy].type}" +
                      " has dealt 0 damage.")
                return 0
            elif (player_guess != random_num and
                    player_guess in range(1, 3)):
                print("INCORRECT! You failed to dodge the attack.")
                return 1
            else:
                print("Please enter a number between 1 and 2.")
        except ValueError:
            print("Please enter a number between 1 and 2.")


def counterattack(damage, min, enemy):
    hit = (int(enemies_list[1][enemy].base_dmg *
           randint(min, MAX_MULTIPLIER) / 10)
           if randint(1, 1) == 1 else damage)
    print(f"""{enemies_list[1][enemy].type} has performed a counterattack!
\n        {enemies_list[1][enemy].type} has dealt {hit} damage to you!\n""")
    player.health -= hit
    print("\n" + SEPARATOR)
    sleep(3)


def attack(damage, min, enemy):
    # Enemy miss.
    if enemies_list[1][enemy].base_dmg == damage and randint(1, 18) == 1:
        print(f"{enemies_list[1][enemy].type} has missed their attack.")
        return 0
    # User miss.
    if weaken_weapons[player.base_dmg][1] == damage and randint(1, 6) == 1:
        print("\n\nYour attack has missed." +
              "\n        You dealt 0 damage.")
        print("\n\n" + SEPARATOR)
        return 0
    # User dodge.
    if enemies_list[1][enemy].base_dmg == damage and randint(1, 3) == 1:
        if dodge(enemy) == 0:
            return 0
    # User hit.
    hit = (int(damage * randint(min, MAX_MULTIPLIER) / 10)
           if randint(1, 3) == 1 else damage)
    if weaken_weapons[player.base_dmg][1] == damage:
        print(f"""\n\nYour attack hit!
\n      You dealt {hit} damage to {enemies_list[1][enemy].type}!""")
        print("\n\n" + SEPARATOR + "\n\n")
        sleep(3)
    elif enemies_list[1][enemy].base_dmg == damage:
        print(f"\n\n{enemies_list[1][enemy].type}'s attack has hit you!")
        print(f"\n        {enemies_list[1][enemy].type}" +
              f" has dealt {hit} damage to you!\n")
        sleep(3)
    if weaken_weapons[player.base_dmg][1] == damage and randint(1, 6) == 1:
        counterattack(damage, min, enemy)
    return hit


def menu():
    user_info()
    print("\n" + SEPARATOR + "\n")
    print("""    1. Play
    2. How To Play
    3. Exit""")
    print(f"\n{SEPARATOR}\n")
    proceed = int(input("\nSelect an option's number: "))
    print(f"\n{SEPARATOR}\n")
    clear_terminal()
    if proceed == 1:
        battle()
    elif proceed == 2:
        print("Play the game")
    elif proceed == 3:
        sys.exit()
    else:
        print("Please enter an options number.")


def battle():
    round = 1
    fought = 1
    while len(enemies_list) != 0 and round <= 5:
        if fought > 1:
            sleep(1)
            print(f"\n{SEPARATOR}\n")
            print("              Player:\n")
            print(f"\n    Health:           {player.health}/{MAX_HP} HP")
            print(f"    Wallet:           ${player.money}")
        print(f"\n{SEPARATOR}\n")
        sleep(1)
        print(f"""    Round {round}
                        Attack {fought}!""")
        enemy_info()
        enemy = chosen_enemy()
        player.base_dmg = weapon_selection()
        sleep(1)
        enemies_list[1][enemy].health -= attack(weaken_weapons[player.base_dmg][1], 11, enemy)
        sleep(1)
        player.health -= attack(enemies_list[1][enemy].base_dmg, 12, enemy)
        # sleep(5)
        # fought += 1
        # clear_terminal()
    if enemies_list[1][enemy][0] + enemies_list[1][1] + enemies_list[1][2] == 0:
        print("The end")


menu()
