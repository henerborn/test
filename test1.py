class Character:
    def __init__(self, name, health, damage, speed):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed
    def take_damage(self, mod):
        self.health -= mod  

class Warrior(Character):
    def __init__(self, name, health, damage, speed):
        super().__init__(name, health, damage, speed)
        self.iron_armor = 0.50  # Damage is knocked down (0 - worst; 1 - best)

    def take_damage(self, mod):
        mod_health = mod * self.iron_armor
        return super().take_damage(mod_health)

    
class Enemy(Character):
    def __init__(self, name, health, damage, speed):
        super().__init__(name, health, damage, speed)
        self.leather_armor = 0.90

    def take_damage(self, mod):
        mod_health = mod * self.leather_armor
        return super().take_damage(mod_health)
    

def battle(first: Warrior, second: Enemy):
    if first.health > second.health:
        print(f"The {first.name} is more healthy than {second.name}")
    else:
        print(f"The {second.name} is more healthy than {first.name}")

    if first.damage > second.damage:
        print(f"The {first.name} is stronger than {second.name}")
    else:
        print(f"The {second.name} is stronger than {first.name}")

    if first.speed > second.speed:
        print(f"The {first.name} is faster than {second.name}")
    else:
        print(f"The {second.name} is faster than {first.name}")

warrior = Warrior("Victor", 100, 50, 10)
print(f"{warrior.name}'s initial health: {warrior.health}")
print(f"{warrior.name}'s initial damage: {warrior.damage}")
print(f"{warrior.name}'s initial speed: {warrior.speed}")
warrior.take_damage(50)
print(f"{warrior.name}'s health after damage: {warrior.health}")

enemy = Enemy("HenerBorn", 100, 40, 20)
print(f"{enemy.name}'s initial health: {enemy.health}")
print(f"{enemy.name}'s initial damage: {enemy.damage}")
print(f"{enemy.name}'s initial speed: {enemy.speed}")
enemy.take_damage(50)
print(f"{enemy.name}'s health after damage: {enemy.health}")

battle(warrior, enemy)



  

