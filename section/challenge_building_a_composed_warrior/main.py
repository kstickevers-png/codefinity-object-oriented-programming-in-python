class Weapon:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack

class Warrior:
    def __init__(self, name):
        self.name =name
        self.weapon= None
        
    def equip_weapon(self, weapon):
        self.weapon = weapon

    def show_weapon(self):
        if self.weapon == None:
            print (f"{self.name.lower()} is unarmed")
        else:    
            print(f"{self.name.lower()} is holding a {self.weapon.name.lower()}")


sword = Weapon("Sword", 5)
warrior = Warrior("Conan")

warrior.equip_weapon(sword)
warrior.show_weapon()