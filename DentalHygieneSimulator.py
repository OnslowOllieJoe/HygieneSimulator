##
# Name: Ollie Joe
# Date: 07/06/022
# Description: RPG battle simulator which teaches dental hygiene.

print()
health = 100
class user():
    def __init__(self, health, weapon):
        self.health = health
        self.dollars = 0

class enemy():
    def __init__(self, type, health, base_dmg):
        self.type = type
        self.health = health
        self.base_dmg = base_dmg

plaque = enemy("Plaque", 100, 15)
tartar = enemy("Tartar", 100, 15)
tooth_decay = enemy("Tooth Decay", 100, 15)

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





current_attack = user(health, weapon_selection())
# variable.parameter is format for accessing
print(plaque.base_dmg)


# Time checker
import datetime
start_time = datetime.datetime.now()
end_time = datetime.datetime.now()
print(end_time - start_time)

