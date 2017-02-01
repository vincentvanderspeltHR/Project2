import pygame
import time
import random
import math

pygame.init()

display_width = 800
display_height = 800
screen = pygame.display.set_mode((display_width, display_height))

if display_width<= 600:
    display_width == 600
if display_height <= 600:
    display_height ==600


image1 = pygame.image.load("adrenaline rush.jpg")
image2 = pygame.image.load("Advanced Rifling.jpg")
image3 = pygame.image.load("Aluminium Hull.jpg")
image4 = pygame.image.load("Backup.jpg")
image5 = pygame.image.load("EMP.jpg")
image6 = pygame.image.load("Extra fuel ll.jpg")
image7 = pygame.image.load("extra fuel.jpg")
image8 = pygame.image.load("Far sight.jpg")
image9 = pygame.image.load("Flak armor.jpg")
image10 = pygame.image.load("FMJ.jpg")
image11 = pygame.image.load("Hack intel.jpg")
image12 = pygame.image.load("Jack Sparrow.jpg")
image13 = pygame.image.load("Naval Mine.jpg")
image14 = pygame.image.load("Rally.jpg")
image15 = pygame.image.load("reinforced hull.jpg")
image16 = pygame.image.load("Repair.jpg")
image17 = pygame.image.load("Rifling.jpg")
image18 = pygame.image.load("sabotage.jpg")
image19 = pygame.image.load("Smokescreen.jpg")
image20 = pygame.image.load("Sonar.jpg")




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

class Card:
    def __init__(self,naam,image):
        self.naam = naam
        self.image = image

card1=Card("adrenaline rush",image1)
card2=Card("Advanced Rifling",image2)
card3=Card("Aluminium Hull",image3)
card4=Card("Backup",image4)
card5=Card("EMP",image5)
card6=Card("Extra fuel ll",image6)
card7=Card("extra fuel",image7)
card8=Card("Far sight",image8)
card9=Card("Flak armor",image9)
card10=Card("FMJ",image10,)
card11=Card("Hack intel",image11)
card12=Card("Jack Sparrow",image12)
card13=Card("Naval Mine",image13)
card14=Card("Rally",image14)
card15=Card("reinforced hull",image15)
card16=Card("Repair",image16)
card17=Card("Rifling",image17)
card18=Card("sabotage",image18)
card19=Card("Smokescreen",image19)
card20=Card("Sonar",image20)

class Game:
    def __init__(self, firstplayer, P1, P2):
        self.currentplayer = firstplayer
        self.playerlist = [P1, P2]

    def __init__(self,cards):
        self.allcardslist = [card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12,card13,card14,card15,card16,card17,card18,card19,card20]
        self.p1list = [card1,card2,card4,card5,card6,card7,card10,card13,card14,card15,card17,card18,card19,card20]
        self.p2list = [card1,card2,card4,card5,card6,card7,card10,card13,card14,card15,card17,card18,card19,card20]
        self.off_list = [card2,card5,card10,card13,card17]
        self.def_list = [card15,card18,card19,card20]
        self.uti_list = [card1,card4,card6,card7]
        self.sp_list = [card3,card8,card9,card11,card12,card16]

    def nextplayer(self):
        for element in self.currentplayer.boatlist:
            element.confirm()
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
        if self.currentboat.new_stance == "attacking":
            pygame.draw.ellipse(screen, (255, 255, 255), (self.currentboat.new_x, self.currentboat.new_y, (self.currentboat.gamegrid.gridx)-(self.currentboat.gamegrid.gridx/4), ((self.currentboat.gamegrid.gridy)*self.currentboat.length - (self.currentboat.gamegrid.gridx/4))), 4)
        else:
            pygame.draw.ellipse(screen, (255, 255, 255), (self.currentboat.new_x, self.currentboat.new_y, ((self.currentboat.gamegrid.gridy)*self.currentboat.length - (self.currentboat.gamegrid.gridx/4)), (self.currentboat.gamegrid.gridx)-(self.currentboat.gamegrid.gridx/4)), 4)

    def nextboat(self):
        if self.currentboat == self.boatlist[0]:
            self.currentboat = self.boatlist[-1]
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
        self.attackingboat_width = (self.gamegrid.gridx)-(self.gamegrid.gridx/4)
        self.attackingboat_height = ((self.gamegrid.gridy)*self.length - (self.gamegrid.gridx/4))
        self.defendingboat_width = self.attackingboat_height
        self.defendingboat_height = self.attackingboat_width
        #self.position_attacking = (self.x, self.y, (self.gamegrid.gridx)-(self.gamegrid.gridx/4), ((self.gamegrid.gridy)*self.length - (self.gamegrid.gridx/4)))
        #self.position_defending = (self.x, self.y, self.position_attacking[3], self.position_attacking[2])
        self.new_position = (self.new_x, self.new_y, (self.gamegrid.gridx)-(self.gamegrid.gridx/4), ((self.gamegrid.gridy)*self.length - (self.gamegrid.gridx/4)))
        self.original_stance = "attacking"
        self.new_stance = "attacking"
        self.movement = self.steps

    def draw(self, screen):
        if self.original_stance == "attacking":
            pygame.draw.ellipse(screen, black, (self.x, self.y, self.attackingboat_width, self.attackingboat_height), 0)
        elif self.original_stance == "defending":
            pygame.draw.ellipse(screen, black, (self.x, self.y, self.defendingboat_width, self.defendingboat_height), 0)

    def draw_new(self, screen):
        if not self.original_stance == self.new_stance and self.new_stance == "defending":
            pygame.draw.ellipse(screen, light_red, (self.new_x, self.new_y, self.defendingboat_width, self.defendingboat_height), 0)
        elif not self.original_stance == self.new_stance and self.new_stance == "attacking":
            if not self.movement == self.steps:
                pygame.draw.ellipse(screen, light_red, (self.new_x, self.new_y, self.attackingboat_width, self.attackingboat_height), 0)
            else:
                pygame.draw.ellipse(screen, light_red, (self.x, self.y, self.attackingboat_width, self.defendingboat_height), 0)
        elif self.original_stance == "defending" and not self.movement == self.steps:
            if self.new_stance == "defending" and self.movement == self.steps - 1:
                pygame.draw.ellipse(screen, black, (self.x, self.y, self.defendingboat_width, self.defendingboat_height), 0)
            else:
                pygame.draw.ellipse(screen, light_red, (self.new_x, self.new_y, self.defendingboat_width, self.defendingboat_height), 0)
        elif self.original_stance == "attacking" and not self.movement == self.steps:
            pygame.draw.ellipse(screen, light_red, (self.new_x, self.new_y, self.attackingboat_width, self.attackingboat_height), 0)

    def change_stance(self):
        if self.original_stance == "defending" and self.movement == self.steps:
            self.movement -= 1
        if self.movement > 0:
            if self.new_stance == "defending":
                self.new_stance = "attacking"
            else:
                self.new_stance = "defending"

    def move(self, direction):
        if self.new_stance == "attacking":
            if direction == "left":
                if (self.new_x - self.gamegrid.gridx) < self.x:
                    if self.new_x - self.gamegrid.gridx > self.gamegrid.gridstartx:
                        if self.movement > 0:
                            self.new_x -= self.gamegrid.gridx
                            self.movement -= 1
                else:
                    self.movement += 1
                    self.new_x -= self.gamegrid.gridx
            elif direction == "right":
                if (self.new_x + self.gamegrid.gridx) > self.x:
                    if self.new_x + self.gamegrid.gridx < self.gamegrid.gridstartx+self.gamegrid.x:
                        if self.movement > 0:
                            self.new_x += self.gamegrid.gridx
                            self.movement -= 1
                else:
                    self.movement += 1
                    self.new_x += self.gamegrid.gridx
            if direction == "up":
                if (self.new_y - self.gamegrid.gridy) < self.y:
                    if self.new_y - self.gamegrid.gridy > self.gamegrid.gridstarty:
                        if self.movement > 0:
                            self.new_y -= self.gamegrid.gridy
                            self.movement -= 1
                else:
                    self.movement += 1
                    self.new_y -= self.gamegrid.gridy
            if direction == "down":
                if (self.new_y + self.gamegrid.gridy) > self.y:
                    if self.new_y + self.gamegrid.gridy < self.gamegrid.gridstarty+self.gamegrid.y:
                        if self.movement > 0:
                            self.new_y += self.gamegrid.gridy
                            self.movement -= 1
                else:
                    self.movement += 1
                    self.new_y += self.gamegrid.gridy

    def confirm(self):
        self.x = self.new_x
        self.y = self.new_y
        self.original_stance = self.new_stance
        self.movement = self.steps


GameGrid = Grid(display_width, display_height)

positie_boat1_x = GameGrid.gridstartx + ((1 / 6) * GameGrid.gridx)
positie_boat1_y = GameGrid.gridstarty + ((1 / 6) * GameGrid.gridy)
Boat1 = Boat(positie_boat1_x, positie_boat1_y, 2, 3, GameGrid)

positie_boat2_x = GameGrid.gridstartx + ((1 / 6) * GameGrid.gridx * 6)
positie_boat2_y = GameGrid.gridstarty + ((1 / 6) * GameGrid.gridy)
Boat2 = Boat(positie_boat2_x, positie_boat2_y, 3, 3, GameGrid)

positie_boat3_x = GameGrid.gridstartx + ((1 / 6) * GameGrid.gridx * 12)
positie_boat3_y = GameGrid.gridstarty + ((1 / 6) * GameGrid.gridy)
Boat3 = Boat(positie_boat3_x, positie_boat3_y, 4, 3, GameGrid)

positie_boat4_x = GameGrid.gridstartx + ((1 / 6) * GameGrid.gridx * 18)
positie_boat4_y = GameGrid.gridstarty + ((1 / 6) * GameGrid.gridy)
Boat4 = Boat(positie_boat4_x, positie_boat4_y, 5, 3, GameGrid)

P1 = Player("p1", Boat1, Boat2)
P2 = Player("p2", Boat3, Boat4)

Game1 = Game(P1, P1, P2)


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
    elif action == "next_player":
        Game1.nextplayer()

def gamePause():
    paused = True

    pygame.draw.rect(screen, white, (0, display_height*0.3, display_width, display_height*0.1), 0)
    text_to_screen("Het spel is gepauzeerd", black, -display_height*0.15, "medium")

    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False


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
    gameExit = False
    while not gameExit:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameExit = True
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_SPACE:
                     Game1.currentplayer.nextboat()
                 elif event.key == pygame.K_n:
                     Game1.nextplayer()
                     print(Game1)
                 elif event.key == pygame.K_p:
                     gamePause()
                 elif event.key == pygame.K_c:
                     Game1.currentplayer.currentboat.change_stance()
                 elif event.key == pygame.K_RIGHT:
                     Game1.currentplayer.currentboat.move("right")
                 elif event.key == pygame.K_LEFT:
                     Game1.currentplayer.currentboat.move("left")
                 elif event.key == pygame.K_UP:
                     Game1.currentplayer.currentboat.move("up")
                 elif event.key == pygame.K_DOWN:
                     Game1.currentplayer.currentboat.move("down")

         screen.fill(white)
         GameGrid.draw(screen)
         screen.blit(image1, (display_width // 30, display_height // 5))
         screen.blit(image1, (display_width // 30, display_height * 0.6))
         screen.blit(image2, (display_width *0.8, display_height / 2.5))
         for player in Game1.playerlist:
             for boat in player.boatlist:
                 boat.draw(screen)

         Game1.currentplayer.currentboat.draw_new(screen)
         Game1.currentplayer.selectedboat(screen)
         button("Game beëindigen", (display_width/2)-150, (display_height*0.1), 300, 50, red, light_blue, black, "termination_screen")
         if Game1.currentplayer == P1:
            button("Volgende", display_width * 0.825, display_height * 0.83, 190, 60, green, light_blue, black, "next_player")
         if Game1.currentplayer == P2:
            button("Volgende", 0, display_height * 0.83, 190, 60, green, light_blue, black, "next_player")
         button("Hoofdmenu", display_width * 0.825, display_height * 0.9, 190, 60, green, light_blue, black, "main")
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