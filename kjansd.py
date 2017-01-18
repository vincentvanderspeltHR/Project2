import math
import pygame

clock = pygame.time.Clock()
FPS = 60

class Boat:
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length

    def draw(self, screen):
        pygame.draw.ellipse(screen, (0, 0, 0), (self.x, self.y, 22, (30*self.length - 8)), 0)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.x += 30
        elif keys[pygame.K_LEFT]:
            self.x -= 30

        if keys[pygame.K_UP]:
            self.y -= 30
        elif keys[pygame.K_DOWN]:
            self.y += 30

class Grid:
    def __init__(self, resolution_x, resolution_y):
        self.x = 600
        self.y = 600
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y

    def fill(self, screen):
        pygame.draw.rect(screen, (0, 0, 180), (((self.resolution_x-self.x)/2), ((self.resolution_y-self.y)/2), self.x, self.y), 0)

    def draw(self, screen):
        gridlines = 0
        while not gridlines > 20:
            pygame.draw.line(screen, (0, 0, 0), (((self.resolution_x-self.x)/2), ((self.resolution_y-self.y)/2)+30*gridlines), (((self.resolution_x-self.x)/2)+self.x, ((self.resolution_y-self.y)/2)+30*gridlines), 2)
            gridlines += 1
        gridlines = 0
        while not gridlines > 20:
            pygame.draw.line(screen, (0, 0, 0), (((self.resolution_x-self.x)/2)+30*gridlines, ((self.resolution_y-self.y)/2)), (((self.resolution_x-self.x)/2)+30*gridlines, ((self.resolution_y-self.y)/2)+self.y), 2)
            gridlines += 1


def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True

    return False

def program():
    print("Github is gay")
    width = 1000
    height = 1000
    size = (width, height)

    GameGrid = Grid(width, height)

    Boat2 = Boat(205, 205, 2)
    Boat3 = Boat(235, 205, 3)
    Boat4 = Boat(265, 205, 4)



    pygame.init()

    screen = pygame.display.set_mode(size)

    while not process_events():
         screen.fill((255, 255, 255))
         GameGrid.fill(screen)
         GameGrid.draw(screen)
         Boat2.move()
         Boat2.draw(screen)
         Boat3.draw(screen)
         Boat4.draw(screen)
         pygame.display.flip()
         clock.tick(FPS)

program()