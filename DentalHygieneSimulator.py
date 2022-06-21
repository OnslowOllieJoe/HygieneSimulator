##
# Name: Ollie Joe
# Date: 07/06/022
# Description: RPG battle simulator which teaches dental hygiene.

import random

# Constants
MAX_HP = 100
SEPARATOR = "---------------------------------"
SPACE_LENGTH = 15
weaken_weapons = [
               ["Toothbrush", 15],
               ["Dental Floss", 15],
               ["Mouthwash", 15]
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


def user_and_enemy_info():
    print(f"{SEPARATOR}\n")
    print("            Player:\n")
    print(f"    Health:          ({mc.health}/{MAX_HP})HP")
    print(f"    Wallet:          ${mc.money}")
    print(f"""\n{SEPARATOR}\n
            Enemies:\n""")
    #for i in range(len(current_enemy_list)):
    for count, i in enumerate(range(len(current_enemy_list)), start=1):
        print(f"    {count}: {current_enemy_list[i].type}: " +
              (" " * (SPACE_LENGTH - (len(current_enemy_list[i].type)))) +
              f"({str(current_enemy_list[i].health)}/{MAX_HP})HP")
    


def weapon_selection():
    print("\n" + SEPARATOR)
    print("\n            Weapons:\n")
    for count, value in enumerate(weaken_weapons, start=1):
        print(f"    {count}: " + value[0])
    while True:
        try:
            print("\n" + SEPARATOR)
            chosen_weapon = int(input("\nEnter a weapons number: "))
            if chosen_weapon in range(1, len(weaken_weapons) + 1):
                print(f"You have chosen {weaken_weapons[chosen_weapon - 1][0]}!")
                print("\n" +SEPARATOR)
                return chosen_weapon - 1
            else:
                print("Please enter a number from {} to {}."
                .format(1, len(weaken_weapons)))
        except:
            print("Sorry, that is not a valid choice.")


mc = characters("Player", 100, 0, 0)
plaque = characters("Plaque", 100, 15, 0)
tartar = characters("Tartar", 100, 15, 0)
tooth_decay = characters("Tooth Decay", 100, 15, 0)
current_enemy_list = [
              plaque, 
              tartar, 
              tooth_decay
              ]
user_and_enemy_info()
mc.base_dmg = weapon_selection()


critical_hit = int(10 * (random.randint(1,2) + (random.randint(0, 9) * 0.1)) if random.randint(1, 3) == 1 else 0)
current_attack = weaken_weapons[mc.base_dmg][1] + critical_hit
print(current_attack)

target_enemy = int(input("Select an enemy's number: "))
if target_enemy in range(1, len(current_enemy_list) + 1):
    print("You have chosen enemy {target_enemy}, {current_enemy_list[target_enemy].type}")
else:
    print(f"Please enter a number from {1} to {len(current_enemy_list)},")
