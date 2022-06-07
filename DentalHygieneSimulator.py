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

enemy_list = [
              plaque, 
              tartar, 
              tooth_decay
              ]


# variable.parameter is format for accessing


def fight():
    print("Enemies:")
    for i in enemy_list:
        print(i)
        print(f"    {i[0].type} {str(i[0].health)}/ {max_hp}")
fight()
