import pygame, sys
from pygame.locals import *

class Speler:
def __init__(self):
    self.x = X
    self.y = Y
    self.length = Length


def update(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        self.x -= 1
    elif keys[pygame.K_RIGHT]:
        self.x += 1

    if keys[pygame.K_UP]:
        self.y -= 1
    elif keys[pygame.K_DOWN]:
        self.y += 1

print("Test1234")

def draw_circle(self, screen):
    pygame.draw.rect(screen, (255, 0, 0, 128), (int(self.X), int(self.Y), int(self.Length))


    pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Aandacht')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

