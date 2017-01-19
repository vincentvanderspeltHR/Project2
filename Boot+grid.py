import math
import pygame

clock = pygame.time.Clock()
FPS = 60

class Boat:
    def __init__(self, x, y, length, gamegrid):
        self.x = x
        self.y = y
        self.length = length
        self.gamegrid = gamegrid
        self.position = (self.x, self.y, (self.gamegrid.gridx)-8, ((self.gamegrid.gridy)*self.length - 8))

    def draw(self, screen):
        pygame.draw.ellipse(screen, (0, 0, 0), self.position, 0)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.x += (self.gamegrid.x/20)
        elif keys[pygame.K_LEFT]:
            self.x -= (self.gamegrid.x/20)

        if keys[pygame.K_UP]:
            self.y -= (self.gamegrid.y/20)
        elif keys[pygame.K_DOWN]:
            self.y += (self.gamegrid.y/20)

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True

    return False


def program():
    width = 1000
    height = 1000
    size = (width, height)

    GameGrid = Grid(width, height)

    Boat2 = Boat((GameGrid.gridstartx+((1/6)*GameGrid.gridx)), (GameGrid.gridstarty+((1/6)*GameGrid.gridy)), 2, GameGrid)

    pygame.init()

    screen = pygame.display.set_mode(size)

    while not process_events():

         screen.fill((255, 255, 255))
         GameGrid.fill(screen)
         GameGrid.draw(screen)
         Boat2.draw(screen)

         pygame.display.flip()
         clock.tick(FPS)

program()
