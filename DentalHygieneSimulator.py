##
# Name: Ollie Joe
# Date: 07/06/022
# Description: RPG battle simulator which teaches dental hygiene.

# Constants
MAX_HP = 100
SEPERATOR = "---------------------------------"
SPACE_LENGTH = 15

class user():
    def __init__(self, weapon):
        self.weapon = weapon
        self.health = 100
        self.money = 0


class enemy():
    def __init__(self, type, health, base_dmg):
        self.type = type
        self.health = health
        self.base_dmg = base_dmg


# def weapon_selection():
#     weaken_weapons = [
#                ["Tooth Brush", 15],
#                ["Dental Floss", 15],
#                ["Mouthwash", 15]
#                ]
#     print(f"""{SEPERATOR}
# \n     Available Weapons:\n
# {SEPERATOR}""")
#     count = 1
#     for i in weaken_weapons:
#         print(f"    {count}: " + i[0])
#         count += 1
#     while True:
#         try:
#             print(SEPERATOR)
#             chosen_weapon = int(input("\nPick your weapons number: ")) - 1
#             print(f"\nYou have chosen {weaken_weapons[chosen_weapon][0]}")
#             return weaken_weapons[chosen_weapon][0]
#         except:
#             print("    Sorry, that is not a valid choice.")


mc = user("knife") #weapon_selection())
plaque = enemy("Plaque", 100, 15)
tartar = enemy("Tartar", 100, 15)
tooth_decay = enemy("Tooth Decay", 100, 15)

current_enemy_list = [
              plaque, 
              tartar, 
              tooth_decay
              ]


# variable.parameter is format for accessing
def fight():
    print(f"""\n{SEPERATOR}\n
            Enemies:\n
{SEPERATOR}""")
    for i in range(len(current_enemy_list)):
        print(f"    {current_enemy_list[i].type}: " +
              (" " * (SPACE_LENGTH - (len(current_enemy_list[i].type)))) +
              f"{str(current_enemy_list[i].health)}/{MAX_HP}")
    print(f"{SEPERATOR}\n")
    print(f"    Your health:     {mc.health}/{MAX_HP}")
    print(f"    Your wallet:     ${mc.money}")
fight()
