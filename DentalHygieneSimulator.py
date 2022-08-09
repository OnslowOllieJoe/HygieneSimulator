##
# Name: Ollie Joe
# Date: 07/06/022
# Description: RPG battle simulator which teaches dental hygiene.

from ast import excepthandler
from multiprocessing.sharedctypes import Value
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


class characters():
    def __init__(self, type, health, base_dmg, money, status):
        self.type = type
        self.health = health
        self.base_dmg = base_dmg
        self.money = money
        self.status = status


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def user_info(player):
    print(SEPARATOR)
    sleep(0.15)
    print("\n")
    sleep(0.15)
    print("              Player:\n")
    sleep(0.15)
    print(f"    Health:           {player.health}/{MAX_HP} HP")
    sleep(0.15)
    print(f"    Wallet:           ${player.money}")
    sleep(0.15)
    print("\n")
    sleep(0.15)
    print("    Main Damage Weapons:")
    sleep(0.15)
    for count, value in enumerate(weaken_weapons, start=1):
        sleep(0.15)
        print(f"      {count}: " + value[0])
    sleep(0.15)
    print("\n    Finishing Weapons:")
    sleep(0.15)
    for count, value in enumerate(kill_weapons, start=1):
        sleep(0.15)
        print(f"      {count}: " + value[0])
    sleep(0.15)
    print("")
    sleep(0.15)
    print(SEPARATOR)
    proceed()


def proceed():
    repeat = True
    while repeat:
        sleep(0.15)
        print("\n")
        proceed = input("Press Enter to continue: ").strip()
        if proceed == "":
            repeat = False
            clear_terminal()
        else:
            print("Please press Enter if you want to continue.")


def enemy_info(current):
    sleep(0.15)
    print("\n")
    sleep(0.15)
    print(SEPARATOR)
    sleep(0.15)
    print("\n")
    sleep(0.15)
    print("              Enemies:\n")
    sleep(0.15)
    for count, i in enumerate(range(len(current)), start=1):
        sleep(0.15)
        print(f"    {count}: {current[i].type} " +
              (" " * (SPACE_LENGTH - (len(current[i].type)))) +
              f"{str(current[i].health)}/{MAX_HP} HP")
    print("\n" + SEPARATOR + "\n")
    sleep(0.15)


def weapon_selection():
    print("\n" + SEPARATOR)
    while True:
        sleep(0.15)
        try:
            print("\n    Main Weapons:\n")
            for count, value in enumerate(weaken_weapons, start=1):
                sleep(0.15)
                print(f"    {count}: " + value[0])
            sleep(0.15)
            print("\n" + SEPARATOR)
            sleep(0.15)
            chosen_weapon = int(input("\n\nEnter a number " +
                                      "to select a weapon : "))
            if chosen_weapon in range(1, len(weaken_weapons) + 1):
                sleep(0.15)
                print(f"\n    You have chosen " +
                      f"{weaken_weapons[chosen_weapon - 1][0]}!\n")
                sleep(0.15)
                print("\n" + SEPARATOR)
                sleep(1.3)
                clear_terminal()
                return chosen_weapon - 1
            else:
                print("Please enter a number from {} to {}."
                      .format(1, len(weaken_weapons)))
                sleep(0.15)
                print("\n" + SEPARATOR)
                sleep(0.15)
        except Exception:
            print("Sorry, that is not a valid choice.")
            sleep(0.15)
            print("\n" + SEPARATOR)
            sleep(0.15)


def finishing_weapons(enemy, current):
    while True:
        try:
            sleep(0.15)
            print("")
            sleep(0.15)
            finisher = int(input("Select the correct weapon to use against" +
                                 f" {current[enemy].type}: ")) - 1
            sleep(0.15)
            print("")
            if finisher + 1 in range(1, 2):
                if (kill_weapons[finisher] == kill_weapons[0] and
                        current[enemy].type == "Plaque" or
                        current[enemy].type == "Tartar"):
                    sleep(0.15)
                    print("You chose a super effective weapon!")
                    sleep(0.15)
                    print(f"    You have defeated {current[enemy].type}!")
                    return 1
                elif (kill_weapons[finisher] == kill_weapons[1]
                        and current[enemy].type == "Tooth Decay"):
                    sleep(0.15)
                    print("You chose a super effective weapon!")
                    sleep(0.15)
                    print(f"    You have defeated {current[enemy].type}!")
                else:
                    sleep(0.15)
                    print("You have chosen the incorrect weapon!")
                    sleep(0.15)
                    print("    Your attack did 0 damage")
                    return 0
            else:
                print("Please enter a valid option.")
        except ValueError:
            print("Please enter a valid option.")


def chosen_enemy(dead, current):
    sleep(0.15)
    while True:
        try:
            print("")
            sleep(0.15)
            target_enemy = int(input("Select an enemy to attack by" +
                                     " entering their number: "))
            if target_enemy in range(1, len(current) + 1):
                sleep(0.15)
                print(f"\n    You have chosen enemy {target_enemy}, " +
                      f"{current[target_enemy-1].type}!\n\n")
                sleep(0.15)
                print(SEPARATOR)
                sleep(1.3)
                clear_terminal()
                return target_enemy - 1
            else:
                print(f"Please enter a number from {1} to " +
                      f"{len(current) - 1}.")
                sleep(0.15)
                enemy_info(current)
        except ValueError:
            print(f"Please enter a number from {1} to " +
                  f"{len(current) - 1}.")
            sleep(0.15)
            enemy_info()


def dodge(enemy, current):
    while True:
        random_num = randint(1, 3)
        try:
            sleep(0.15)
            player_guess = int(input("\nGuess a number between" +
                                     " 1 and 3 to dodge the attack: "))
            if player_guess == random_num:
                sleep(0.15)
                print("\nCORRECT! You have dodged the enemy's attack.")
                sleep(0.15)
                print(f"\n        {current[enemy].type}" +
                      " has dealt 0 damage.")
                sleep(0.15)
                print("")
                sleep(0.15)
                print(SEPARATOR)
                return 0
            elif (player_guess != random_num and
                    player_guess in range(1, 4)):
                print("INCORRECT! You failed to dodge the attack.")
                return 1
            else:
                print("Please enter a number between 1 and 2.")
                sleep(0.15)
        except ValueError:
            print("Please enter a number between 1 and 2.")
            sleep(0.15)


def counterattack(damage, min, enemy, current, player):
    hit = (int(damage * randint(min, MAX_MULTIPLIER) / 10)
           if randint(1, 3) == 1 else damage)
    sleep(0.15)
    print("")
    sleep(0.15)
    print("")
    sleep(0.15)
    print(f"""{current[enemy].type} has performed a counterattack!
\n        {current[enemy].type} has dealt {hit} damage to you!\n""")
    sleep(0.15)
    player.health -= hit
    print("")
    sleep(0.15)
    print(SEPARATOR)
    sleep(0.15)


def attack(damage, min, enemy, dead, round, fought, current, player):
    if current[enemy] in dead:
        return 0
    # Enemy miss.
    if current[enemy].base_dmg == damage and randint(1, 18) == 1:
        sleep(0.15)
        print(f"\n\n{current[enemy].type} has missed their attack.\n")
        sleep(0.15)
        print("")
        sleep(0.15)
        print(SEPARATOR)
        return 0
    # User miss.
    if weaken_weapons[player.base_dmg][1] == damage and randint(1, 6) == 1:
        sleep(0.15)
        print(SEPARATOR)
        sleep(0.15)
        print("\n")
        sleep(0.15)
        print("Your attack has missed.")
        sleep(0.15)
        print("        You dealt 0 damage.")
        sleep(0.15)
        print("\n")
        sleep(0.15)
        print(SEPARATOR)
        sleep(0.15)
        return 0
    # User dodge.
    if current[enemy].base_dmg == damage and randint(1, 6) == 1:
        if dodge(enemy, current) == 0:
            return 0
    # User hit.
    hit = (int(damage * randint(min, MAX_MULTIPLIER) / 10)
           if randint(1, 3) == 1 else damage)
    if weaken_weapons[player.base_dmg][1] == damage:
        sleep(0.15)
        print(SEPARATOR)
        sleep(0.15)
        print("\n")
        sleep(0.15)
        print("Your attack hit!")
        sleep(0.15)
        print(f"    You dealt {hit} damage to {current[enemy].type}!")
        if hit >= current[enemy].health:
            sleep(0.15)
            print("")
            sleep(0.15)
            print(f"You have defeated {current[enemy].type}!")
        sleep(0.15)
        print("\n")
        sleep(0.15)
        print(SEPARATOR)
    elif current[enemy].base_dmg == damage:
        sleep(0.15)
        print("\n")
        sleep(0.15)
        print(f"{current[enemy].type}'s attack has hit you!")
        sleep(0.15)
        print(f"        {current[enemy].type}" +
              f" has dealt {hit} damage to you!")
        sleep(0.15)
        print("")
        sleep(0.15)
        print("")
        sleep(0.15)
        print(SEPARATOR)
        if hit >= player.health:
            sleep(15)
            clear_terminal()
            you_lose(round, fought, player)
    return hit


def instructions():
    print("\n")
    print(SEPARATOR)
    print("\n")
    print("""1) There are five rounds in a game.

2) Each round has three enemies.

3) The main weapons are toothbrush, dental floss, and mouthwash.

4) The finishing weapons are filling and dental scaler.

5) The enemies can be tooth decay, plaque, and tartar.

6) After winning a round, the player will be rewarded with dollars.

7) The player can purchase health for their character at the end of each round.

8) The main weapons are weapons which deal damage to the enemies
but cannot kill the enemies.

9) The finishing weapons don't deal damage but are used
when the enemy is on 1 health to kill the enemy.""")
    print("\n")
    print(SEPARATOR)
    print("\n")


def menu():
    while True:
        sleep(0.15)
        print("\n" + SEPARATOR + "\n")
        sleep(0.15)
        print("                      1. Play")
        sleep(0.15)
        print("\n")
        sleep(0.15)
        print("                   2. How To Play")
        sleep(0.15)
        print("\n")
        sleep(0.15)
        print("                      3. Exit")
        sleep(0.15)
        print(f"\n{SEPARATOR}\n")
        sleep(0.15)
        proceed = input("Select an option's number: ").strip()
        if proceed == "1":
            clear_terminal()
            battle()
        elif proceed == "2":
            clear_terminal()
            instructions()
            while True:
                sleep(0.15)
                menu_return = input("Press Enter to return " +
                                    "to the menu: ").strip()
                sleep(0.15)
                if menu_return == "":
                    clear_terminal()
                    break
                else:
                    sleep(0.15)
                    print("Please press Enter if you want to " +
                          "return to the menu.")
                    sleep(0.15)
                    print("\n")
        elif proceed == "3":
            sleep(0.15)
            print("\nThank you for using Dental Hygiene Simulator.")
            sys.exit()
        else:
            print("Please enter a valid option's number.")


def check_if_dead(enemy, dead, current):
    if current[enemy].health <= 0:
        dead.append(current[enemy])
        current[enemy].health = 1
        current[enemy].status = (f"{current[enemy].type} " +
                                 "(Use finishing weapon to kill!)")


def you_lose(round, fought, player):
    print("")
    sleep(0.15)
    print(SEPARATOR)
    sleep(0.15)
    print("")
    sleep(0.15)
    print("                   YOU LOST!")
    sleep(0.15)
    print(f"        You survived to round {round} attack {fought}")
    sleep(0.15)
    print("")
    print(f"    Wallet:    ${player.money}")
    sleep(0.15)
    print("")
    sleep(0.15)
    print(SEPARATOR)
    sleep(0.15)
    proceed()
    menu()


def battle():
    enemies_list = ["Plaque", "Tartar", "Tooth Decay"]
    player = characters("Player", 100, 0, 0, "Player")
    enemy_one = characters(enemies_list[randint(0,
                           len(enemies_list) - 1)], 25, 3, 0,
                           enemies_list[randint(0, len(enemies_list) - 1)])
    enemy_two = characters(enemies_list[randint(0,
                           len(enemies_list) - 1)], 100, 3, 0,
                           enemies_list[randint(0, len(enemies_list) - 1)])
    enemy_three = characters(enemies_list[randint(0,
                             len(enemies_list) - 1)], 100, 3, 0,
                             enemies_list[randint(0, len(enemies_list) - 1)])
    current = [enemy_one, enemy_two, enemy_three]
    round = 1
    fought = 1
    user_info(player)
    dead = []
    while len(current) != 0 and round <= 5:
        if fought > 1:
            sleep(1)
            print(f"\n{SEPARATOR}\n")
            sleep(0.15)
            print("              Player:\n")
            sleep(0.15)
            print(f"\n    Health:           {player.health}/{MAX_HP} HP")
            sleep(0.15)
            print(f"    Wallet:           ${player.money}")
            sleep(0.15)
            print("")
            sleep(0.15)
            print(SEPARATOR)
            proceed()
        sleep(0.15)
        print("\n")
        sleep(0.15)
        print(SEPARATOR)
        sleep(0.15)
        print("\n")
        sleep(0.15)
        print(f"          Round {round}")
        sleep(0.15)
        print("\n")
        sleep(0.15)
        print(f"                                  Attack {fought}!")
        sleep(0.15)
        print("\n")
        sleep(0.15)
        print(SEPARATOR)
        sleep(1.3)
        clear_terminal()
        enemy_info(current)
        enemy = chosen_enemy(dead, current)
        if current[enemy] in dead:
            clear_terminal()
            print("")
            sleep(0.15)
            print(SEPARATOR)
            sleep(0.15)
            print("")
            sleep(0.15)
            print("")
            sleep(0.15)
            for count, value in enumerate(kill_weapons, start=1):
                print(f"    {count}: {value[0]}")
                sleep(0.15)
            print("")
            sleep(0.15)
            print("")
            sleep(0.15)
            print(SEPARATOR)
            finishing_weapons(enemy, current)
        else:
            player.base_dmg = weapon_selection()
            sleep(0.15)
            current[enemy].health -= attack(weaken_weapons[player.base_dmg][1],
                                            11, enemy, dead, round, fought,
                                            current, player)
            sleep(0.15)
            check_if_dead(enemy, dead, current)
            if (randint(1, 1) == 1 and current[enemy] not in dead):
                counterattack(current[enemy].base_dmg, min,
                              enemy, current, player)
            proceed()
            print(SEPARATOR)
            player.health -= attack(current[enemy].base_dmg, 12, 0, dead,
                                    round, fought, current, player)
            player.health -= attack(current[enemy].base_dmg, 12, 1, dead,
                                    round, fought, current, player)
            player.health -= attack(current[enemy].base_dmg, 12, 2, dead,
                                    round, fought, current, player)
        proceed()
        fought += 1
        clear_terminal()
    if current[0] + current[1] + current[2] == 0:
        round += 1
        print(f"Round {round}")


menu()
