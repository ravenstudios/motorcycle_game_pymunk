import pygame
import pymunk
from constants import *


class Ramp:
    def __init__(self, x, y, space):
        self.pos = (x, y)
        self.vertices = [(-32, 0), (32, 32), (32, -32)]

        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = self.pos

        self.shape = pymunk.Poly(self.body, self.vertices)  # Create the triangle shape with the provided vertices

        space.add(self.body, self.shape)

        # Define the vertices for the triangle (relative to the body's center of gravity)



    def update(self, camera_offset):
        x = self.body.position.x - camera_offset
        y = self.body.position.y
        self.body.position = (x, y)



    def draw(self, surface, camera_offset):

        x = self.body.position.x - camera_offset
        y = self.body.position.y - BLOCK_SIZE // 2

        rect = (
            x,
            y,
            BLOCK_SIZE,
            BLOCK_SIZE
        )
        pygame.draw.rect(surface, (0, 0, 255), rect)
