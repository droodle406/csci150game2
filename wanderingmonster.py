import random


class wanderingmonster:
    """
    Represents a monster that moves around the world map.

    Parameters:
    x (int): Monster's x position on the grid
    y (int): Monster's y position on the grid
    monster_type (str): Type of monster
    color (list or tuple): RGB color value
    hp (int): Monster health points

    Returns:
    None

    Example:
        monster = wanderingmonster(3, 4, "goblin", [255, 0, 0], 100)
    """

    def __init__(self, x, y, monster_type, color, hp):
        self.x = x
        self.y = y
        self.monster_type = monster_type
        self.color = list(color)
        self.hp = hp

    @classmethod
    def random_spawn(cls, occupied, forbidden, grid_w, grid_h):
        """
        Creates a monster at a random valid location.

        Parameters:
        occupied (list): List of coordinate tuples already used by monsters
        forbidden (list): List of coordinate tuples that monsters cannot spawn on
        grid_w (int): Width of the grid
        grid_h (int): Height of the grid

        Returns:
        wanderingmonster: A new monster object in a valid location

        Example:
            monster = wanderingmonster.random_spawn([], [(0, 0)], 10, 10)
        """

        while True:
            x = random.randint(0, grid_w - 1)
            y = random.randint(0, grid_h - 1)

            if (x, y) not in occupied and (x, y) not in forbidden:
                return cls(x, y, "goblin", [255, 0, 0], 100)

    @classmethod
    def from_dict(cls, data):
        """
        Creates a wanderingmonster object from a dictionary.

        Parameters:
        data (dict): Dictionary containing monster data

        Returns:
        wanderingmonster: Monster object created from saved data

        Example:
            monster = wanderingmonster.from_dict(data)
        """

        return cls(data["x"],data["y"],data["monster_type"],data["color"],data["hp"])

    def to_dict(self):
        """
        Converts the monster object into a JSON-safe dictionary.

        Parameters:
        None

        Returns:
        dict: Dictionary containing monster data

        Example:
            monster.to_dict()
        """

        return {"x": self.x,"y": self.y,"monster_type": self.monster_type,"color": self.color,"hp": self.hp}

    def move(self, occupied, forbidden, grid_w, grid_h):
        """
        Attempts to move the monster one space in a random direction.

        Parameters:
        occupied (list): List of coordinate tuples occupied by other monsters
        forbidden (list): List of coordinate tuples the monster cannot move onto
        grid_w (int): Width of the grid
        grid_h (int): Height of the grid

        Returns:
        None

        Example:
            monster.move(occupied, forbidden, 10, 10)
        """

        directions = [(0, -1),(0, 1),(-1, 0),(1, 0)]

        dx, dy = random.choice(directions)

        new_x = self.x + dx
        new_y = self.y + dy

        if new_x < 0 or new_x >= grid_w:
            return

        if new_y < 0 or new_y >= grid_h:
            return

        if (new_x, new_y) in occupied:
            return

        if (new_x, new_y) in forbidden:
            return

        self.x = new_x
        self.y = new_y
