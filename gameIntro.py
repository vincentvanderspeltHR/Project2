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
        button ("quit game", (display_width/2)-75, (display_height*0.65), 150, 50, red, light_blue,black, "quit")

        pygame.display.update()

def gameLoop():
     gameExit = False
     gameOver = False
     FPS = 15
     while not gameExit:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameExit = True
         screen.fill(white)
         button("Quit game", (display_width/2)-75, (display_height*0.5), 150, 50, red, light_red, black, "quit")
         pygame.display.update()
         clock.tick(FPS)


     pygame.quit()
     quit()

gameIntro()