# john.j.marshall@hotmail.com

import items, enemies

class MapTile():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def intro_text(self):
    raise NotImplementedError()

  def modify_player(self, player):
    raise NotImplementedError()


class StartingRoom(MapTile):

  def intro_text(self):
    return """
      You awake to find yourself in the belly of a wrecked ship.
      The ruined mast of the ship is adorned with lit candles and ornate artifacts... almost like an alter.
      You have no memory of this place or who you are.
      You can make out four paths leading out of the wrecked ship, each equally full of danger and adventure.
      """

  def modify_player(self, player):
    # Room has no action on player
    pass

# Class for treasure room tile
class TreasureRoom(MapTile):
  def __init__(self, x, y, item):
    self.item = item
    super().__init__(x, y)

  def add_loot(self, player):
    player.inventory.append(self.item)

  def modify_player(self, player):
    self.add_loot(player)

# Class for enemy room tile
class EnemyRoom(MapTile):
  def __init__(self, x, y, enemy):
    self.enemy = enemy
    super().__init__(x, y)

  def modify_player(self, the_player):
    if self.enemy.is_alive():
      the_player.hp = the_player.hp - self.enemy.damage
      print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

# @TODO additional room tiles required

