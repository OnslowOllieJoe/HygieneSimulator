##
# Name: Ollie Joe
# Date: 07/06/022
# Description: RPG battle simulator which teaches dental hygiene.

# Constants
MAX_HP = 100
SEPARATOR = "---------------------------------"
SPACE_LENGTH = 15


class entities():
    def __init__(self, type, health, base_dmg, money):
        self.type = type
        self.health = health
        self.base_dmg = base_dmg
        self.money = money


def weapon_selection():
    weaken_weapons = [
               ["Tooth Brush", 15],
               ["Dental Floss", 15],
               ["Mouthwash", 15]
               ]
    print(SEPARATOR)
    for count, value in enumerate(weaken_weapons, start=1):
        print(f"    {count}: " + value[0])
    while True:
        try:
            print(SEPARATOR)
            chosen_weapon = int(input("\nPick your weapons number: ")) - 1
            print(f"You have chosen {weaken_weapons[chosen_weapon][0]}!")
            return weaken_weapons[chosen_weapon][1]
        except:
            print("    Sorry, that is not a valid choice.")


mc = entities("Player", MAX_HP, weapon_selection(), 0)
plaque = entities("Plaque", MAX_HP, 15, 0)
tartar = entities("Tartar", MAX_HP, 15, 0)
tooth_decay = entities("Tooth Decay", MAX_HP, 15, 0)

current_enemy_list = [
              plaque, 
              tartar, 
              tooth_decay
              ]


# variable.parameter is format for accessing
def fight():
    print(f"""\n{SEPARATOR}\n
            Enemies:\n""")
    for i in range(len(current_enemy_list)):
        print(f"    {current_enemy_list[i].type}: " +
              (" " * (SPACE_LENGTH - (len(current_enemy_list[i].type)))) +
              f"{str(current_enemy_list[i].health)}/{MAX_HP}")
    print(f"{SEPARATOR}\n")
    print("            Player:\n")
    print(f"    Your health:     {mc.health}/{MAX_HP}")
    print(f"    Your wallet:     ${mc.money}")
    print(f"{SEPARATOR}\n")
fight()
