import math
import pygame

clock = pygame.time.Clock()
FPS = 60


class Game:
    def __init__(self, firstplayer, P1, P2):
        self.currentplayer = firstplayer
        self.playerlist = [P1, P2]

    def nextplayer(self):
        if self.currentplayer == self.playerlist[0]:
            self.currentplayer = self.playerlist[1]
        else:
            self.currentplayer = self.playerlist[0]

    def __str__(self):
        return str(self.currentplayer.name) + " is the current player."


class Player:
    def __init__(self, name, boat1, boat2):
        self.name = name
        self.score = 0
        self.boatlist = [boat1, boat2]
        self.currentboat = boat1

    def selectedboat(self, screen):
        pygame.draw.ellipse(screen, (255, 255, 255), self.currentboat.position, 4)

    def nextboat(self):
        if self.currentboat == self.boatlist[0]:
            self.currentboat = self.boatlist[1]
        else:
            self.currentboat = self.boatlist[0]


class Grid:
    def __init__(self, resolution_x, resolution_y):
        self.x = resolution_x*0.6
        self.y = resolution_y*0.6
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y
        self.gridstartx = ((self.resolution_x-self.x)/2)
        self.gridstarty = ((self.resolution_y-self.y)/2)
        self.gridx = self.x/20
        self.gridy = self.y/20

    def fill(self, screen):
        pygame.draw.rect(screen, (0, 0, 180), (self.gridstartx, self.gridstarty, self.x, self.y), 0)

    def draw(self, screen):
        gridlines = 0
        while not gridlines > 20:
            pygame.draw.line(screen, (0, 0, 0), (((self.resolution_x-self.x)/2), (((self.resolution_y-self.y)/2)+self.gridy*gridlines)), ((((self.resolution_x-self.x)/2)+self.x), (((self.resolution_y-self.y)/2)+self.gridy*gridlines)), 2)
            gridlines += 1
        gridlines = 0
        while not gridlines > 20:
            pygame.draw.line(screen, (0, 0, 0), (((self.resolution_x-self.x)/2)+self.gridx*gridlines, ((self.resolution_y-self.y)/2)), (((self.resolution_x-self.x)/2)+self.gridx*gridlines, ((self.resolution_y-self.y)/2)+self.y), 2)
            gridlines += 1


class Boat:
    def __init__(self, x, y, length, gamegrid):
        self.x = x
        self.y = y
        self.length = length
        self.gamegrid = gamegrid
        self.position = (self.x, self.y, self.gamegrid.gridx-8, self.gamegrid.gridy*self.length - 8)

    def draw(self, screen):
        pygame.draw.ellipse(screen, (0, 0, 0), self.position, 0)

    def move(self, d):
        if d == "Up":
            self.y -= self.gamegrid.gridy
        if d == "Down":
            self.y += self.gamegrid.gridy
        if d == "Left":
            self.x -= self.gamegrid.gridx
        if d == "Right":
            self.x += self.gamegrid.gridx


def program():
    gameExit = False
    width = 1000
    height = 1000
    size = (width, height)

    GameGrid = Grid(width, height)

    Boat1 = Boat(GameGrid.gridstartx+((1/6)*(GameGrid.gridx*8)), (GameGrid.gridstarty+((1/6)*GameGrid.gridy)), 4, GameGrid)

    Boat2 = Boat(GameGrid.gridstartx+((1/6)*(GameGrid.gridx)), (GameGrid.gridstarty+((1/6)*GameGrid.gridy)), 2, GameGrid)

    P1 = Player("p1", Boat1, Boat2)
    P2 = Player("p2", Boat1, Boat2)

    Game1 = Game(P1, P1, P2)

    pygame.init()

    screen = pygame.display.set_mode(size)

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Boat2.move("Up")
                elif event.key == pygame.K_DOWN:
                    Boat2.move("Down")
                elif event.key == pygame.K_LEFT:
                    Boat2.move("Left")
                elif event.key == pygame.K_RIGHT:
                    Boat2.move("Right")
                elif event.key == pygame.K_SPACE:
                    P1.nextboat()
                elif event.key == pygame.K_n:
                    Game1.nextplayer()
                    print(Game1)

        screen.fill((255, 255, 255))
        GameGrid.fill(screen)
        GameGrid.draw(screen)
        Boat2.draw(screen)
        Boat1.draw(screen)
        P1.selectedboat(screen)
        pygame.display.flip()
        clock.tick(FPS)

program()
