##
# Name: Ollie Joe
# Date: 07/06/022
# Description: RPG battle simulator which teaches dental hygiene.

# Constants
MAX_HP = 100
SEPARATOR = "---------------------------------"
SPACE_LENGTH = 15
weaken_weapons = [
               ["Toothbrush", 15],
               ["Dental Floss", 15],
               ["Mouthwash", 15]
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
    for i in range(len(current_enemy_list)):
        print(f"    {current_enemy_list[i].type}: " +
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
                return weaken_weapons[chosen_weapon - 1][0]
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
######