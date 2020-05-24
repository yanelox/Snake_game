import pygame
import random
import Game_Parameters


class Prize(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.x = random.randint(10, Game_Parameters.width - 10) // Game_Parameters.cell * Game_Parameters.cell \
            + Game_Parameters.cell / 2
        self.y = random.randint(10, Game_Parameters.height - 10) // Game_Parameters.cell * Game_Parameters.cell \
            + Game_Parameters.cell / 2

        self.color = Game_Parameters.red

        self.image = pygame.Surface((Game_Parameters.cell, Game_Parameters.cell))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        self.rect.center = (self.x, self.y)

    def get_prize_x(self):
        return self.x

    def get_prize_y(self):
        return self.y

    def set_prize_x(self, value):
        self.x = value

    def set_prize_y(self, value):
        self.y = value
