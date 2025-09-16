class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def take_damage(self, amount):
        self.health -= amount

class Warrior(Character):
    def __init__(self, health, damage, speed):
        super().__init__(health, damage, speed)
        self.iron_armor = 0.90
    def take_damage(self, amount):
        mod_amount = amount * self.iron_armor
        return super().take_damage(mod_amount)
    

warrior = Warrior(100, 50, 10)
print(f"Initial health: {warrior.health}")
warrior.take_damage(40)
print(f"Health after damage: {warrior.health}")



  

