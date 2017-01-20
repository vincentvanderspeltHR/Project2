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
blue = (0, 50, 200)

clock = pygame.time.Clock()

rulesfont = pygame.font.SysFont("centurygothic", 15)
headingfont = pygame.font.SysFont("centurygothic", 20)
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
        pygame.draw.rect(screen, (blue), (self.gridstartx, self.gridstarty, self.x, self.y), 0)
        gridlines = 0
        while not gridlines > 20:
            pygame.draw.line(screen, (0, 0, 0), (((self.resolution_x-self.x)/2), (((self.resolution_y-self.y)/2)+self.gridy*gridlines)), ((((self.resolution_x-self.x)/2)+self.x), (((self.resolution_y-self.y)/2)+self.gridy*gridlines)), 2)
            gridlines += 1
        gridlines = 0
        while not gridlines > 20:
            pygame.draw.line(screen, (0, 0, 0), (((self.resolution_x-self.x)/2)+self.gridx*gridlines, ((self.resolution_y-self.y)/2)), (((self.resolution_x-self.x)/2)+self.gridx*gridlines, ((self.resolution_y-self.y)/2)+self.y), 2)
            gridlines += 1
        pygame.draw.rect(screen, black, (self.gridstartx - 140, self.gridstarty, 135, self.y / 3), 8)
        pygame.draw.rect(screen, black,(self.gridstartx - 140, self.y + self.gridstarty - (self.y / 3), 135, self.y / 3), 8)
        pygame.draw.rect(screen, black, (
        self.gridstartx + self.x, self.gridstarty + (self.y / 10) * 4, self.gridstartx, (self.y / 10) * 2), 8)
        trapcards = 0
        while not trapcards > 6:
            pygame.draw.rect(screen, black, (self.gridstartx + (self.x / 7 * trapcards), self.gridstarty - self.gridstarty * 0.75, self.x / 7,self.gridstarty * 0.75), 10)
            trapcards += 1
        trapcards = 0
        while not trapcards > 6:
            pygame.draw.rect(screen, black, (self.gridstartx + (self.x / 7 * trapcards), self.gridstarty + self.y, self.x / 7, self.gridstarty * 0.75),10)
            trapcards += 1
        perkcards = 0
        while not perkcards > 3:
            pygame.draw.rect(screen, black, (self.gridstartx + self.x, self.gridstarty + (self.y / 10) * perkcards, self.x / 4, self.x / 10), 10)
            perkcards += 1
        perkcards = 1
        while not perkcards > 4:
            pygame.draw.rect(screen, black, (self.gridstartx + self.x, self.gridstarty + self.y - (self.y / 10) * perkcards, self.x / 4, self.x / 10),  10)
            perkcards += 1

class Boat:
    def __init__(self, x, y, length, steps, gamegrid):
        self.x = x
        self.y = y
        self.new_x = x
        self.new_y = y
        self.length = length
        self.steps = steps
        self.gamegrid = gamegrid
        self.position_attacking = (self.x, self.y, (self.gamegrid.gridx)-(self.gamegrid.gridx/4), ((self.gamegrid.gridy)*self.length - (self.gamegrid.gridx/4)))
        self.position_defending = (self.position_attacking[0]-self.gamegrid.gridx, self.position_attacking[1]+self.gamegrid.gridy, self.position_attacking[3], self.position_attacking[2])
        self.new_position = (self.new_x, self.new_y, (self.gamegrid.gridx)-(self.gamegrid.gridx/4), ((self.gamegrid.gridy)*self.length - (self.gamegrid.gridx/4)))
        self.original_stance = "attacking"
        self.new_stance = "attacking"
        self.movement = 0

    def draw(self, screen):
        if self.original_stance == "attacking":
            pygame.draw.ellipse(screen, black, self.position_attacking, 0)
        elif self.original_stance == "defending":
            pygame.draw.ellipse(screen, black, self.position_defending, 0)

    def draw_new_stance(self, screen):
        if not self.original_stance == self.new_stance:
            if self.new_stance == "attacking":
                pygame.draw.ellipse(screen, light_red, self.position_attacking, 0)
            else:
                pygame.draw.ellipse(screen, light_red, self.position_defending, 0)

    def change_stance(self):
        if self.new_stance == "defending":
            self.new_stance = "attacking"
            print("attacking")
        else:
            self.new_stance = "defending"
            print("defending")

    def move(self, direction):
        max_movement = self.steps+1
        if self.new_stance == "attacking":
            if direction == "left":
                if (self.new_x - self.gamegrid.gridx)-self.new_x
                self.movement += 1
                if max_movement > movement > -max_movement:
                    self.new_x -= self.gamegrid.gridx
                else:
                    self.x_movement += 1

            elif direction == "right":
                self.movement += 1
                movement = self.x_movement + self.y_movement
                if max_movement > movement > -max_movement:
                    self.new_x += self.gamegrid.gridx
                else:
                    self.x_movement += 1


            print(self.movement)
        print(self.new_x)
        print(self.new_y)
def text_objects(text, color, size = "small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    if size == "rules":
        textSurface = rulesfont.render(text, True, color)

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
    elif action == "start":
        gameLoop()
    elif action == "main":
        gameIntro()
    elif action == "rules_main":
        gameRules("main")
    elif action == "rules_voorbereiding":
        gameRules("voorbereiding")
    elif action == "rules_spelverloop":
        gameRules("spelverloop")
    elif action == "rules_boten":
        gameRules("boten")
    elif action == "rules_bewegen&posities":
        gameRules("bewegen & posities")
    elif action == "rules_kaarten":
        gameRules("kaarten")
    elif action == "termination_screen":
        gameTermination()

def gameIntro():
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        screen.fill(white)
        text_to_screen("Battleships", black, -(display_height*0.35), "medium")
        button("Start game", (display_width/2)-75 , (display_height*0.35), 150, 50, red, light_blue, black, "start")
        button("Help", (display_width / 2) - 75, (display_height * 0.45), 150, 50, red, light_blue, black, "rules_main")
        button("High score",  (display_width/2)-75, (display_height*0.55), 150, 50, red, light_blue, black, "high score")
        button("Quit", (display_width/2)-75, (display_height*0.65), 150, 50, red, light_blue,black, "quit")

        pygame.display.update()

    pygame.quit()
    quit()

def gameRules(page):
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        screen.fill(white)
        if page == "main":
            text_to_screen("Welkom in het regelboek", black, 0)
            text_to_screen("Navigeer met de knoppen hier rechts", black, +50, "rules")

        elif page == "voorbereiding":
            text_to_screen("Welkom op pagina voorbereiding", black, -100, "small")
            text_to_screen("Iedere speler begint met twee schepen", black, -50, "rules")
            text_to_screen("en 2 kaarten van de basis stapel.", black, -25, "rules")
            text_to_screen("De spelers plaatsen hun schepen tegen",black, 0, "rules")
            text_to_screen(" zijn/haar eigen haven aan in de aanvalspositie", black, +25, "rules")
            text_to_screen("de speler mag zelf bepalen waar de schepen staan,", black, +50, "rules")
            text_to_screen("zolang ze maar tegen zijn/haar eigen haven staat.", black, +75, "rules")

        elif page == "spelverloop":
            text_to_screen("Welkom op pagina spelverloop", black, -150)
            text_to_screen("Aan het begin van een speler zijn/haar beurt" , black, -100, "rules")
            text_to_screen("trekt de speler één kaart van de normale stapel.", black, -75, "rules")
            text_to_screen("Kaarten mogen alleen gebruikt worden voor het aanvallen.", black, -50, "rules")
            text_to_screen("De speler die aan de beurt is mag zijn schepen verplaatsen,", black, -25, "rules")
            text_to_screen("wanneer een schip van de tegenstander binnen het aanvals", black, 0, "rules")
            text_to_screen("bereik staat van de speler die aan de beurt is staat, mag", black, +25, "rules")
            text_to_screen("de speler die aan de beurt is zijn tegenstanders schip aanvallen.", black, +50, "rules")
            text_to_screen("Er mag per beurt maximaal 2 keer aangevallen worden", black, +75, "rules")
            text_to_screen("en elk schip mag maar maximaal 1 keer per beurt aanvallen.", black, +100, "rules")


        elif page == "boten":
            text_to_screen("Welkom op pagina boten", black, -150)
            text_to_screen("☻Er zijn verschillende schepen in dit spel", black, -100, "rules")
            text_to_screen("met elk andere lengtes.", black, -75, "rules")
            text_to_screen("☻Als een schip vernietigt wordt, zal dit schip op het veld", black, -50, "rules")
            text_to_screen("blijven liggen als obstakel waar", black, -25, "rules")
            text_to_screen("niet doorheen gegaan kan worden.", black, 0, "rules")
            text_to_screen("☻Wanneer een speler al zijn schepen kwijt is,", black, +25, "rules")
            text_to_screen("verliest deze speler.", black, +50, "rules")
            text_to_screen("De winnaar is de speler die als laatste", black, +75, "rules")
            text_to_screen("met een niet vernietigt schip overblijft.", black, +100, "rules")


        elif page == "bewegen & posities":
            text_to_screen("Welkom op pagina bewegen & posities", black, -225)
            text_to_screen("☻Wanneer een speler aan de beurt is mag de speler", black, -175, "rules")
            text_to_screen("al zijn/haar schepen verplaatsen volgens het aantal", black, -150, "rules")
            text_to_screen("stappen dat het schip kan zetten.", black, -125, "rules")
            text_to_screen("☻Ook kun je de positie van je schepen veranderen,", black, -100, "rules")
            text_to_screen("wanneer je dit doet telt dat als 1 stap:", black, -75, "rules")
            text_to_screen("    ☺Wanneer een schip in zijn aanvalspositie staat heeft", black, -50, "rules")
            text_to_screen("    het schip zijn standaard aanval bereik. ", black, -25, "rules")
            text_to_screen("    ☺Wanneer een schip in zijn verdedigingspositite staat", black, 0, "rules")
            text_to_screen("    mag deze niet verplaatst worden.", black, +25, "rules")
            text_to_screen("    (Hulpkaarten hebben nog wel effect)", black, +50, "rules")
            text_to_screen("☻Spelers mogen 2 keer per beurt aanvallen.", black, +75, "rules")
            text_to_screen("Aanvallen kan alleen wanneer een schip van de", black, +100, "rules")
            text_to_screen("tegenstander in het bereik.", black, +125, "rules")
            text_to_screen("staat van een van jouw schepen.", black, +150, "rules")
            text_to_screen("Per schip mag je maar één keer aanvallen.", black, +175, "rules")


        elif page == "kaarten":
            text_to_screen("Welkom op pagina kaarten", black)
            text_to_screen("Pagina nog niet gevonden.", black, +50, "rules")

        if not page == "voorbereiding":
            button("Voorbereiding", display_width*0.75, display_height*0.2, 250, 60, red, light_blue, black, "rules_voorbereiding")
        if not page == "spelverloop":
            button("Spelverloop", display_width*0.75, display_height*0.3, 250, 60, red, light_blue, black, "rules_spelverloop")
        if not page == "boten":
            button("Boten", display_width * 0.75, display_height * 0.4, 250, 60, red, light_blue, black, "rules_boten")
        if not page == "bewegen & posities":
            button("Bewegen & posities", display_width * 0.75, display_height * 0.5, 250, 60, red, light_blue, black, "rules_bewegen&posities")
        if not page == "kaarten":
            button("Kaarten", display_width * 0.75, display_height * 0.6, 250, 60, red, light_blue, black, "rules_kaarten")
        button("Hoofdmenu", display_width*0.75, display_height*0.8, 250, 60, green, light_blue, black, "main")

        pygame.display.update()

    pygame.quit()
    quit()

def gameLoop():
     GameGrid = Grid(display_width, display_height)

     Boat2 = Boat((GameGrid.gridstartx + ((1 / 6) * GameGrid.gridx)), (GameGrid.gridstarty + ((1 / 6) * GameGrid.gridy)),2, 3, GameGrid)

     gameExit = False
     while not gameExit:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameExit = True
             elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Boat2.change_stance()
                elif event.key == pygame.K_RIGHT:
                     Boat2.move("right")
                elif event.key == pygame.K_LEFT:
                     Boat2.move("left")
                elif event.key == pygame.K_UP:
                     Boat2.move("up")
                elif event.key == pygame.K_DOWN:
                     Boat2.move("down")




         screen.fill(white)
         GameGrid.draw(screen)
         Boat2.draw(screen)
         Boat2.draw_new_stance(screen)

         button("Game beëindigen", (display_width/2)-150, (display_height*0.1), 300, 50, red, light_blue, black, "termination_screen")
         button("Hoofdmenu", display_width * 0.825, display_height * 0.85, 190, 60, green, light_blue, black, "main")

         pygame.display.update()


     pygame.quit()
     quit()

def gameTermination():
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True


        screen.fill(white)
        text_to_screen("The game has ended", black, -(display_height/4), "medium")
        button("Hoofdmenu", display_width * 0.5 - 125, display_height * 0.4, 250, 60, red, light_blue, black, "main")
        button("Quit", display_width * 0.5 - 125, display_height * 0.6, 250, 60, red, light_blue, black, "quit")

        pygame.display.update()

    pygame.quit()
    quit()

gameIntro()