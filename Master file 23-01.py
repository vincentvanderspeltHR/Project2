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


class Game:
    def __init__(self, firstplayer, P1, P2):
        self.currentplayer = firstplayer
        self.playerlist = [P1, P2]
        self.available_boats = [short_boat1, short_boat2, medium_boat1, medium_boat2, large_boat1, large_boat2]

    def changeplayers(self):
        if self.currentplayer == self.playerlist[0]:
            self.currentplayer = self.playerlist[1]
        else:
            self.currentplayer = self.playerlist[0]

    def nextplayer_ingame(self):
        valid_turn = 0
        for element in self.currentplayer.boatlist:
            if element.confirm() == True:
                valid_turn += 1
        if valid_turn == len(Game1.currentplayer.boatlist):
            for element in self.currentplayer.boatlist:
                element.x = element.new_x
                element.y = element.new_y
                element.original_stance = element.new_stance
                element.movement = element.steps
            self.changeplayers()

    def nextplayer(self):
        for element in self.currentplayer.boatlist:
            element.confirm()
        if self.currentplayer == self.playerlist[0]:
            self.currentplayer = self.playerlist[1]
        else:
            self.currentplayer = self.playerlist[0]

    def __str__(self):
        return str(self.currentplayer.name)


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.boatlist = []
        self.currentboat = 0

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

    def show_stats(self, screen):
        text_to_screen("HP: "+str(Game1.currentplayer.currentboat.currenthp)+"/"+str(Game1.currentplayer.currentboat.hp), black, -display_height*0.45, "small", -display_width*0.45)
        text_to_screen(
            "Steps: " + str(Game1.currentplayer.currentboat.movement) + "/" + str(Game1.currentplayer.currentboat.steps),
            black, -display_height * 0.42, "small", -display_width * 0.435)

class Boat:
    def __init__(self, x, y, length, steps, gamegrid, HP, currentHP, attacking_range_x, attacking_range_y, defending_range_y):
        self.x = x
        self.y = y
        self.new_x = x
        self.new_y = y
        self.switch_x = x
        self.length = length
        self.steps = steps
        self.gamegrid = gamegrid
        self.attackingboat_width = (self.gamegrid.gridx)-(self.gamegrid.gridx/4)
        self.attackingboat_height = ((self.gamegrid.gridy)*self.length - (self.gamegrid.gridx/4))
        self.defendingboat_width = self.attackingboat_height
        self.defendingboat_height = self.attackingboat_width
        self.new_position = (self.new_x, self.new_y, (self.gamegrid.gridx)-(self.gamegrid.gridx/4), ((self.gamegrid.gridy)*self.length - (self.gamegrid.gridx/4)))
        self.original_stance = "attacking"
        self.new_stance = "attacking"
        self.hp = HP
        self.currenthp = currentHP
        self.horizontal_attackingrange = attacking_range_x
        self.vertical_attackingrange = attacking_range_y
        self.horizontal_defendingrange = 0
        self.vertical_defendingrange = defending_range_y
        self.range_buff = 0
        self.damage_buff = 0
        self.emp_buff = 0
        self.flakarmor_buff = 0
        self.movement_multiplier = 1
        self.movement = self.steps*self.movement_multiplier

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
            if self.steps > 1:
                self.movement -= 1
        if self.movement > 0:
            if self.new_stance == "defending":
                if self.switch_x > display_width/2:
                    self.new_x = self.new_x + self.gamegrid.gridx*(self.length - 1)
                self.new_stance = "attacking"
                if Game1.currentplayer == P2:
                    self.new_y = self.new_y - (self.gamegrid.gridy * 0.6) - self.gamegrid.gridy * (self.length - 1) + (self.gamegrid.gridy * 0.6)
                if self.steps == 1 and self.original_stance == "defending":
                    self.movement -= 1
            else:
                if self.switch_x > display_width/2:
                    self.new_x = self.new_x - self.gamegrid.gridx*(self.length - 1)
                self.new_stance = "defending"
                if Game1.currentplayer == P2:
                    self.new_y = self.new_y - (self.gamegrid.gridy * 0.6) + self.gamegrid.gridy * (self.length - 1) + (self.gamegrid.gridy * 0.6)
        elif self.steps == 1 and self.original_stance == "defending":
            self.new_stance = "defending"
            self.movement += 1


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
                    if self.new_y + self.attackingboat_height + self.gamegrid.gridy < self.gamegrid.gridstarty+self.gamegrid.y:
                        if self.movement > 0:
                            self.new_y += self.gamegrid.gridy
                            self.movement -= 1
                else:
                    self.movement += 1
                    self.new_y += self.gamegrid.gridy
        self.switch_x = self.new_x

    def confirm(self):
        for player in Game1.playerlist:
            for boat in player.boatlist:
                tiles = self.steps - 1
                while tiles >= 0:
                    if not boat.x == self.x:
                        if self.new_stance == "attacking":
                            if boat.new_stance == "attacking":
                                if boat.new_x - (self.gamegrid.gridx / 6) < self.new_x < boat.new_x - (
                                    self.gamegrid.gridx / 6) + self.gamegrid.gridx:
                                    if boat.new_y - (
                                        self.gamegrid.gridy / 6) < self.new_y + self.gamegrid.gridy * tiles < boat.new_y - (
                                        self.gamegrid.gridy / 6) + self.gamegrid.gridy * boat.length:  # or boat.new_y-(self.gamegrid.gridy/6) < self.y+self.attackingboat_height < boat.new_y-(self.gamegrid.gridy/6)+self.gamegrid.gridy*boat.length:
                                        return False
                            elif boat.new_stance == "defending":
                                if boat.new_x - (self.gamegrid.gridx / 6) < self.new_x < boat.new_x - (
                                    self.gamegrid.gridx / 6) + self.gamegrid.gridx * boat.length:
                                    if boat.new_y - (
                                        self.gamegrid.gridy / 6) < self.new_y + self.gamegrid.gridy * tiles < boat.new_y - (
                                        self.gamegrid.gridy / 6) + self.gamegrid.gridy:  # or boat.new_y - (self.gamegrid.gridx / 6) < self.new_y+self.attackingboat_height < boat.new_y - (self.gamegrid.gridy / 6) + self.gamegrid.gridy:
                                        return False
                        elif self.new_stance == "defending":
                            if boat.new_stance == "attacking":
                                if boat.new_x - (
                                    self.gamegrid.gridx / 6) < self.new_x + self.gamegrid.gridx * tiles < boat.new_x - (
                                    self.gamegrid.gridx / 6) + self.gamegrid.gridx:  # or boat.new_x-(self.gamegrid.gridx/6) < self.new_x+self.gamegrid.gridx*self.length < boat.new_x-(self.gamegrid.gridx/6)+self.gamegrid.gridx:
                                    if boat.new_y - (self.gamegrid.gridy / 6) < self.new_y < boat.new_y - (
                                        self.gamegrid.gridy / 6) + self.gamegrid.gridy * boat.length:
                                        return False
                            elif boat.new_stance == "defending":
                                if boat.new_x - (
                                    self.gamegrid.gridx / 6) < self.new_x + self.gamegrid.gridx * tiles < boat.new_x - (
                                    self.gamegrid.gridx / 6) + self.gamegrid.gridx:  # or boat.new_x-(self.gamegrid.gridx/6) < self.new_x+self.gamegrid.gridx*self.length < boat.new_x-(self.gamegrid.gridx/6)+self.gamegrid.gridx:
                                    if boat.new_y - (self.gamegrid.gridy / 6) < self.new_y < boat.new_y - (
                                        self.gamegrid.gridy / 6) + self.gamegrid.gridy:
                                        return False
                    tiles -= 1

        return True


GameGrid = Grid(display_width, display_height)


#Posities boten
positie_short_boat1_x = GameGrid.gridstartx + (GameGrid.gridx/6) + GameGrid.gridx*10
positie_short_boat1_y = GameGrid.gridstarty + (GameGrid.gridy/6)

positie_short_boat2_x = GameGrid.gridstartx + (GameGrid.gridx/6) + GameGrid.gridx
positie_short_boat2_y = GameGrid.gridstarty + (GameGrid.gridy/6)

positie_medium_boat1_x = GameGrid.gridstartx + (GameGrid.gridx/6) + 2*GameGrid.gridx
positie_medium_boat1_y = GameGrid.gridstarty + (GameGrid.gridy/6)

positie_medium_boat2_x = GameGrid.gridstartx + (GameGrid.gridx/6) + 3*GameGrid.gridx
positie_medium_boat2_y = GameGrid.gridstarty + (GameGrid.gridy/6)

positie_large_boat1_x = GameGrid.gridstartx + (GameGrid.gridx/6) + 4*GameGrid.gridx
positie_large_boat1_y = GameGrid.gridstarty + (GameGrid.gridy/6)

positie_large_boat2_x = GameGrid.gridstartx + (GameGrid.gridx/6) + 5*GameGrid.gridx
positie_large_boat2_y = GameGrid.gridstarty + (GameGrid.gridy/6)

#Alle boten
short_boat1 = Boat(positie_short_boat1_x, positie_short_boat1_y, 2, 3, GameGrid, 2, 2, 2, 2, 3)
short_boat2 = Boat(positie_short_boat2_x, positie_short_boat2_y, 2, 3, GameGrid, 2, 2, 2, 2, 3)
medium_boat1 = Boat(positie_medium_boat1_x, positie_medium_boat1_y, 3, 2, GameGrid, 3, 3, 3, 3, 4)
medium_boat2 = Boat(positie_medium_boat2_x, positie_medium_boat2_y, 3, 2, GameGrid, 3, 3, 3, 3, 4)
large_boat1 = Boat(positie_large_boat1_x, positie_large_boat1_y, 4, 1, GameGrid, 4, 4, 4, 4, 5)
large_boat2 = Boat(positie_large_boat2_x, positie_large_boat2_y, 4, 1, GameGrid, 4, 4, 4, 4, 5)


P1 = Player("P1")
P2 = Player("P2")

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


def text_to_screen(text, color, y_displace = 0, size = "small", x_displace = 0):
    textSurf, textRect = text_objects(text, color, size)
    textRect.center = (int(display_width / 2)+x_displace, int(display_height / 2)+y_displace)
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
        Game1.nextplayer_ingame()
    elif action == "chooseboats":
        chooseBoats()
    elif action == "shortboat1":
        Game1.currentplayer.boatlist.append(short_boat1)
        Game1.available_boats.remove(short_boat1)
        Game1.nextplayer()
    elif action == "shortboat2":
        Game1.currentplayer.boatlist.append(short_boat2)
        Game1.available_boats.remove(short_boat2)
        Game1.nextplayer()
    elif action == "mediumboat1":
        Game1.currentplayer.boatlist.append(medium_boat1)
        Game1.available_boats.remove(medium_boat1)
        Game1.nextplayer()
    elif action == "mediumboat2":
        Game1.currentplayer.boatlist.append(medium_boat2)
        Game1.available_boats.remove(medium_boat2)
        Game1.nextplayer()
    elif action == "largeboat1":
        Game1.currentplayer.boatlist.append(large_boat1)
        Game1.available_boats.remove(large_boat1)
        Game1.nextplayer()
    elif action == "largeboat2":
        Game1.currentplayer.boatlist.append(large_boat2)
        Game1.available_boats.remove(large_boat2)
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


def chooseBoats():
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        screen.fill(white)
        if len(Game1.available_boats) > 2:
            if short_boat1 in Game1.available_boats:
                button("Short boat 1", display_width / 6, display_height / 2, 190, 50, red, light_blue, black, "shortboat1")
            if short_boat2 in Game1.available_boats:
                button("Short boat 2", display_width / 6 + display_width / 5, display_height / 2, 190, 50, red, light_blue, black, "shortboat2")
            if medium_boat1 in Game1.available_boats:
                button("Medium boat 1", display_width / 6 + 2*display_width / 5, display_height / 2, 190, 50, red, light_blue, black, "mediumboat1")
            if medium_boat2 in Game1.available_boats:
                button("Medium boat 2", display_width / 6, display_height / 2 + display_height / 5, 190, 50, red, light_blue, black, "mediumboat2")
            if large_boat1 in Game1.available_boats:
                button("Large boat 1", display_width / 6 + display_width / 5, display_height / 2 + display_height / 5, 190, 50, red, light_blue, black, "largeboat1")
            if large_boat2 in Game1.available_boats:
                button("Large boat 2", display_width / 6 + 2*display_width / 5, display_height / 2 + display_height / 5, 190, 50, red, light_blue, black, "largeboat2")

        if len(Game1.available_boats) == 2:
            for player in Game1.playerlist:
                player.currentboat = player.boatlist[0]
            text_to_screen("Alle boten zijn gekozen", black, -display_height * 0.35, "medium")
        else:
            text_to_screen((str(Game1)) + ", kies een schip.", black, -(display_height * 0.35), "medium")
        button("Start game", (display_width)-display_width/6, (display_height*0.85), 150, 50, red, light_blue, black, "start")
        button("Hoofdmenu", (display_width)-display_width/6, (display_height*0.75), 150, 50, red, light_blue,black, "main")

        pygame.display.flip()


    pygame.quit()
    quit()


def gameIntro():
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        screen.fill(white)
        text_to_screen("Battleships", black, -(display_height*0.35), "medium")
        button("Start game", (display_width/2)-75 , (display_height*0.35), 150, 50, red, light_blue, black, "chooseboats")
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
         GameGrid.show_stats(screen)

         for player in Game1.playerlist:
             for boat in player.boatlist:
                 boat.draw(screen)

         for element in Game1.currentplayer.boatlist:
             element.draw_new(screen)

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