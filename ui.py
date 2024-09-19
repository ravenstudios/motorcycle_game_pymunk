import pygame
import pymunk
import pymunk.pygame_util

class MovingObject(pygame.sprite.Sprite):
    def __init__(self, space, position, radius, color, mass=1, friction=0.7):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=position)
        self.body, self.shape = self.create_moving_object(space, position, radius, mass, friction)

    def create_moving_object(self, space, position, radius, mass, friction):
        body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
        body.position = position
        shape = pymunk.Circle(body, radius)
        shape.friction = friction
        space.add(body, shape)
        return body, shape

    def update(self):
        self.rect.center = (self.body.position.x, self.body.position.y)

class Player(MovingObject):
    def __init__(self, space):
        super().__init__(space, (400, 300), 25, (255, 0, 0), mass=1, friction=0.7)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.body.velocity = (-200, 0)
        elif keys[pygame.K_RIGHT]:
            self.body.velocity = (200, 0)
        else:
            self.body.velocity = (0, 0)

        self.body.position += (self.body.velocity[0] * 0.1, self.body.velocity[1] * 0.1)
        super().update()

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.camera_width = width
        self.camera_height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(self.camera_width / 2)
        y = -target.rect.centery + int(self.camera_height / 2)
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.camera.width - 800), x)
        y = max(-(self.camera.height - 600), y)
        self.camera = pygame.Rect(x, y, self.camera_width, self.camera_height)

class Game:
    def __init__(self):
        pygame.init()
        self.space = pymunk.Space()
        self.space.gravity = (0, -900)
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        self.player = Player(self.space)
        self.moving_objects = pygame.sprite.Group()
        self.camera = Camera(1600, 1200)
        self.create_ground()
        self.create_moving_objects()

    def create_ground(self):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape = pymunk.Segment(body, (-400, -300), (400, -300), 10)
        shape.friction = 1.0
        self.space.add(body, shape)

    def create_moving_objects(self):
        # Example: add some moving objects
        colors = [(0, 255, 0), (0, 0, 255)]
        positions = [(300, 300), (500, 400)]
        for color, pos in zip(colors, positions):
            obj = MovingObject(self.space, pos, 30, color)
            self.moving_objects.add(obj)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.player.update(keys)
            self.camera.update(self.player)

            self.screen.fill((0, 0, 0))

            for obj in self.moving_objects:
                obj.update()
                self.screen.blit(obj.image, self.camera.apply(obj))

            self.screen.blit(self.player.image, self.camera.apply(self.player))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
