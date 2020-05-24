import pygame
import Game_Parameters

orientation = 'left'


class SnakeElement(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)

        self.x = Game_Parameters.width / 2 // Game_Parameters.cell * Game_Parameters.cell + Game_Parameters.cell / 2
        self.y = Game_Parameters.height / 2 // Game_Parameters.cell * Game_Parameters.cell + Game_Parameters.cell / 2

        self.color = color

        self.image = pygame.Surface((Game_Parameters.cell, Game_Parameters.cell))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        self.rect.center = (self.x, self.y)

    def set_snake_element_x(self, value):
        self.x = value

    def set_snake_element_y(self, value):
        self.y = value

    def get_snake_element_x(self):
        return self.x

    def get_snake_element_y(self):
        return self.y

    def get_snake_element_weight(self):
        return self.weight

    def get_snake_element_height(self):
        return self.height


def move(snake_m):
    # Change all coordinates without first element
    for i in range(len(snake_m) - 1, 0, -1):
        snake_m[i].set_snake_element_x(snake_m[i - 1].get_snake_element_x())
        snake_m[i].set_snake_element_y(snake_m[i - 1].get_snake_element_y())

    # Change first element's coordinates
    if orientation == 'left':
        snake_m[0].set_snake_element_x(snake_m[0].get_snake_element_x() - Game_Parameters.moving_speed)
    if orientation == 'up':
        snake_m[0].set_snake_element_y(snake_m[0].get_snake_element_y() - Game_Parameters.moving_speed)
    if orientation == 'right':
        snake_m[0].set_snake_element_x(snake_m[0].get_snake_element_x() + Game_Parameters.moving_speed)
    if orientation == 'down':
        snake_m[0].set_snake_element_y(snake_m[0].get_snake_element_y() + Game_Parameters.moving_speed)
