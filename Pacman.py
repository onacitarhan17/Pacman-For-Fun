# Pac-Man class

import pygame

class Pacman:
    def __init__(self, x, y, width, height, surface):
        self._SIZE = (50, 50)
        self._asset_right = pygame.transform.scale(pygame.image.load('./assets/pacman/right.png'), self._SIZE)
        self._asset_right_alt = pygame.transform.scale(pygame.image.load('./assets/pacman/right_alt.png'), self._SIZE)
        self._asset_left = pygame.transform.scale(pygame.image.load('./assets/pacman/left.png'), self._SIZE)
        self._asset_left_alt = pygame.transform.scale(pygame.image.load('./assets/pacman/left_alt.png'), self._SIZE)
        self._asset_up = pygame.transform.scale(pygame.image.load('./assets/pacman/up.png'), self._SIZE)
        self._asset_up_alt = pygame.transform.scale(pygame.image.load('./assets/pacman/up_alt.png'), self._SIZE)
        self._asset_down = pygame.transform.scale(pygame.image.load('./assets/pacman/down.png'), self._SIZE)
        self._asset_down_alt = pygame.transform.scale(pygame.image.load('./assets/pacman/down_alt.png'), self._SIZE)
        self._asset_circle = pygame.transform.scale(pygame.image.load('./assets/pacman/circle.png'), self._SIZE)
        self._image = pygame.transform.scale(pygame.image.load('./assets/pacman/circle.png'), self._SIZE)
        self._rect = self._image.get_rect()
        self._rect.center = (x, y)
        self._speed = [0, 0]
        self._width = width
        self._height = height
        self._surface = surface
        self._direction = None

    def move(self):
        self._rect.x += self._speed[0]
        self._rect.y += self._speed[1]
        # check for collision with the walls
        if self._rect.right > self._width:
            self._rect.left = 0
        if self._rect.left < 0:
            self._rect.right = self._width
        if self._rect.top > self._height:
            self._rect.bottom = 0
        if self._rect.bottom < 0:
            self._rect.top = self._height
        self.draw()

    def set_direction(self, direction):
        if direction == 'left':
            self._direction = 'left'
            self._speed = [-1, 0]
        if direction == 'right':
            self._direction = 'right'
            self._speed = [1, 0]
        if direction == 'up':
            self._direction = 'up'
            self._speed = [0, -1]
        if direction == 'down':
            self._direction = 'down'
            self._speed = [0, 1]

    def get_position(self):
        return self._rect.center

    def change_image(self):
        if self._direction == 'left':
            # change image to left_alt.png each second
            if pygame.time.get_ticks() % 150 < 75:
                self._image = self._asset_left
            else:
                self._image = self._asset_left_alt
        elif self._direction == 'right':
            # change image to right_alt.png each second
            if pygame.time.get_ticks() % 150 < 75:
                self._image = self._asset_right
            else:
                self._image = self._asset_right_alt
        elif self._direction == 'up':
            # change image to up_alt.png each second
            if pygame.time.get_ticks() % 150 < 75:
                self._image = self._asset_up
            else:
                self._image = self._asset_up_alt
        elif self._direction == 'down':
            # change image to down_alt.png each second
            if pygame.time.get_ticks() % 150 < 75:
                self._image = self._asset_down
            else:
                self._image = self._asset_down_alt
        else:
            self._image = self._asset_circle

    def draw(self):
        self.change_image()
        self._surface.blit(self._image, self._rect)
