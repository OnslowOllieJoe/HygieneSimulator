##
# Name: Ollie Joe
# Date: 07/06/022
# Description: RPG battle simulator which teaches dental hygiene.

# Constants
max_hp = 100

class user():
    def __init__(self, health, weapon):
        self.health = health
        self.weapon = weapon
        self.dollars = 0


class enemy():
    def __init__(self, type, health, base_dmg):
        self.type = type
        self.health = health
        self.base_dmg = base_dmg


def weapon_selection():
    weaken_weapons = [
               ["Tooth Brush", 15],
               ["Dental Floss", 15],
               ["Mouthwash", 15]
               ]
    print("Available Weapons:")
    count = 1
    for i in weaken_weapons:
        print(f"    {count}: " + i[0])
        count += 1
    while True:
        try:
            chosen_weapon = int(input("Pick your weapons number: ")) - 1
            return weaken_weapons[chosen_weapon][0]
        except:
            print("    Sorry, that is not a valid choice.")


mc = user(100, weapon_selection())
plaque = enemy("Plaque", 100, 15)
tartar = enemy("Tartar", 100, 15)
tooth_decay = enemy("Tooth Decay", 100, 15)

current_enemy_list = [
              plaque, 
              tartar, 
              tooth_decay
              ]


# variable.parameter is format for accessing

SPACE_LENGTH = 15
def fight():
    print("""\n---------------------------------
          Enemies:
---------------------------------""")
    for i in range(len(current_enemy_list)):
        print(f"    {current_enemy_list[i].type}: " +
              (" " * (SPACE_LENGTH - (len(current_enemy_list[i].type)))) +
              f"{str(current_enemy_list[i].health)}/{max_hp}")
    print("---------------------------------")
fight()
