import pygame
import pymunk
from constants import *
import game_object

class Ramp(game_object.Game_object):
    def __init__(self, x, y, space):
        self.init_x = x
        self.init_y = y
        self.pos = (x, y)
        self.vertices = [(-32, 0), (32, 32), (32, -32)]

        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = self.pos

        self.shape = pymunk.Poly(self.body, self.vertices)  # Create the triangle shape with the provided vertices

        space.add(self.body, self.shape)

        # Define the vertices for the triangle (relative to the body's center of gravity)



    def update(self, camera_offset):

        x = int(self.body.position.x - camera_offset[0])
        y = self.body.position.y
        self.body.position = (x, y)
        pygame.display.set_caption(str(self.body.position))
