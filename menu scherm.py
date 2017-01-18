import math
import pygame
black = (0, 0, 0)

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def program():
    pygame.init()
    pygame.font.init()

    width = 600
    height = 600
    size = (width, height)

    screen = pygame.display.set_mode(size)

    font = pygame.font.SysFont("None", 60)
    game_name = font.render("Battleships", True, black)
    game_start = font.render("Start Game", True, black)
    game_help = font.render("Regels",True,black)
    game_quit = font.render("Stop game",True,black)


    while process_events():
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), (170, 40, 300, 80), 10)
        screen.blit(game_name,(180,50))
        screen.blit(game_start, (180, 200))
        screen.blit(game_help, (180, 350))
        screen.blit(game_quit, (180, 500))
        pygame.display.flip()

program()