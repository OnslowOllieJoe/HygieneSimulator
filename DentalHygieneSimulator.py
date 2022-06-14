##
# Name: Ollie Joe
# Date: 07/06/022
# Description: RPG battle simulator which teaches dental hygiene.

# Constants
MAX_HP = 100
SEPARATOR = "---------------------------------"
SPACE_LENGTH = 15


class characters():
    def __init__(self, type, health, base_dmg, money):
        self.type = type
        self.health = health
        self.base_dmg = base_dmg
        self.money = money


def user_and_enemy_info():
    print(f"""\n{SEPARATOR}\n
            Enemies:\n""")
    for i in range(len(current_enemy_list)):
        print(f"    {current_enemy_list[i].type}: " +
              (" " * (SPACE_LENGTH - (len(current_enemy_list[i].type)))) +
              f"{str(current_enemy_list[i].health)}/{MAX_HP}")
    print(f"{SEPARATOR}\n")
    print("            Player:\n")
    print(f"    Health:     {mc.health}/{MAX_HP}")
    print(f"    Wallet:     ${mc.money}")


def weapon_selection():
    weaken_weapons = [
               ["Tooth Brush", 15],
               ["Dental Floss", 15],
               ["Mouthwash", 15]
               ]
    print(SEPARATOR)
    print("\n            Weapons:\n")
    for count, value in enumerate(weaken_weapons, start=1):
        print(f"    {count}: " + value[0])
    while True:
        try:
            print(SEPARATOR)
            chosen_weapon = int(input("\nPick your weapons number: ")) - 1
            print(f"You have chosen {weaken_weapons[chosen_weapon][0]}!")
            print("\n" +SEPARATOR)
            return weaken_weapons[chosen_weapon][1]
        except:
            print("    Sorry, that is not a valid choice.")


mc = characters("Player", MAX_HP, 0, 0)
plaque = characters("Plaque", MAX_HP, 15, 0)
tartar = characters("Tartar", MAX_HP, 15, 0)
tooth_decay = characters("Tooth Decay", MAX_HP, 15, 0)
current_enemy_list = [
              plaque, 
              tartar, 
              tooth_decay
              ]
user_and_enemy_info()
mc.base_dmg = weapon_selection()
