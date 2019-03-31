#john.j.marshall@outlook.com

class Item():

# This is the base class for all items

  def __init__(self, name, description, value):
    self.name = name
    self.description = description
    self.value = value

  def __str__(self):
    return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# Currency Classes


class Gold(Item):
  def __init__(self, amt):
    self.amt = amt
    super().__init__(name="Gold",
                     description="A round coin with {} stamped on the front.".format(str(self.amt)),
                     value=self.amt)


class Doubloon(Item):
  def __init__(self, amt):
    self.amt = amt
    super().__init__(name="Doubloon",
                     description="An odd shape with an off blue look about it... "
                                 "it feels like it's vibrating in the palm of your hand.".format(str(self.amt)),
                     value=self.amt)


class CursedDoubloon(Item):
  def __init__(self, amt):
    self.amt = amt
    super().__init__(name="Cursed Doubloon",
                     description="The coin disappears as you pick it up... "
                                 "you feel a pain come over you and a black spot appears on the palm of your hand".format(str(self.amt)),
                     value=self.amt)

# Weapon classes

class Weapon(Item):
  def __init__(self, name, description, value, damage):
    self.damage = damage
    super().__init__(name, description, value)

  def __str__(self):
    return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Dagger(Weapon):
    def __init__(self):
      super().__init__(name="Dagger",
                       description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                       value=10,
                       damage=10)

@TODO
#Add in cutlass and flintlock pistol sub classes