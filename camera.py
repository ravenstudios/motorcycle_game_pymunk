class Camera:
    def __init__(self, screen_width, screen_height, target):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.target = target  # The player or object the camera follows
        self.offset = pygame.Vector2(0, 0)

    def update(self):
        # Update the camera's offset to follow the target (center the target on the screen)
        self.offset.x = self.target.body.position.x - self.screen_width // 2
        self.offset.y = self.target.body.position.y - self.screen_height // 2

    def apply(self, position):
        # Apply the offset to the object's position before drawing it
        return position - self.offset
