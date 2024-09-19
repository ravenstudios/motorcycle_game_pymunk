import pygame
import pymunk
from constants import *
import math
import random


class Motorcycle:
    def __init__(self, space):
        self.x = 500
        self.y = 500
        self.initial_angle = 0


        self.body = pymunk.Body(1, pymunk.moment_for_box(1, (BLOCK_SIZE, BLOCK_SIZE)))
        self.body.position = (self.x, self.y)
        self.square_shape = pymunk.Poly.create_box(self.body, (BLOCK_SIZE, BLOCK_SIZE))
        self.square_shape.elasticity = 0.5
        self.square_shape.friction = 0.4
        space.add(self.body, self.square_shape)
        # Control parameters
        self.force_magnitude = 1000

    def update(self):



        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.body.apply_force_at_local_point((-self.force_magnitude, 0), (0, 0))
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.body.apply_force_at_local_point((self.force_magnitude, 0), (0, 0))

        if pygame.key.get_pressed()[pygame.K_UP]:
            self.body.angular_velocity += 0.1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.body.angular_velocity -= 0.1

    def reset(self):
        self.body.position = (500, 500)
        self.body.velocity = (0, 0)
        self.body.angular_velocity = 0
        self.body.angle = 0


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
