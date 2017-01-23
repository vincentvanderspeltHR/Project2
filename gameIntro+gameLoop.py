import pygame
import time
import random

pygame.init()

display_width = 1000
display_height = 1000
screen = pygame.display.set_mode((display_width, display_height))

if display_width<= 600:
    display_width == 600
if display_height <= 600:
    display_height ==600

pygame.display.set_caption("Menu scherm")

#icon = pygame.image.load(" ")
#pygame.display.set_icon(icon)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
light_red = (200,0,0)
light_blue = (0,255,255)
green = (0,255,0)

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("centurygothic", 25)
medfont = pygame.font.SysFont("centurygothic", 50)
largefont = pygame.font.SysFont("centurygothic", 85)
game_name = medfont.render("Battleships", True, black)

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

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 180), (self.gridstartx, self.gridstarty, self.x, self.y), 0)
        gridlines = 0
        while not gridlines > 20:
            pygame.draw.line(screen, (0, 0, 0), (((self.resolution_x-self.x)/2), (((self.resolution_y-self.y)/2)+self.gridy*gridlines)), ((((self.resolution_x-self.x)/2)+self.x), (((self.resolution_y-self.y)/2)+self.gridy*gridlines)), 2)
            gridlines += 1
        gridlines = 0
        while not gridlines > 20:
            pygame.draw.line(screen, (0, 0, 0), (((self.resolution_x-self.x)/2)+self.gridx*gridlines, ((self.resolution_y-self.y)/2)), (((self.resolution_x-self.x)/2)+self.gridx*gridlines, ((self.resolution_y-self.y)/2)+self.y), 2)
            gridlines += 1
        pygame.draw.rect(screen, black, (self.gridstartx-140, self.gridstarty, 135, self.y/3), 8)
        pygame.draw.rect(screen, black, (self.gridstartx-140, self.y+self.gridstarty-(self.y/3), 135, self.y / 3), 8)
        pygame.draw.rect(screen, black, (self.gridstartx+self.x, self.gridstarty+(self.y/10)*4, self.gridstartx,(self.y/10)*2), 8)
        trapcards = 0
        while not trapcards > 6:
            pygame.draw.rect(screen, black, (self.gridstartx+(self.x/7*trapcards), self.gridstarty-self.gridstarty*0.75, self.x/7, self.gridstarty*0.75), 10)
            trapcards += 1
        trapcards = 0
        while not trapcards > 6:
            pygame.draw.rect(screen, black, (self.gridstartx + (self.x / 7 * trapcards), self.gridstarty+self.y, self.x / 7,self.gridstarty * 0.75), 10)
            trapcards += 1
        perkcards = 0
        while not perkcards > 3:
            pygame.draw.rect(screen, black, (self.gridstartx+self.x, self.gridstarty+(self.y/10)*perkcards, self.x/4, self.x / 10), 10)
            perkcards += 1
        perkcards = 1
        while not perkcards > 4:
            pygame.draw.rect(screen, black, (self.gridstartx+self.x, self.gridstarty+self.y-(self.y/10)*perkcards, self.x/4, self.x / 10), 10)
            perkcards += 1




class Boat:
    def __init__(self, x, y, length, gamegrid):
        self.x = x
        self.y = y
        self.length = length
        self.gamegrid = gamegrid
        self.position = (self.x, self.y, (self.gamegrid.gridx)-8, ((self.gamegrid.gridy)*self.length - 8))

    def draw(self, screen):
        pygame.draw.ellipse(screen, (0, 0, 0), self.position, 0)


def text_objects(text, color, size = "small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def text_to_screen(text, color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(text, color, size)
    textRect.center = (int(display_width / 2), int(display_height / 2)+y_displace)
    screen.blit(textSurf, textRect)

def text_to_button(text, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(text, color, size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    screen.blit(textSurf, textRect)

def button(text, x, y, width, height, inactive_color, active_color, text_color, action = None):
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+width > cursor[0] > x and y+height > cursor[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            do_action(action)
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    text_to_button(text, text_color, x, y, width, height)

def do_action(action):
    if action == "quit":
        pygame.quit()
        quit()
    if action == "high score":
        pass
    if action == "start":
        gameLoop()
    if action == "rules":
        pass

def gameIntro():
    gameExit = False
    gameStart = False
    while not gameExit or gameStart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
        screen.fill(white)
        text_to_screen("Battleships", black, -(display_height*0.35), "medium")
        button("Start game", (display_width/2)-75 , (display_height*0.35), 150, 50, red, light_red, black, "start")
        button("rules", (display_width / 2) - 75, (display_height * 0.45), 150, 50, red, light_blue, black, "rules")
        button("High score",  (display_width/2)-75, (display_height*0.55), 150, 50, red, light_blue, black, "high score")
        button("quit game", (display_width/2)-75, (display_height*0.65), 150, 50, red, light_blue,black, "quit")

        pygame.display.update()

def gameLoop():
     gameExit = False
     gameOver = False
     FPS = 15
     while not gameExit:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameExit = True


         GameGrid = Grid(display_width, display_height)

         Boat2 = Boat((GameGrid.gridstartx + ((1 / 6) * GameGrid.gridx)), (GameGrid.gridstarty + ((1 / 6) * GameGrid.gridy)), 2, GameGrid)

         screen.fill(white)
         GameGrid.draw(screen)
         Boat2.draw(screen)

         button("Quit game", (display_width/2)-75, (display_height*0.1), 150, 50, red, light_red, black, "quit")

         pygame.display.update()
         clock.tick(FPS)


     pygame.quit()
     quit()

gameIntro()