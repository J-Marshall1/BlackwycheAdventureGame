# john.j.marshall@hotmail.com
# Game world file


_world = {}
starting_position = (0, 0)


def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    with open('resource/map.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))  # Assumes all rows contain the same number of tabs
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')  # Windows users may to replace '\r\n'
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)

# Method aids in working with map tiles


def tile_exists(x, y):
    return _world.get((x, y))


