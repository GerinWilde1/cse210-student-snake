import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here



class Food(Actor):
    


    def __init__(self):

        super().__init__()
        self.set_text("@")
        self._points = 0
        self.reset()


    def get_points(self):


        return self._points

    def reset(self):
        """moves the food to a new random location then it's picked up."""
        self._points = random.randint(1, 5)
        x = random.randint(2, constants.MAX_X - 2)
        y = random.randint(2, constants.MAX_Y - 2)
        position = Point(x, y)
        self.set_position(position)