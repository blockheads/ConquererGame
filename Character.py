class Character:

    def __init__(self, name, sprite):
        self._name = name
        self._sprite = sprite

        self.health = 100
        self.damage = 10
        self._x = 0
        self._y = 0

    @property
    def name(self):
        return self._name

    """
    in game screen space x coordinate
    """
    @property
    def x(self):
        return self._x

    """
    in game screen space y coordinate
    """
    @property
    def y(self):
        return self._y

    """
    Get the sprite itself for drawing to canvas
    """
    @property
    def sprite(self):
        return self._sprite

    """
    checks if collided with characters current pos
    """
    def collided(self,x,y):
        return self._sprite.get_rect().collidepoint(x - self.x, y - self.y)
    """
    
    sprite bounding box
    """
    def rect(self):
        return self._sprite.get_rect()

