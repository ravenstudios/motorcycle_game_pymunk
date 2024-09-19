import pygame


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.camera_width = width
        self.camera_height = height

    def apply(self):
        return self.camera.topleft

    def update(self, target):
        x = -target.body.position.x + int(self.camera_width / 2)
        y = -target.body.position.y + int(self.camera_height / 2)
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.camera.width - 800), x)
        y = max(-(self.camera.height - 600), y)
        self.camera = pygame.Rect(x, y, self.camera_width, self.camera_height)
