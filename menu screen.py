import pygame
from pygame.locals import *

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True
        return False

def program():
    pygame.init()

    width = 600
    height = 600
    size = (width, height)

    screen = pygame.display.set_mode(size)

    # Set up the default font
    pygame.font.init()
    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render("Some text!", 1, (255,255,0))
    label.blit(label, (100, 100))

    while True:
        screen.fill((0, 0, 0))

        pygame.display.flip()

program()

