# john.j.marshall@hotmail.com

import items, enemies, actions, world

# MapTile is the base class this used as a starting point for other room tiles.


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


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

# Base class for treasure room tile does not appear in the game


class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ...it grows as you get closer! It's sunlight!
        
        Victory is yours!        
        """

    def modify_player(self, player):
        player.victory = True


class TreasureRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)

# Base class for enemy room tile does not appear in the game


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class CaptainsCabinRoom(MapTile):
    def intro_text(self):
        return """
        This room is disorganised with books strewn across the floor and sad bookcase tipped over.
        There is a portrait of a man hanging ominously with holes piercing the art... 
        Possibly a picture of the long gone Captain.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class FindDaggerRoom(TreasureRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """

# @TODO additional room tiles required


