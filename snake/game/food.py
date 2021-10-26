import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here
class Food(Actor):
    """The food class. It keeps track of everything that the food is doing. moves it when needed and when collected helps to grow the snakes tail."""


    def __init__(self):
        """Invokes superclass, calls reset when it's needed in order to move the food to a new location,
        points grows the snake and helps to keep track of total score whilde not being reset from 0"""

        super().__init__()
        self.set_text("@")
        self._points = 0
        self.reset()


    def get_points(self):
        """This helps to call _points whenever it is needed without changing the origional"""

        return self._points

    def reset(self):
        """moves the food to a new random location then it's picked up."""
        self._points = random.randint(1, 5)
        x = random.randint(2, constants.MAX_X - 2)
        y = random.randint(2, constants.MAX_Y - 2)
        position = Point(x, y)
        self.set_position(position)