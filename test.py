import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

screen = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Pooface")

#icon = pygame.image.load(" ")
#pygame.display.set_icon(icon)

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
light_red = (255,0,0)

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("centurygothic", 25)
medfont = pygame.font.SysFont("centurygothic", 50)
largefont = pygame.font.SysFont("centurygothic", 85)

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
    if action == "murica":
        print("murica fuck yeah")
    if action == "start":
        gameLoop()


def gameIntro():
    gameExit = False
    gameStart = False
    while not gameExit or gameStart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
        screen.fill(white)
        button("Start", 350, 400, 100, 50, red, light_red, black, "start")

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
        button("Quit", 350, 500, 100, 50, red, light_red, black, "quit")

        pygame.display.update()
        clock.tick(FPS)


    pygame.quit()
    quit()

gameIntro()