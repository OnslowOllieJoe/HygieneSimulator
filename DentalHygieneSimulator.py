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
from tkinter.tix import MAX
from turtle import clear

# Constants
MAX_HP = 100
SEPARATOR = "-" * 55
SPACE_LENGTH = 20
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
HEALING_OPTIONS = [[50, "1) Small glass -  Heals 25HP",
                    "small glass of fluoride water", 25],
                   [75, "2) Medium glass - Heals 50HP",
                    "medium glass of fluoride water", 50],
                   [150, "3) Large glass -  Heals to 100HP",
                   "large glass of fluoride water", 100]]


# Class for player and enemies.
class characters():
    def __init__(self, type, health, base_dmg, money):
        self.type = type
        self.health = health
        self.base_dmg = base_dmg
        self.money = money
        self.status = type


# Player class set.
player = characters("Player", 100, 0, 0)


# Function to clear terminal.
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to print the player's information.
def user_info(player):
    print(SEPARATOR)
    sleep(0.05)
    print("\n")
    sleep(0.05)
    print("              Player:")
    sleep(0.05)
    print("")
    sleep(0.05)
    print(f"    Health:           {player.health}/{MAX_HP} HP")
    sleep(0.05)
    print(f"    Wallet:           ${player.money}")
    sleep(0.05)
    print("\n")
    sleep(0.05)
    print("    Main Damage Weapons:")
    sleep(0.05)
    for count, value in enumerate(weaken_weapons, start=1):
        sleep(0.05)
        print(f"      {count}: " + value[0])
    sleep(0.05)
    print("\n    Finishing Weapons:")
    sleep(0.05)
    for count, value in enumerate(kill_weapons, start=1):
        sleep(0.05)
        print(f"      {count}: " + value[0])
    sleep(0.05)
    print("")
    sleep(0.05)
    print(SEPARATOR)
    proceed()


# Function to ask the user if they want to continue to the next action.
def proceed():
    repeat = True
    while repeat:
        sleep(0.1)
        print("\n")
        proceed = input("Press Enter to continue: ").strip()
        if proceed == "":
            repeat = False
            clear_terminal()
        else:
            print("Please press Enter if you want to continue.")


# Function to print the enemies information.
def enemy_info(current):
    sleep(0.1)
    print("\n")
    sleep(0.1)
    print(SEPARATOR)
    sleep(0.1)
    print("\n")
    sleep(0.1)
    print("              Enemies:")
    sleep(0.1)
    print("")
    sleep(0.1)
    for count, i in enumerate(range(len(current)), start=1):
        sleep(0.1)
        print(f"    {count}: {current[i].status} " +
              (" " * (SPACE_LENGTH - (len(current[i].status)))) +
              (" " * (3 - len(str(current[i].health)))) +
              f"{str(current[i].health)}/{MAX_HP} HP")
    sleep(0.1)
    print("")
    sleep(0.1)
    print(SEPARATOR)
    sleep(0.1)
    print("")
    sleep(0.1)


# Function for the player to select a main wepaon.
def weapon_selection():
    sleep(0.1)
    print("")
    sleep(0.1)
    print(SEPARATOR)
    while True:
        sleep(0.05)
        try:
            print("")
            sleep(0.05)
            print("    Main Weapons: ")
            sleep(0.05)
            print("")
            for count, value in enumerate(weaken_weapons, start=1):
                sleep(0.05)
                print(f"    {count}: " + value[0])
            sleep(0.05)
            print("")
            print(SEPARATOR)
            sleep(0.05)
            print("")
            sleep(0.05)
            print("")
            chosen_weapon = int(input("Enter a number " +
                                      "to select a weapon: "))
            if chosen_weapon in range(1, len(weaken_weapons) + 1):
                sleep(0.05)
                print("")
                sleep(0.05)
                print(f"    You have chosen " +
                      f"{weaken_weapons[chosen_weapon - 1][0]}!")
                sleep(0.05)
                print("")
                sleep(0.05)
                print("")
                sleep(0.05)
                print(SEPARATOR)
                sleep(0.05)
                clear_terminal()
                return chosen_weapon - 1
            else:
                print("Please enter a number from {} to {}."
                      .format(1, len(weaken_weapons)))
                sleep(0.1)
                print("")
                sleep(0.1)
                print("")
                sleep(0.1)
                print(SEPARATOR)
                sleep(0.1)
        except Exception:
            print("Sorry, that is not a valid choice.")
            sleep(0.1)
            print("")
            sleep(0.1)
            print(SEPARATOR)
            sleep(0.1)


# Function for the player to select a finishing weapon.
def finishing_weapons(enemy, current):
    while True:
        try:
            sleep(0.1)
            print("")
            sleep(0.1)
            print("")
            sleep(0.1)
            finisher = int(input("Select the correct weapon to use against" +
                                 f" {current[enemy].type}: "))
            sleep(0.1)
            print("")
            # Check if the weapon is effective against tooth decay.
            if finisher in range(1, 3):
                if (kill_weapons[finisher - 1] == kill_weapons[1]
                        and current[enemy].type == "Tooth Decay"):
                    sleep(0.1)
                    print("You chose a super effective weapon!")
                    sleep(0.1)
                    print(f"    You have defeated {current[enemy].type}!")
                    sleep(0.1)
                    print("")
                    sleep(0.1)
                    print(SEPARATOR)
                    # Change the enemy's status
                    current[enemy].status = ((''.join([u'\u0336{}'.format(c)
                                              for c in current[enemy].type]))
                                             + (" " * (SPACE_LENGTH -
                                                len(current[enemy].type))))
                    current[enemy].health = 0
                    return None
                # Check if the weapon is effective against tartar and plaque
                elif (kill_weapons[finisher - 1] == kill_weapons[0] and
                        (current[enemy].type == "Plaque" or
                         current[enemy].type == "Tartar")):
                    sleep(0.1)
                    print("You chose a super effective weapon!")
                    sleep(0.1)
                    # Change the enemy's status
                    print(f"    You have defeated {current[enemy].type}!")
                    current[enemy].status = ((''.join([u'\u0336{}'.format(c)
                                             for c in current[enemy].type]))
                                             + (" " * (SPACE_LENGTH -
                                                len(current[enemy].type))))
                    current[enemy].health = 0
                    sleep(0.1)
                    print("")
                    sleep(0.1)
                    print(SEPARATOR)
                    return None
                else:
                    sleep(0.1)
                    print("You have chosen the incorrect weapon!")
                    sleep(0.1)
                    print("    Your attack did 0 damage")
                    sleep(0.1)
                    print("")
                    sleep(0.1)
                    print(SEPARATOR)
                    return None
            else:
                print("")
                sleep(0.1)
                print("Please enter a valid option.")
                sleep(0.1)
                print("")
                sleep(0.1)
                print("")
                sleep(0.1)
                print(SEPARATOR)
        except ValueError:
            print("")
            sleep(0.1)
            print("Please enter a valid option.")
            sleep(0.1)
            print("")
            sleep(0.1)
            print("")
            sleep(0.1)
            print(SEPARATOR)


# Function for the player to select an enemy to attack.
def chosen_enemy(current):
    sleep(0.1)
    while True:
        try:
            print("")
            sleep(0.1)
            target_enemy = int(input("Select an enemy's number to attack: "))
            sleep(0.1)
            # Check if the enemy is already dead.
            if target_enemy in range(1, len(current) + 1):
                if (current[target_enemy - 1].health == 0):
                    print("")
                    sleep(0.1)
                    print("That enemy has already been defeated.")
                    sleep(0.1)
                    enemy_info(current)
                else:
                    print("")
                    sleep(0.1)
                    print(f"    You have chosen enemy {target_enemy}, " +
                          f"{current[target_enemy-1].type}!")
                    sleep(0.1)
                    print("")
                    sleep(0.1)
                    print("")
                    print(SEPARATOR)
                    sleep(1)
                    clear_terminal()
                    return target_enemy - 1
            else:
                sleep(0.1)
                print("")
                sleep(0.1)
                print("Sorry, that is not a valid option.")
                sleep(0.1)
                enemy_info(current)
        except ValueError:
            sleep(0.1)
            print("")
            sleep(0.1)
            print("Sorry, that is not a valid option.")
            sleep(0.1)
            enemy_info(current)


# Function for the player to dodge the enemies attacks.
def dodge(enemy, current):
    while True:
        random_num = randint(1, 3)
        try:
            sleep(0.1)
            print("")
            sleep(0.1)
            print("")
            sleep(0.1)
            player_guess = int(input("Guess a number between" +
                                     " 1 and 3 to dodge the attack: "))
            # Check if the player's guess is correct.
            if player_guess == random_num:
                sleep(0.1)
                print("")
                sleep(0.1)
                print("CORRECT! You have dodged the enemy's attack.")
                sleep(0.1)
                print("")
                sleep(0.1)
                print(f"        {current[enemy].type}" +
                      " has dealt 0 damage.")
                sleep(0.1)
                print("")
                sleep(0.1)
                print(SEPARATOR)
                return 0
            elif (player_guess != random_num and
                    player_guess in range(1, 4)):
                print("INCORRECT! You failed to dodge the attack.")
                return 1
            else:
                print("Please enter a number between 1 and 3.")
                sleep(0.1)
        except ValueError:
            print("Please enter a number between 1 and 3.")
            sleep(0.1)


# Function for the enemies to counterattack the player.
def counterattack(damage, min, enemy, current, player):
    hit = int((damage * randint(min, MAX_MULTIPLIER) / 10)
              if randint(1, 3) == 1 else damage)
    sleep(0.1)
    print("")
    sleep(0.1)
    print("")
    sleep(0.1)
    print(f"{current[enemy].type} has performed a counterattack!")
    sleep(0.1)
    if hit > damage:
        print(f"{current[enemy].type}'s attack was a critical hit!")
        sleep(0.1)
    print("")
    sleep(0.1)
    print(f"        {current[enemy].type} has dealt {hit} damage to you!")
    sleep(0.1)
    print("")
    sleep(0.1)
    player.health -= hit
    print("")
    sleep(0.1)
    print(SEPARATOR)
    sleep(0.1)


# Function for the player and enemies attacks and missed attacks.
def attack(damage, min, enemy, dead, round, fought, current, player, chance):
    if current[enemy] in dead:
        return 0
    # Enemy miss.
    if current[enemy].base_dmg == damage and randint(1, 18) == 1:
        sleep(0.1)
        print("")
        sleep(0.1)
        print("")
        sleep(0.1)
        print(f"{current[enemy].type} has missed their attack.")
        sleep(0.1)
        print("")
        sleep(0.1)
        print(f"        {current[enemy].type} has dealt 0 damage.")
        sleep(0.1)
        print("")
        sleep(0.1)
        print("")
        sleep(0.1)
        print(SEPARATOR)
        return 0
    # User miss.
    if weaken_weapons[player.base_dmg][1] == damage and randint(1, 6) == 1:
        sleep(0.1)
        print(SEPARATOR)
        sleep(0.1)
        print("\n")
        sleep(0.1)
        print("Your attack has missed.")
        sleep(0.1)
        print("")
        sleep(0.1)
        print("        You dealt 0 damage.")
        sleep(0.1)
        print("\n")
        sleep(0.1)
        print(SEPARATOR)
        sleep(0.1)
        return 0
    # User dodge.
    if current[enemy].base_dmg == damage and randint(1, 6) == 1:
        if dodge(enemy, current) == 0:
            return 0
    # User hit.
    hit = (int(damage * randint(min, MAX_MULTIPLIER) / 10)
           if randint(1, chance) == 1 else damage)
    if weaken_weapons[player.base_dmg][1] == damage:
        sleep(0.1)
        print(SEPARATOR)
        sleep(0.1)
        print("\n")
        sleep(0.1)
        print("Your attack hit!")
        sleep(0.1)
        if hit > damage:
            print("Your attack was a critical hit!")
            sleep(0.1)
        print("")
        sleep(0.1)
        print(f"    You dealt {hit} damage to {current[enemy].type}!")
        if hit >= current[enemy].health:
            sleep(0.1)
            print("")
            sleep(0.1)
            print(f"You have knocked out {current[enemy].type}!")
            sleep(0.1)
            print(f"Defeat {current[enemy].type} using a finishing weapon.")
        sleep(0.1)
        print("\n")
        sleep(0.1)
        print(SEPARATOR)
    elif current[enemy].base_dmg == damage:
        sleep(0.1)
        print("\n")
        sleep(0.1)
        print(f"{current[enemy].type}'s attack has hit you!")
        sleep(0.1)
        if hit > damage:
            print(f"{current[enemy].type}'s attack was a critical hit!")
            sleep(0.1)
        print("")
        sleep(0.1)
        print(f"        {current[enemy].type}" +
              f" has dealt {hit} damage to you!")
        sleep(0.1)
        print("")
        sleep(0.1)
        print("")
        sleep(0.1)
        print(SEPARATOR)
        if hit >= player.health:
            sleep(1)
            clear_terminal()
            you_lose(round, fought, player)
    return hit


# Function to print the how to play.
def instructions():
    print("\n")
    print(SEPARATOR)
    print("\n")
    print("""1) There are three rounds in a game.

2) Each round has three enemies.

3) The main weapons are toothbrush, dental floss, and mouthwash.

4) The finishing weapons are filling and dental scaler.

5) The enemies can be tooth decay, plaque, and tartar.

6) After winning a round, the player will be rewarded with dollars.

7) The player can purchase health for their character at the end of each round.

8) The main weapons are weapons which deal damage to the enemies
but cannot kill the enemies.

9) The finishing weapons don't deal damage but are used
when the enemy is on 1 health to kill the enemy.

10) At random the player will have the chance to miss their attack,
dodge the enemy attack, deal up to 75 damage.

11) At random each enemy will have the chance to miss their attack,
deal up to 9 damage, and counterattack the player.""")
    print("\n")
    print(SEPARATOR)
    print("\n")


# Function for the player to choose to play, how to play, or exit the game.
def menu(round, fought):
    while True:
        sleep(0.1)
        print("")
        sleep(0.1)
        print(SEPARATOR)
        sleep(0.1)
        print("")
        sleep(0.1)
        print("                      1. Play")
        sleep(0.1)
        print("\n")
        sleep(0.1)
        print("                   2. How To Play")
        sleep(0.1)
        print("\n")
        sleep(0.1)
        print("                      3. Exit")
        sleep(0.1)
        print("")
        sleep(0.1)
        print(SEPARATOR)
        sleep(0.1)
        print("")
        sleep(0.1)
        proceed = input("Select an option's number: ").strip()
        if proceed == "1":
            clear_terminal()
            battle(round, fought, total_fought)
        elif proceed == "2":
            clear_terminal()
            instructions()
            while True:
                sleep(0.1)
                menu_return = input("Press Enter to return " +
                                    "to the menu: ").strip()
                sleep(0.1)
                if menu_return == "":
                    clear_terminal()
                    break
                else:
                    sleep(0.1)
                    print("Please press Enter if you want to " +
                          "return to the menu.")
                    sleep(0.1)
                    print("\n")
        elif proceed == "3":
            sleep(0.1)
            print("")
            sleep(0.1)
            print("Thank you for playing Dental Hygiene Simulator.")
            sys.exit()
        else:
            print("Please enter a valid option's number.")


# Function to check if the enemy is dead.
def check_if_dead(enemy, dead, current):
    if current[enemy].health <= 0:
        dead.append(current[enemy])
        current[enemy].health = 1
        current[enemy].status = f"{current[enemy].type}[Finish]"


# Function to tell the player they lost the gmae and reset character.
def you_lose(round, fought, player):
    print("")
    sleep(0.1)
    print(SEPARATOR)
    sleep(0.1)
    print("")
    sleep(0.1)
    print("                   YOU LOST!")
    sleep(0.1)
    print(f"        You survived to round {round} attack {fought}")
    sleep(0.1)
    print("")
    print(f"    Wallet:    ${player.money}")
    sleep(0.1)
    print("")
    sleep(0.1)
    print(SEPARATOR)
    sleep(0.1)
    proceed()
    round = 1
    fought = 1
    player.health = 100
    player.money = 0
    menu(round, fought)


# Function to tell the player how much they healed and what heal they are on.
def health_print(healing, player):
    sleep(0.1)
    print("")
    sleep(0.1)
    print(SEPARATOR)
    sleep(0.1)
    print("")
    sleep(0.1)
    print("")
    sleep(0.1)
    print(f"  You have purchased a {HEALING_OPTIONS[healing][2]}.")
    sleep(0.1)
    print("")
    sleep(0.1)
    print(f"            You have healed {HEALING_OPTIONS[healing][3]}" +
          " health.")
    sleep(0.1)
    print("")
    sleep(0.1)
    print(f"              Your Health: {player.health}/100 HP")
    sleep(0.1)
    print("")
    sleep(0.1)
    print("")
    sleep(0.1)
    print(SEPARATOR)
    proceed()


# Function to make sure the player does not heal above 100 health.
def over_heal(player):
    if player.health > 100:
        player.health = 100


# Function to tell the player they do not have enough money to buy health.
def money_check(player, healing):
    if player.money < HEALING_OPTIONS[healing][0]:
        print("")
        sleep(0.1)
        print(SEPARATOR)
        sleep(0.1)
        print("")
        sleep(0.1)
        print("")
        sleep(0.1)
        print("  Sorry, you do not have enough to purchase this item.")
        sleep(0.1)
        print("")
        sleep(0.1)
        print("")
        sleep(0.1)
        print(SEPARATOR)
        proceed()
    else:
        return None


# Function for the healing station for the player to purchase health.
def buy_health(player):
    while True:
        if player.health == 100:
            return None
        sleep(0.05)
        print("")
        sleep(0.05)
        print(SEPARATOR)
        sleep(0.05)
        print("")
        sleep(0.05)
        print("")
        sleep(0.05)
        print("              Player:")
        sleep(0.05)
        print("")
        sleep(0.05)
        print("")
        sleep(0.05)
        print(f"    Health:           {player.health}/{MAX_HP} HP")
        sleep(0.05)
        print(f"    Wallet:           ${player.money}")
        sleep(0.05)
        print("")
        sleep(0.05)
        print(SEPARATOR)
        sleep(0.05)
        print("")
        sleep(0.05)
        print("")
        sleep(0.05)
        print("           Fluoride Water Healing station")
        sleep(0.05)
        print("")
        sleep(0.05)
        for i in range(len(HEALING_OPTIONS)):
            print(f"{HEALING_OPTIONS[i][1]}" +
                  (" " * (40 - len(HEALING_OPTIONS[i][1]))) +
                  f"${HEALING_OPTIONS[i][0]}")
            sleep(0.05)
            print("")
        sleep(0.05)
        print("")
        sleep(0.05)
        print("9) Decline")
        sleep(0.05)
        print("")
        sleep(0.05)
        print("")
        sleep(0.05)
        print(SEPARATOR)
        sleep(0.05)
        print("")
        healing = input("Enter an option's number: ").strip()
        sleep(0.05)
        if healing in ["1", "2", "3"]:
            clear_terminal()
            money_check(player, int(healing) - 1)
        if healing == "1" and player.money >= 50:
            clear_terminal()
            player.health += 25
            player.money -= 50
            over_heal(player)
            health_print(int(healing) - 1, player)
        elif healing == "2" and player.money >= 75:
            clear_terminal()
            player.health += 50
            player.money -= 75
            over_heal(player)
            health_print(int(healing) - 1, player)
        elif healing == "3" and player.money >= 150:
            clear_terminal()
            player.health = 100
            player.money -= 150
            health_print(int(healing) - 1, player)
        elif healing == "9":
            clear_terminal()
            return None
        elif healing not in ["1", "2", "3", "9"]:
            print("")
            sleep(0.05)
            print("Sorry, that is not a valid option.")
            sleep(0.05)
            print("")
            sleep(0.05)


round = 1
fought = 1
total_fought = 0


# Function for the battle where the player and enemies attack eachother.
def battle(round, fought, total_fought):
    # Reset the total attacks fought.
    if round == 1 and fought == 1:
        total_fought = 0
    enemies_list = ["Plaque", "Tartar", "Tooth Decay"]
    # Set the enemy classes.
    enemy_one = characters(enemies_list[randint(0,
                           len(enemies_list) - 1)], 100, 3, 0)
    enemy_two = characters(enemies_list[randint(0,
                           len(enemies_list) - 1)], 100, 3, 0)
    enemy_three = characters(enemies_list[randint(0,
                             len(enemies_list) - 1)], 100, 3, 0)
    current = [enemy_one, enemy_two, enemy_three]
    user_info(player)
    dead = []
    fought = 1
    # Check if the play has won the game.
    if round > 3:
        clear_terminal()
        print("")
        sleep(0.1)
        print(SEPARATOR)
        sleep(0.1)
        print("")
        sleep(0.1)
        print("                   YOU WIN!")
        sleep(0.1)
        print("")
        sleep(0.1)
        print(f"             You survived {total_fought} attacks.")
        sleep(0.1)
        print("")
        print(f"    Wallet:    ${player.money}")
        sleep(0.1)
        print("")
        sleep(0.1)
        print(SEPARATOR)
        proceed()
        round = 1
        fought = 1
        total_fought = 0
        player.health = 100
        player.money = 0
        battle(round, fought, total_fought)
    # Check if the player has beat a round.
    if round > 1:
        clear_terminal()
        sleep(0.1)
        print("")
        sleep(0.1)
        print(SEPARATOR)
        sleep(0.1)
        print("")
        sleep(0.1)
        print("")
        sleep(0.1)
        print(f"           You have completed round {round - 1}!")
        sleep(0.1)
        print("")
        sleep(0.1)
        print("       You have been rewarded with 125 dollars!")
        player.money += 125
        sleep(0.1)
        print("")
        sleep(0.1)
        print("")
        sleep(0.1)
        print(SEPARATOR)
        proceed()
        buy_health(player)
    # Loop while all the enemies are not dead.
    while dead != 3 and round <= 5:
        if current[0].health + current[1].health + current[2].health == 0:
            round += 1
            battle(round, fought, total_fought)
        sleep(0.1)
        print("\n")
        sleep(0.1)
        print(SEPARATOR)
        sleep(0.1)
        print("\n")
        sleep(0.1)
        print(f"          Round {round}")
        sleep(0.1)
        print("\n")
        sleep(0.1)
        print(f"                                  Attack {fought}!")
        sleep(0.1)
        print("\n")
        sleep(0.1)
        print(SEPARATOR)
        sleep(1)
        clear_terminal()
        if fought > 1:
            sleep(0.1)
            print("")
            sleep(0.1)
            print(f"{SEPARATOR}")
            sleep(0.1)
            print("")
            sleep(0.1)
            print("              Player:")
            sleep(0.1)
            print("")
            sleep(0.1)
            print("")
            sleep(0.1)
            print(f"    Health:           {player.health}/{MAX_HP} HP")
            sleep(0.1)
            print(f"    Wallet:           ${player.money}")
            sleep(0.1)
            print("")
            sleep(0.1)
            print(SEPARATOR)
            proceed()
        enemy_info(current)
        enemy = chosen_enemy(current)
        if current[enemy] in dead:
            clear_terminal()
            print("")
            sleep(0.1)
            print(SEPARATOR)
            sleep(0.1)
            print("")
            sleep(0.1)
            print("")
            sleep(0.1)
            for count, value in enumerate(kill_weapons, start=1):
                print(f"    {count}: {value[0]}")
                sleep(0.1)
            print("")
            sleep(0.1)
            print("")
            sleep(0.1)
            print(SEPARATOR)
            finishing_weapons(enemy, current)
        else:
            # Let the player attack the enemy.
            player.base_dmg = weapon_selection()
            sleep(0.1)
            current[enemy].health -= attack(weaken_weapons[player.base_dmg][1],
                                            11, enemy, dead, round, fought,
                                            current, player, 3)
            sleep(0.1)
            check_if_dead(enemy, dead, current)
            if (randint(1, 6) == 1 and current[enemy] not in dead):
                counterattack(current[enemy].base_dmg, 12,
                              enemy, current, player)
        proceed()
        print(SEPARATOR)
        # Make the enemies attack the player.
        player.health -= attack(current[enemy].base_dmg, 12, 0, dead,
                                round, fought, current, player, 3)
        player.health -= attack(current[enemy].base_dmg, 12, 1, dead,
                                round, fought, current, player, 3)
        player.health -= attack(current[enemy].base_dmg, 12, 2, dead,
                                round, fought, current, player, 3)
        if len(dead) != 3:
            proceed()
        fought += 1
        total_fought += 1
        clear_terminal()


# Call the menu to start the game.
menu(round, fought)
