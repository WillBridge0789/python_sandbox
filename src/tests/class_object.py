class Mage:
    name = ""
    level = 0
    health = 250
    attack = 90
    defense = 70

class Warrior:
    name = ""
    level = 0
    health = 500
    attack = 150
    defense = 125

mage1 = Mage()
mage1.name = "Mary"
mage1.level = 3
mage1.health = 250 * 3
mage1.attack = 90 * 1.5
mage1.defense = 70 * 2

mage2 = Mage()
mage2.name = "Will"
mage2.level = 50
mage2.health = 250 * 25
mage2.attack = 90 * 20
mage2.defense = 70 * 17

warrior1 = Warrior()
warrior1.name = "Larry"
warrior1.level = 10
warrior1.health *= 5
warrior1.attack *= 5
warrior1.defense *= 3

print("This is " + str(mage1.name) + ". They're stats are: lvl: " + str(mage1.level) + " HP: " + str(mage1.health) + " ATK: " + str(mage1.attack) + " DEF: " + str(mage1.defense) + ". " )
print("This is " + str(mage2.name) + ". They're stats are: lvl: " + str(mage2.level) + " HP: " + str(mage2.health) + " ATK: " + str(mage2.attack) + " DEF: " + str(mage2.defense) + ". " )
print("This is " + str(warrior1.name) + ". They're stats are: lvl: " + str(warrior1.level) + " HP: " + str(warrior1.health) + " ATK: " + str(warrior1.attack) + " DEF: " + str(warrior1.defense) + ". " )
