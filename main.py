# Main class for the game

import pygame
import pygame_gui

from Pacman import Pacman

# Static variables
WIDTH = 786
HEIGHT = 968
ACTIVE_HEIGHT = 868
FPS = 60

# Initialize pygame and create window
pygame.init()
pygame.display.set_caption('Pac-Man')
surface = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(pygame.Color('#000000'))

# Initialize the pygame GUI manager and clock
manager = pygame_gui.UIManager((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# set a background image
background_image = pygame.transform.scale(pygame.image.load('./assets/levels/1.png'), (WIDTH, ACTIVE_HEIGHT))

# variable to keep the main loop running
is_running = True

# create a pacman object
pacman = Pacman(400, 400, WIDTH, ACTIVE_HEIGHT, surface)

# main loop
while is_running:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            is_running = False
        # check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman.set_direction('left')
            if event.key == pygame.K_RIGHT:
                pacman.set_direction('right')
            if event.key == pygame.K_UP:
                pacman.set_direction('up')
            if event.key == pygame.K_DOWN:
                pacman.set_direction('down')
        manager.process_events(event)

    manager.update(dt)
    surface.blit(background, (0, 0))
    surface.blit(background_image, (0, 50))
    manager.draw_ui(surface)
    pacman.move()

    pygame.display.update()
