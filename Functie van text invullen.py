import pygame


pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Menu scherm")

name_list = []

pygame.font.SysFont(None, 50)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

x = display_width
y = display_height

name = ""

gameExit = False
ja = True

gameDisplay.fill(white)

font = pygame.font.SysFont(None, 25)
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x- x/2, y- y/2])
#-----------------------------------------------------------------------------
#De loop.
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
# ----------------------------------------------------------------------------
        if event.type == pygame. KEYDOWN:
            pygame.event.pump()
        while ja:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.event.pump()
                    if event.type == pygame.QUIT:
                        gameExit = True
                    if event.key == pygame.K_q:
                        name = name + "q"
                        pygame.display.update()
                    if event.key == pygame.K_w:
                        name = name + "w"
                        pygame.display.update()
                    if event.key == pygame.K_e:
                        name = name + "e"
                        pygame.display.update()
                    if event.key == pygame.K_r:
                        name = name + "r"
                        pygame.display.update()
                    if event.key == pygame.K_t:
                        name = name + "t"
                        pygame.display.update()
                    if event.key == pygame.K_y:
                        name = name + "y"
                        pygame.display.update()
                    if event.key == pygame.K_u:
                        name = name + "u"
                        pygame.display.update()
                    if event.key == pygame.K_i:
                        name = name + "i"
                        pygame.display.update()
                    if event.key == pygame.K_o:
                        name = name + "o"
                        pygame.display.update()
                    if event.key == pygame.K_p:
                        name = name+"p"
                        pygame.display.update()
                    if event.key == pygame.K_a:
                        name = name+"a"
                        pygame.display.update()
                    if event.key == pygame.K_s:
                        name = name+"s"
                        pygame.display.update()
                    if event.key == pygame.K_d:
                        name = name+"d"
                        pygame.display.update()
                    if event.key == pygame.K_f:
                        name = name+"f"
                        pygame.display.update()
                    if event.key == pygame.K_g:
                        name = name+"g"
                        pygame.display.update()
                    if event.key == pygame.K_h:
                        name = name+"h"
                        pygame.display.update()
                    if event.key == pygame.K_j:
                        name = name+"j"
                        pygame.display.update()
                    if event.key == pygame.K_k:
                        name = name+"k"
                        pygame.display.update()
                    if event.key == pygame.K_l:
                        name = name+"l"
                        pygame.display.update()
                    if event.key == pygame.K_z:
                        name = name+"z"
                        pygame.display.update()
                    if event.key == pygame.K_x:
                        name = name+"x"
                        pygame.display.update()
                    if event.key == pygame.K_c:
                        name = name+"c"
                        pygame.display.update()
                    if event.key == pygame.K_v:
                        name = name+"v"
                        pygame.display.update()
                    if event.key == pygame.K_b:
                        name = name+"b"
                        pygame.display.update()
                    if event.key == pygame.K_n:
                        name = name+"n"
                        pygame.display.update()
                    if event.key == pygame.K_m:
                        name = name+"m"
                        pygame.display.update()
                    if event.key == pygame.K_SPACE:
                        name = name+" "
                        pygame.display.update()
                    if event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                        pygame.display.update()
                    if event.type == pygame.QUIT:
                        gameExit = True
                    if event.key == pygame.K_RETURN:
                        message_to_screen(name, red)
                        gameDisplay.fill(white)
                        pygame.display.update()
                        ja = False
                        pass

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
            gameDisplay.fill(white)
            message_to_screen("Naam: "+ name, red)

            pygame.display.update()

#-----------------------------------------------------------------------------
    gameDisplay.fill(white)

    message_to_screen("Naam: " + name , red)
    pygame.display.update()
pygame.display.update()
pygame.time.wait(0)
pygame.quit()

