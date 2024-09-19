import pygame
import pymunk
from constants import *
import math
import random


class Game_object:
    def __init__(self):
        pass

    def update(self):
        pass

    def reset(self):
        pass


    def draw(self, surface, camera_offset):
        if self.body.position.x > GAME_WIDTH:
            x = self.body.position.x - camera_offset
        else:
            x = self.body.position.x - BLOCK_SIZE // 2

        y = self.body.position.y - BLOCK_SIZE // 2

        rect = (
            x,
            y,
            BLOCK_SIZE,
            BLOCK_SIZE
        )
        pygame.draw.rect(surface, (255, 0, 0), rect)
