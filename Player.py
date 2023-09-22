import pygame


class Player:
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.rect = pygame.rect
        self.vel_y = 0
        self.jump = False

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)

    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0

        if moving_left:
            dx = -self.speed
        if moving_right:
            dx = self.speed

        self.rect.x += dx
        self.rect.y += dy
