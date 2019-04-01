# john.j.marshall@hotmmail.com

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class Skeleton(Enemy):
    def __init__(self):
        super().__init__(name="Skeleton (Old Pew)", hp=100, damage=15)

