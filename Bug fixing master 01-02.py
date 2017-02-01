import pygame
import random
import ctypes

# pygame.mixer.music.load("soundtrack" + str(Game1.soundtrack) + ".wav")
pygame.init()

display_width = 1000
display_height = 800

if display_width<= 1000:
    display_width = 1000
if display_height <= 800:
    display_height = 800

user32 = ctypes.windll.user32

screen = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Menu scherm")

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
image14 = pygame.image.load("Rally.jpg")
image15 = pygame.image.load("reinforced hull.jpg")
image16 = pygame.image.load("Repair.jpg")
image17 = pygame.image.load("Rifling.jpg")
image18 = pygame.image.load("sabotage.jpg")
image19 = pygame.image.load("Smokescreen.jpg")
cardback_original = pygame.image.load("back1.jpg")

settingsCogwheel = pygame.image.load("outline_gearwheel-512.png")
settingsCogwheel_height = int(display_height/20)
settingsCogwheel_width = int(display_width/20)
settingsCogwheel = pygame.transform.scale(settingsCogwheel, [settingsCogwheel_width, settingsCogwheel_height])

sound_on = pygame.image.load("sound_on.png")
sound_on_height = int(display_height/20)
sound_on_width = int(display_width/20)
sound_on = pygame.transform.scale(sound_on, [sound_on_width, sound_on_height])

sound_off = pygame.image.load("sound_off.png")
sound_off_height = int(display_height/20)
sound_off_width = int(display_width/20)
sound_off = pygame.transform.scale(sound_off, [sound_off_width, sound_off_height])



pygame.mixer.music.load("soundtrack1.wav")
card_draw_sound = pygame.mixer.Sound("draw_card_3.ogg")
attack_sound = pygame.mixer.Sound("62.wav")
play_card_sound = pygame.mixer.Sound("Battlecry_1.ogg")
buff_card_sound = pygame.mixer.Sound("1030.wav")
game_error_sound = pygame.mixer.Sound("439.wav")
ship_movement = pygame.mixer.Sound("movement_ship.wav")
button_click = pygame.mixer.Sound("button_click.ogg")

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
light_red = (200,0,0)
light_blue = (0,255,255)
green = (0,255,0)
blue = (0, 50, 200)
yellow = (255, 255, 0)
grey = (128, 128, 128)
brown = (165, 42, 42)


rulesfont = pygame.font.SysFont("centurygothic", 15)
headingfont = pygame.font.SysFont("centurygothic", 20)
smallfont = pygame.font.SysFont("centurygothic", 25)
medfont = pygame.font.SysFont("centurygothic", 50)
largefont = pygame.font.SysFont("centurygothic", 85)
statsfont = pygame.font.SysFont("centurygothic", 13)

game_name = medfont.render("Battleships", True, black)


class Game:
    def __init__(self, firstplayer, P1, P2):
        self.currentplayer = firstplayer
        self.playerlist = [P1, P2]
        self.available_boats = [short_boat1, short_boat2, medium_boat1, medium_boat2, large_boat1, large_boat2, short_boat1_p2, short_boat2_p2, medium_boat1_p2, medium_boat2_p2, large_boat1_p2, large_boat2_p2]
        self.setup_counter = 0
        self.allcards = []
        self.offense_cards = []
        self.defense_cards = []
        self.utility_cards = []
        self.special_cards = []
        self.special_deck = []
        self.normal_deck = []
        self.discard_pile = []
        self.message_show = pygame.time.get_ticks()
        self.message_cooldown = 2500
        self.sound = True
        self.soundtrack = 1
        self.setup = True

    def changeplayers(self):
        if self.currentplayer == self.playerlist[0]:
            self.currentplayer = self.playerlist[1]
        else:
            self.currentplayer = self.playerlist[0]

    def nextplayer_ingame(self):
        valid_turn = 0
        for boat in Game1.currentplayer.boatlist:
            if boat.confirm():
                valid_turn += 1
        if valid_turn == len(Game1.currentplayer.boatlist):
            for element in self.currentplayer.boatlist:
                element.confirm_stats()
            Game1.currentplayer.attack_amount = 2
            self.changeplayers()
            Game1.currentplayer.draw_from_deck(Game1.normal_deck, 1)
        else:
            if Game1.setup_counter == 9:
                text_to_screen("Er zijn boten die elkaar overlappen!", red, -display_height * 0.48)

    def nextplayer_setup(self):
        if self.currentplayer.currentboat.confirm():
            if self.currentplayer.currentboat.new_x > GameGrid.gridstartx:
                self.currentplayer.currentboat.confirm_stats()
                self.currentplayer.nextboat()
                self.changeplayers()
                self.setup_counter += 1
        else:
            text_to_screen("Er staan boten buiten het veld of er overlappen boten!", red, -display_height * 0.48)

    def __str__(self):
        return str(self.currentplayer.name)


class Card:
    def __init__(self, name, image, type, amount):
        self.name = name
        self.image = image
        self.mini_image = pygame.transform.scale(self.image,(int((display_width*0.8)/6), int(display_height*0.15)))
        self.type = type
        self.amount = amount

    def draw_card(self, screen):
        if int((display_width*0.8)/6)*Game1.currentplayer.hand_length + int((display_width*0.8)/6) > pygame.mouse.get_pos()[0] > int((display_width*0.8)/6)*Game1.currentplayer.hand_length and GameGrid.gridstarty * 1.7 + GameGrid.y + int(display_height*0.15) > pygame.mouse.get_pos()[1] > GameGrid.gridstarty * 1.7 + GameGrid.y:
            screen.blit(self.image, [int((display_width * 0.8) / 6) * Game1.currentplayer.hand_length,
                                     GameGrid.gridstarty * 1.7 + GameGrid.y - 379 + int(display_height * 0.02)])
            if pygame.mouse.get_pressed()[0] == 1:
                while pygame.mouse.get_pressed()[0] == 1:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP and int((display_width*0.8)/6)*Game1.currentplayer.hand_length + int((display_width*0.8)/6) > pygame.mouse.get_pos()[0] > int((display_width*0.8)/6)*Game1.currentplayer.hand_length and GameGrid.gridstarty * 1.7 + GameGrid.y + int(display_height*0.15) > pygame.mouse.get_pos()[1] > GameGrid.gridstarty * 1.7 + GameGrid.y:
                            if event.button == 1:
                                if Game1.currentplayer.attack_amount >= 2:
                                    self.perform()
                                    break
                                else:
                                    game_error("Je mag geen kaarten spelen na het aanvallen!")
                                    break
                        else:
                            break
        else:
            screen.blit(pygame.transform.scale(self.image,(int((display_width*0.8)/6), int(display_height*0.15))), [int((display_width*0.8)/6)*Game1.currentplayer.hand_length, GameGrid.gridstarty * 1.7 + GameGrid.y])

    def draw_pick_card(self, screen):
        screen.blit(self.image, [int(display_width/8)*3*(Game1.currentplayer.pick_card_length), int(display_height/2 -198)])
        if int((display_width/8)*3*(Game1.currentplayer.pick_card_length))+261 > pygame.mouse.get_pos()[0] > int(display_width/8)*3*(Game1.currentplayer.pick_card_length) and int(display_height/2 -198)+397 > pygame.mouse.get_pos()[1] > int(display_height/2 -198):
            if pygame.mouse.get_pressed()[0] == 1:
                while pygame.mouse.get_pressed()[0] == 1:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP and int((display_width/8)*3*(Game1.currentplayer.pick_card_length)+261) > pygame.mouse.get_pos()[0] > int((display_width/8)*3*(Game1.currentplayer.pick_card_length)) and int(display_height/2 -198)+397 > pygame.mouse.get_pos()[1] > int(display_height/2 -198):
                            if event.button == 1:
                                if len(Game1.currentplayer.cards_in_hand) >= 6:
                                    game_error("Je hebt al 6 kaarten!")
                                else:
                                    Game1.currentplayer.cards_in_hand.append(self)
                                Game1.currentplayer.pick_cards.remove(self)
                                while len(Game1.currentplayer.pick_cards) > 0:
                                    Game1.special_deck.append(Game1.currentplayer.pick_cards[0])
                                    Game1.currentplayer.pick_cards.remove(Game1.currentplayer.pick_cards[0])
                                break
                        else:
                            break

    def perform(self):
        if self.name == "Advanced Rifling":
            Game1.currentplayer.currentboat.range_buff += 2
            Game1.currentplayer.currentboat.horizontal_attackingrange += Game1.currentplayer.currentboat.range_buff
            Game1.currentplayer.currentboat.vertical_attackingrange += Game1.currentplayer.currentboat.range_buff
            Game1.currentplayer.currentboat.vertical_defendingrange += Game1.currentplayer.currentboat.range_buff
        elif self.name == "Rifling":
            Game1.currentplayer.currentboat.range_buff += 1
            Game1.currentplayer.currentboat.horizontal_attackingrange += Game1.currentplayer.currentboat.range_buff
            Game1.currentplayer.currentboat.vertical_attackingrange += Game1.currentplayer.currentboat.range_buff
            Game1.currentplayer.currentboat.vertical_defendingrange += Game1.currentplayer.currentboat.range_buff
        elif self.name == "FMJ":
            Game1.currentplayer.currentboat.damage_buff += 1
        elif self.name == "Reinforced Hull":
            Game1.currentplayer.currentboat.currenthp += 1
            Game1.currentplayer.currentboat.hp += 1
        elif self.name == "Extra Fuel":
            Game1.currentplayer.currentboat.movement += 1
        elif self.name == "Extra Fuel 2":
            Game1.currentplayer.currentboat.movement += 2
        elif self.name == "Aluminium Hull":
            Game1.currentplayer.currentboat.steps = Game1.currentplayer.currentboat.steps*2
        elif self.name == "Far Sight":
            Game1.currentplayer.currentboat.horizontal_attackingrange += 2
            Game1.currentplayer.currentboat.vertical_attackingrange += 2
            Game1.currentplayer.currentboat.vertical_defendingrange += 2
        elif self.name == "Adrenaline Rush":
            Game1.currentplayer.currentboat.movement = Game1.currentplayer.currentboat.steps
        elif self.name == "Backup":
            Game1.currentplayer.draw_from_deck(Game1.normal_deck, 2)
        elif self.name == "Rally":
            for boat in Game1.currentplayer.boatlist:
                boat.movement += 1
        elif self.name == "Repair":
            Game1.currentplayer.currentboat.currenthp = Game1.currentplayer.currentboat.hp
        elif self.name == "EMP":
            Game1.currentplayer.emp_buff += 1
        elif self.name == "Hack Intel":
            if len(Game1.special_deck) == 0:
                game_error("Er zijn geen special kaarten meer over!")
            if len(Game1.special_deck) >= 3:
                draw_amount = 3
            else:
                draw_amount = len(Game1.special_deck)
            while draw_amount > 0:
                draw_random = random.randint(0, len(Game1.special_deck) - 1)
                Game1.currentplayer.pick_cards.append(Game1.special_deck[draw_random])
                Game1.special_deck.remove(Game1.special_deck[draw_random])
                draw_amount -= 1
        elif self.name == "Sabotage":
            Game1.currentplayer.sabotage_buff += 1
            Game1.currentplayer.trap_cards.append(self)
        else:
            pass
        Game1.currentplayer.cards_in_hand.remove(self)
        if not self.type == "special":
            Game1.discard_pile.append(self)
        if Game1.sound == True:
            pygame.mixer.Sound.play(play_card_sound)



class Player:
    def __init__(self):
        self.name = ""
        self.score = 0
        self.boatlist = []
        self.currentboat = 0
        self.attackable_boats = []
        self.targeted_boat = 0
        self.cards_in_hand = []
        self.pick_cards = []
        self.trap_cards = []
        self.pick_card_length = 0
        self.hand_length = 0
        self.destroyed_boats = []
        self.emp_buff = 0
        self.attack_amount = 2
        self.sabotage_buff = 0

    def show_stats(self, screen):
        text_to_screen("HP: "+str(self.currentboat.currenthp)+"/"+str(self.currentboat.hp), black, -display_height*0.45, "small", -display_width*0.45)
        text_to_screen(
            "Stappen: " + str(self.currentboat.movement) + "/" + str(self.currentboat.steps),
            black, -display_height * 0.425, "small", -display_width * 0.414)
        text_to_screen(
            "Aanval: " + str(self.currentboat.attack_amount) + "/" + str(self.currentboat.original_attack_amount),
            black, -display_height * 0.4, "small", -display_width * 0.422)
        text_to_screen("Totale aanvallen: "+str(Game1.currentplayer.attack_amount)+"/2", black, -display_height*0.375, "rules", -display_width*0.415)

    def show_target_stats(self, screen):
        if Game1.currentplayer == P1:
            enemy = P2
        elif Game1.currentplayer == P2:
            enemy = P1
        display_difference = 0.025

        position = (enemy.boatlist.index(Game1.currentplayer.targeted_boat)+1)
        if position < 3:
            text_to_screen("Schip " + str(position), red,
                           -(display_height * 0.5) + (display_difference * display_height * position * 3), "small",
                           +display_width * 0.35)
            text_to_screen("HP: " + str(self.targeted_boat.currenthp) + "/" + str(self.targeted_boat.hp), red,
                           -(display_height * 0.475) + (display_difference * display_height * position * 3),
                           "small", +display_width * 0.35)
        else:
            text_to_screen("Schip " + str(position), red,
                           -(display_height * 0.5) + (display_difference * display_height * (position-2) * 3), "small",
                           +display_width * 0.45)
            text_to_screen("HP: " + str(self.targeted_boat.currenthp) + "/" + str(self.targeted_boat.hp), red,
                           -(display_height * 0.475) + (display_difference * display_height * (position-2) * 3),
                           "small", +display_width * 0.45)

    def show_enemy_stats(self, screen):
        if Game1.currentplayer == P1:
            enemy = P2
        elif Game1.currentplayer == P2:
            enemy = P1
        display_difference = 0.025
        enemy_boat = 0

        for boat in enemy.boatlist:
            enemy_boat += 1
            if not boat == Game1.currentplayer.targeted_boat:
                if enemy_boat < 3:
                    text_to_screen("Schip "+str(enemy_boat), black,
                                   -(display_height * 0.5) + (display_difference*display_height*enemy_boat*3), "stats", +display_width * 0.35)
                    text_to_screen("HP: " + str(boat.currenthp) + "/" + str(boat.hp), black,
                                   -(display_height * 0.475)+(display_difference*display_height*enemy_boat*3), "stats", +display_width * 0.35)
                else:
                    text_to_screen("Schip " + str(enemy_boat), black,
                                   -(display_height * 0.5) + (display_difference * display_height * (enemy_boat-2) * 3),
                                   "stats", +display_width * 0.45)
                    text_to_screen("HP: " + str(boat.currenthp) + "/" + str(boat.hp), black,
                                   -(display_height * 0.475) + (display_difference * display_height * (enemy_boat-2) * 3),
                                   "stats", +display_width * 0.45)

    def selectedboat(self, screen):
        if self.currentboat.new_stance == "attacking":
            pygame.draw.ellipse(screen, (255, 255, 255), (self.currentboat.new_x, self.currentboat.new_y, (self.currentboat.gamegrid.gridx)-(self.currentboat.gamegrid.gridx/4), ((self.currentboat.gamegrid.gridy)*self.currentboat.length - (self.currentboat.gamegrid.gridx/4))), 4)
        else:
            pygame.draw.ellipse(screen, (255, 255, 255), (self.currentboat.new_x, self.currentboat.new_y, ((self.currentboat.gamegrid.gridy)*self.currentboat.length - (self.currentboat.gamegrid.gridx/4)), (self.currentboat.gamegrid.gridx)-(self.currentboat.gamegrid.gridx/4)), 4)

    def draw_targetedboat(self, screen):
        if self.targeted_boat.new_stance == "attacking":
            pygame.draw.ellipse(screen, (255, 0, 0), (self.targeted_boat.new_x, self.targeted_boat.new_y, (self.targeted_boat.gamegrid.gridx)-(self.targeted_boat.gamegrid.gridx/4), ((self.targeted_boat.gamegrid.gridy)*self.targeted_boat.length - (self.targeted_boat.gamegrid.gridx/4))), 4)
        else:
            pygame.draw.ellipse(screen, (255, 0, 0), (self.targeted_boat.new_x, self.targeted_boat.new_y, ((self.targeted_boat.gamegrid.gridy)*self.targeted_boat.length - (self.targeted_boat.gamegrid.gridx/4)), (self.targeted_boat.gamegrid.gridx)-(self.targeted_boat.gamegrid.gridx/4)), 4)


    def nextboat(self):
        boats = len(Game1.currentplayer.boatlist)
        position = Game1.currentplayer.boatlist.index(Game1.currentplayer.currentboat)
        if boats > 1:
            if position+1 == boats:
                Game1.currentplayer.currentboat = Game1.currentplayer.boatlist[0]
            else:
                Game1.currentplayer.currentboat = Game1.currentplayer.boatlist[position+1]



    def next_attackable_boat(self):
        boats = len(Game1.currentplayer.attackable_boats)
        position = Game1.currentplayer.attackable_boats.index(Game1.currentplayer.targeted_boat)
        if boats > 1:
            if position + 1 == boats:
                Game1.currentplayer.targeted_boat = Game1.currentplayer.attackable_boats[0]
            else:
                Game1.currentplayer.targeted_boat = Game1.currentplayer.attackable_boats[position + 1]

    def attack(self, boat):
        if Game1.sound == True:
            pygame.mixer.Sound.play(attack_sound)

        if Game1.currentplayer == P1:
            enemy = P2
        elif Game1.currentplayer == P2:
            enemy = P1

        if enemy.sabotage_buff > 0:
            Game1.currentplayer.currentboat.currenthp -= (1 + Game1.currentplayer.currentboat.damage_buff)
            game_error("Schade op jezelf gedaan vanwege de sabotage kaart!")
            enemy.sabotage_buff -= 1
            enemy.trap_cards.remove(card_sabotage)
            Game1.discard_pile.append(card_sabotage)
        else:
            boat.currenthp -= (1 + Game1.currentplayer.currentboat.damage_buff)
        if Game1.currentplayer.currentboat.damage_buff > 0:
            Game1.currentplayer.currentboat.damage_buff -= Game1.currentplayer.currentboat.damage_buff
            game_error("Damage buff gebruikt!")
        if Game1.currentplayer.emp_buff > 0:
            game_error("Schip uitgeschakeld met EMP!")
            Game1.currentplayer.targeted_boat.EMP = True
        if boat.currenthp <= 0:
            game_error("Schip van "+str(enemy.name)+" gezonken!")
            enemy.boatlist.remove(boat)
            enemy.destroyed_boats.append(boat)
            if enemy.boatlist == []:
                Game1.currentplayer.score += 1
            else:
                enemy.currentboat = enemy.boatlist[0]
        self.targeted_boat = 0
        self.currentboat.attack_amount = 0
        Game1.currentplayer.attack_amount -= 1
        self.currentboat.range_buff = 0

        Game1.currentplayer.attackable_boats = []
        Game1.currentplayer.targeted_boat = 0

    def draw_from_deck(self, deck, draw_amount):
            while draw_amount > 0:
                if len(deck) > 0:
                    draw_random = random.randint(0, len(deck) - 1)
                    if len(Game1.currentplayer.cards_in_hand) < 6:
                        Game1.currentplayer.cards_in_hand.append(deck[draw_random])
                        deck.remove(deck[draw_random])
                        if Game1.sound == True:
                            pygame.mixer.Sound.play(card_draw_sound)
                    else:
                        if deck == Game1.normal_deck:
                            Game1.discard_pile.append(deck[draw_random])
                        deck.remove(deck[draw_random])
                    draw_amount -= 1
                else:
                    if deck == Game1.normal_deck:
                        deck = Game1.discard_pile
                    else:
                        game_error("Er zijn geen kaarten meer over!")
                        break


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

    def draw_trapcards(self, screen):
        for card in P1.trap_cards:
            cardback = pygame.transform.scale(cardback_original, [int(GameGrid.x / 7), int(GameGrid.gridstarty * 0.75)])
            position = P1.trap_cards.index(card)
            display_trapcard = pygame.transform.scale(card.image,
                                                      [int(GameGrid.x / 7), int(GameGrid.gridstarty * 0.75)])
            if Game1.currentplayer == P1:
                screen.blit(display_trapcard, [int(GameGrid.gridstartx + (GameGrid.x / 7 * position)),
                                               int(GameGrid.gridstarty - GameGrid.gridstarty * 0.75 - 4)])
            else:
                screen.blit(cardback, [int(GameGrid.gridstartx + (GameGrid.x / 7 * position)),
                                       int(GameGrid.gridstarty - GameGrid.gridstarty * 0.75 - 4)])

        for card in P2.trap_cards:
            cardback = pygame.transform.scale(cardback_original, [int(GameGrid.x / 7), int(GameGrid.gridstarty * 0.75)])
            position = P2.trap_cards.index(card)
            display_trapcard = pygame.transform.scale(card.image,
                                                      [int(GameGrid.x / 7), int(GameGrid.gridstarty * 0.75)])
            if Game1.currentplayer == P2:
                screen.blit(display_trapcard, [int(GameGrid.gridstartx + (GameGrid.x / 7 * position)),
                                               int(GameGrid.gridstarty + GameGrid.y + 4)])
            else:
                screen.blit(cardback,
                            [int(GameGrid.gridstartx + (GameGrid.x / 7 * position)),
                             int(GameGrid.gridstarty + GameGrid.y + 4)])

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
        # pygame.draw.rect(screen, black, (self.gridstartx - (display_width*0.135-5)-8, self.gridstarty, display_width*0.135, self.y / 3), 8)
        # pygame.draw.rect(screen, black,(self.gridstartx - (display_width*0.135-5)-8, self.y + self.gridstarty - (self.y / 3), display_width*0.135, self.y / 3), 8)
        # pygame.draw.rect(screen, black, (
        # self.gridstartx + self.x+4, self.gridstarty + (self.y / 10) * 4, self.gridstartx, (self.y / 10) * 2), 8)
        trapcards = 0
        while not trapcards > 6:
            pygame.draw.rect(screen, black, (self.gridstartx + (self.x / 7 * trapcards), self.gridstarty - self.gridstarty * 0.75 -4, self.x / 7,self.gridstarty * 0.75), 8)
            trapcards += 1
        pygame.draw.rect(screen, black, (self.gridstartx, self.gridstarty - self.gridstarty * 0.75 -4, self.x, self.gridstarty*0.75), 8)
        trapcards = 0
        while not trapcards > 6:
            pygame.draw.rect(screen, black, (self.gridstartx + (self.x / 7 * trapcards), self.gridstarty + self.y +4, self.x / 7, self.gridstarty * 0.75),8)
            trapcards += 1
        pygame.draw.rect(screen, black, (self.gridstartx, self.gridstarty +self.y +4, self.x, self.gridstarty * 0.75), 8)
        perkcards = 0
        while not perkcards > 3:
            pygame.draw.rect(screen, black, (self.gridstartx + self.x+4, self.gridstarty + (self.y / 8.2) * perkcards, self.x / 4, self.y / 8.2), 8)
            perkcards += 1
        perkcards = 1
        while not perkcards > 4:
            pygame.draw.rect(screen, black, (self.gridstartx + self.x+4, self.gridstarty + self.y - (self.y / 8.2) * perkcards, self.x / 4, self.y / 8.2),  8)
            perkcards += 1
        pygame.draw.rect(screen, black, (self.gridstartx -4, self.gridstarty-4, self.x+8, self.y+8), 8)
        # if Game1.setup_counter == 9:
        #     if not len(Game1.normal_deck) <= 0:
        #         screen.blit(cardback_normal, [self.gridstartx + self.x+4, self.gridstarty + (self.y / 10) * 4])
        #     if not len(Game1.special_deck) <= 0:
        #

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
        self.range_buff = 0
        self.horizontal_attackingrange = attacking_range_x + self.range_buff
        self.vertical_attackingrange = attacking_range_y + self.range_buff
        self.horizontal_defendingrange = 0
        self.vertical_defendingrange = defending_range_y + self.range_buff
        self.damage_buff = 0
        self.flakarmor_buff = 0
        self.movement = self.steps
        self.original_attack_amount = 1
        self.attack_amount = 1
        self.EMP = False
        self.special_card = 0

    def draw(self, screen, color):
        color = color
        if self.x == Game1.currentplayer.currentboat.x and self.y == Game1.currentplayer.currentboat.y:
            color = green
        if self.original_stance == "attacking":
            pygame.draw.ellipse(screen, color, (self.x, self.y, self.attackingboat_width, self.attackingboat_height), 0)
        elif self.original_stance == "defending":
            pygame.draw.ellipse(screen, color, (self.x, self.y, self.defendingboat_width, self.defendingboat_height), 0)

    def draw_new(self, screen):
        if Game1.setup_counter < 9:
            pygame.draw.ellipse(screen, light_red,(self.new_x, self.new_y, self.attackingboat_width, self.attackingboat_height), 0)
        elif not self.original_stance == self.new_stance and self.new_stance == "defending":
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

    def draw_range(self, screen):
        startpunt_x = self.new_x - (self.gamegrid.gridx / 6)
        startpunt_y = self.new_y - (self.gamegrid.gridy / 6)
        if self.new_stance == "attacking":
            draw_grids = 0
            while not draw_grids == self.horizontal_attackingrange:
                draw_grids += 1
                if startpunt_x - self.gamegrid.gridx * draw_grids < self.gamegrid.gridstartx:
                    break
                else:
                    pygame.draw.rect(screen, yellow, (startpunt_x - self.gamegrid.gridx * draw_grids, startpunt_y, self.gamegrid.gridx, self.gamegrid.gridy * self.length))
                if draw_grids == self.horizontal_attackingrange:
                    break
            draw_grids = 0
            while not draw_grids == self.horizontal_attackingrange:
                draw_grids += 1
                if startpunt_x + self.gamegrid.gridx * (draw_grids+1) > self.gamegrid.gridstartx+self.gamegrid.x:
                    break
                else:
                    pygame.draw.rect(screen, yellow, (startpunt_x + self.gamegrid.gridx * draw_grids, startpunt_y, self.gamegrid.gridx, self.gamegrid.gridy * self.length))
                if draw_grids == self.horizontal_attackingrange:
                    break
            draw_grids = 0
            while not draw_grids == self.vertical_attackingrange:
                draw_grids += 1
                if startpunt_y - self.gamegrid.gridy * draw_grids < self.gamegrid.gridstarty:
                    break
                else:
                    pygame.draw.rect(screen, yellow, (
                    startpunt_x, startpunt_y - self.gamegrid.gridy * draw_grids, self.gamegrid.gridx,
                    self.gamegrid.gridy))
                if draw_grids == self.vertical_attackingrange:
                    break
            draw_grids = 0
            while not draw_grids == self.horizontal_attackingrange:
                draw_grids += 1
                if startpunt_y + self.gamegrid.gridy * (draw_grids+(self.length)) > self.gamegrid.gridstarty+self.gamegrid.y:
                    break
                else:
                    pygame.draw.rect(screen, yellow, (
                    startpunt_x, startpunt_y + self.gamegrid.gridy * (draw_grids+(self.length-1)), self.gamegrid.gridx,
                    self.gamegrid.gridy))
                if draw_grids == self.vertical_attackingrange:
                    break

        if self.new_stance == "defending":
            draw_grids = 0
            while not draw_grids == self.vertical_defendingrange:
                draw_grids += 1
                if startpunt_y - self.gamegrid.gridy * draw_grids < self.gamegrid.gridstarty:
                    break
                else:
                    pygame.draw.rect(screen, yellow, (startpunt_x, startpunt_y - self.gamegrid.gridy * draw_grids, self.gamegrid.gridx*self.length,self.gamegrid.gridy))
                if draw_grids == self.vertical_defendingrange:
                    break
            draw_grids = 0
            while not draw_grids == self.vertical_defendingrange:
                draw_grids += 1
                if startpunt_y + self.gamegrid.gridy * (draw_grids+1) > self.gamegrid.gridstarty+self.gamegrid.y:
                    break
                else:
                    pygame.draw.rect(screen, yellow, (startpunt_x, startpunt_y + self.gamegrid.gridy * draw_grids, self.gamegrid.gridx * self.length, self.gamegrid.gridy))
                if draw_grids == self.vertical_defendingrange:
                    break

    def change_stance(self):
        if self.EMP == True:
            game_error("Schip is uitgeschakeld met EMP!")
        else:
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
                if self.switch_x > display_width / 2:
                    self.new_x = self.new_x - self.gamegrid.gridx * (self.length - 1)
                self.new_stance = "defending"
                self.movement += 1
            else:
                game_error("Niet genoeg stappen over om van positie te wisselen!")


    def move(self, direction):
        if self.EMP == True:
            game_error("Schip is uitgeschakeld met EMP!")
        else:
            if self.new_stance == "attacking":
                if direction == "left":
                    if self.original_stance == "defending" and self.switch_x > display_width/2:
                        if (self.new_x - self.gamegrid.gridx) < self.switch_x:
                            if self.new_x - self.gamegrid.gridx > self.gamegrid.gridstartx:
                                if self.movement > 0:
                                    self.new_x -= self.gamegrid.gridx
                                    self.movement -= 1
                                    if Game1.sound == True:
                                        pygame.mixer.Sound.play(ship_movement)
                            else:
                                game_error("Niet genoeg stappen over om te bewegen!")
                        else:
                            self.movement += 1
                            self.new_x -= self.gamegrid.gridx
                    else:
                        if (self.new_x - self.gamegrid.gridx) < self.x:
                            if self.new_x - self.gamegrid.gridx > self.gamegrid.gridstartx:
                                if self.movement > 0:
                                    self.new_x -= self.gamegrid.gridx
                                    self.movement -= 1
                                    if Game1.sound == True:
                                        pygame.mixer.Sound.play(ship_movement)
                            else:
                                game_error("Niet genoeg stappen over om te bewegen!")
                        else:
                            self.movement += 1
                            self.new_x -= self.gamegrid.gridx
                        self.switch_x = self.new_x
                elif direction == "right":
                    if self.original_stance == "defending" and self.switch_x > display_width/2:
                        if (self.new_x + self.gamegrid.gridx) > self.switch_x:
                            if self.new_x + self.gamegrid.gridx < self.gamegrid.gridstartx+self.gamegrid.x:
                                if self.movement > 0:
                                    self.new_x += self.gamegrid.gridx
                                    self.movement -= 1
                                    if Game1.sound == True:
                                        pygame.mixer.Sound.play(ship_movement)
                            else:
                                game_error("Niet genoeg stappen over om te bewegen!")
                        else:
                            self.movement += 1
                            self.new_x += self.gamegrid.gridx
                    else:
                        if (self.new_x + self.gamegrid.gridx) > self.x:
                            if self.new_x + self.gamegrid.gridx < self.gamegrid.gridstartx+self.gamegrid.x:
                                if self.movement > 0:
                                    self.new_x += self.gamegrid.gridx
                                    self.movement -= 1
                                    if Game1.sound == True:
                                        pygame.mixer.Sound.play(ship_movement)
                            else:
                                game_error("Niet genoeg stappen over om te bewegen!")
                        else:
                            self.movement += 1
                            self.new_x += self.gamegrid.gridx
                        self.switch_x = self.new_x
                elif direction == "up":
                    if Game1.currentplayer == P2 and self.original_stance == "defending":
                        if (self.new_y - self.gamegrid.gridy) < self.y-(self.gamegrid.gridy*(self.length-1)):
                            if self.new_y - self.gamegrid.gridy > self.gamegrid.gridstarty:
                                if self.movement > 0:
                                    self.new_y -= self.gamegrid.gridy
                                    self.movement -= 1
                                    if Game1.sound == True:
                                        pygame.mixer.Sound.play(ship_movement)
                            else:
                                game_error("Niet genoeg stappen over om te bewegen!")
                        else:
                            self.movement += 1
                            self.new_y -= self.gamegrid.gridy
                    elif (self.new_y - self.gamegrid.gridy) < self.y:
                        if self.new_y - self.gamegrid.gridy > self.gamegrid.gridstarty:
                            if self.movement > 0:
                                self.new_y -= self.gamegrid.gridy
                                self.movement -= 1
                                if Game1.sound == True:
                                    pygame.mixer.Sound.play(ship_movement)
                            else:
                                game_error("Niet genoeg stappen over om te bewegen!")
                    else:
                        self.movement += 1
                        self.new_y -= self.gamegrid.gridy
                elif direction == "down":
                    if Game1.currentplayer == P2 and self.original_stance == "defending":
                        if (self.new_y + self.gamegrid.gridy) > self.y-(self.gamegrid.gridy*(self.length-1)):
                            if self.new_y + self.attackingboat_height + self.gamegrid.gridy < self.gamegrid.gridstarty + self.gamegrid.y:
                                if self.movement > 0:
                                    self.new_y += self.gamegrid.gridy
                                    self.movement -= 1
                                    if Game1.sound == True:
                                        pygame.mixer.Sound.play(ship_movement)
                            else:
                                game_error("Niet genoeg stappen over om te bewegen!")
                        else:
                            self.movement += 1
                            self.new_y += self.gamegrid.gridy
                    elif (self.new_y + self.gamegrid.gridy) > self.y:
                        if self.new_y + self.attackingboat_height + self.gamegrid.gridy < self.gamegrid.gridstarty+self.gamegrid.y:
                            if self.movement > 0:
                                self.new_y += self.gamegrid.gridy
                                self.movement -= 1
                                if Game1.sound == True:
                                    pygame.mixer.Sound.play(ship_movement)
                            else:
                                game_error("Niet genoeg stappen over om te bewegen!")
                    else:
                        self.movement += 1
                        self.new_y += self.gamegrid.gridy
                if self.special_card == 0:
                    if not self.y == self.new_y:
                        if Game1.currentplayer == P1:
                            if self.new_y + self.gamegrid.gridy*self.length > self.gamegrid.gridstarty+self.gamegrid.y:
                                self.special_card += 1
                                Game1.currentplayer.draw_from_deck(Game1.special_deck, 1)
                                if len(Game1.special_deck) > 0:
                                    game_error("Speciale kaart getrokken!")
                        else:
                            if self.new_y - self.gamegrid.gridy < self.gamegrid.gridstarty:
                                self.special_card += 1
                                Game1.currentplayer.draw_from_deck(Game1.special_deck, 1)
                                if len(Game1.special_deck) > 0:
                                    game_error("Speciale kaart getrokken!")
                if Game1.sound == True:
                    pygame.mixer.Sound.play(ship_movement)
            else:
                game_error("Verdedigende schepen kunnen niet bewegen!")

    def confirm(self):
        boot = 0
        for player in Game1.playerlist:
            for boat in player.boatlist:
                boot += 1
                tiles = self.length - 1
                if not boat == self:
                    while tiles >= 0:
                            if self.new_stance == "attacking":
                                if boat.new_stance == "attacking":
                                    if boat.new_x - (self.gamegrid.gridx / 6) < self.new_x < boat.new_x - (self.gamegrid.gridx / 6) + self.gamegrid.gridx:
                                        if boat.new_y - (self.gamegrid.gridy / 6) < self.new_y + self.gamegrid.gridy * tiles < boat.new_y - (self.gamegrid.gridy / 6) + self.gamegrid.gridy * boat.length:
                                            if Game1.setup_counter == 9:
                                                game_error("Er zijn overlappende schepen!")
                                            return False
                                elif boat.new_stance == "defending":
                                    if boat.new_x - (self.gamegrid.gridx / 6) < self.new_x < boat.new_x - (
                                        self.gamegrid.gridx / 6) + self.gamegrid.gridx * boat.length:
                                        if boat.new_y - (
                                            self.gamegrid.gridy / 6) < self.new_y + self.gamegrid.gridy * tiles < boat.new_y - (
                                            self.gamegrid.gridy / 6) + self.gamegrid.gridy:
                                            if Game1.setup_counter == 9:
                                                game_error("Er zijn overlappende schepen!")
                                            return False
                            elif self.new_stance == "defending":
                                if boat.new_stance == "attacking":
                                    if boat.new_x - (
                                        self.gamegrid.gridx / 6) < self.new_x + self.gamegrid.gridx * tiles < boat.new_x - (
                                        self.gamegrid.gridx / 6) + self.gamegrid.gridx:
                                        if boat.new_y - (self.gamegrid.gridy / 6) < self.new_y < boat.new_y - (
                                            self.gamegrid.gridy / 6) + self.gamegrid.gridy * boat.length:
                                            if Game1.setup_counter == 9:
                                                game_error("Er zijn overlappende schepen!")
                                            return False
                                elif boat.new_stance == "defending":
                                    if boat.new_x - (
                                        self.gamegrid.gridx / 6) < self.new_x + self.gamegrid.gridx * tiles < boat.new_x - (
                                        self.gamegrid.gridx / 6) + self.gamegrid.gridx:
                                        if boat.new_y - (self.gamegrid.gridy / 6) < self.new_y < boat.new_y - (
                                            self.gamegrid.gridy / 6) + self.gamegrid.gridy:
                                            if Game1.setup_counter == 9:
                                                game_error("Er zijn overlappende schepen!")
                                            return False
                            tiles -= 1
            for boat in player.destroyed_boats:
                boot += 1
                tiles = self.length - 1
                if not boat == self:
                    while tiles >= 0:
                        if self.new_stance == "attacking":
                            if boat.new_stance == "attacking":
                                if boat.new_x - (self.gamegrid.gridx / 6) < self.new_x < boat.new_x - (
                                    self.gamegrid.gridx / 6) + self.gamegrid.gridx:
                                    if boat.new_y - (
                                        self.gamegrid.gridy / 6) < self.new_y + self.gamegrid.gridy * tiles < boat.new_y - (
                                        self.gamegrid.gridy / 6) + self.gamegrid.gridy * boat.length:
                                        if Game1.setup_counter == 9:
                                            game_error("Er zijn overlappende schepen!")
                                        return False
                            elif boat.new_stance == "defending":
                                if boat.new_x - (self.gamegrid.gridx / 6) < self.new_x < boat.new_x - (
                                            self.gamegrid.gridx / 6) + self.gamegrid.gridx * boat.length:
                                    if boat.new_y - (
                                                self.gamegrid.gridy / 6) < self.new_y + self.gamegrid.gridy * tiles < boat.new_y - (
                                                self.gamegrid.gridy / 6) + self.gamegrid.gridy:
                                        if Game1.setup_counter == 9:
                                            game_error("Er zijn overlappende schepen!")
                                        return False
                        elif self.new_stance == "defending":
                            if boat.new_stance == "attacking":
                                if boat.new_x - (
                                            self.gamegrid.gridx / 6) < self.new_x + self.gamegrid.gridx * tiles < boat.new_x - (
                                            self.gamegrid.gridx / 6) + self.gamegrid.gridx:
                                    if boat.new_y - (self.gamegrid.gridy / 6) < self.new_y < boat.new_y - (
                                                self.gamegrid.gridy / 6) + self.gamegrid.gridy * boat.length:
                                        if Game1.setup_counter == 9:
                                            game_error("Er zijn overlappende schepen!")
                                        return False
                            elif boat.new_stance == "defending":
                                if boat.new_x - (
                                            self.gamegrid.gridx / 6) < self.new_x + self.gamegrid.gridx * tiles < boat.new_x - (
                                            self.gamegrid.gridx / 6) + self.gamegrid.gridx:
                                    if boat.new_y - (self.gamegrid.gridy / 6) < self.new_y < boat.new_y - (
                                                self.gamegrid.gridy / 6) + self.gamegrid.gridy:
                                        if Game1.setup_counter == 9:
                                            game_error("Er zijn overlappende schepen!")
                                        return False
                        tiles -= 1

        return True

    def attack_check(self):
        if self.EMP == True:
            game_error("Schip is uitgeschakeld met EMP!")
        else:
            if self.confirm() == True:
                if Game1.currentplayer == P1:
                    enemy = P2
                elif Game1.currentplayer == P2:
                    enemy = P1

                for boat in enemy.boatlist:
                    tiles = boat.length - 1
                    attackable = False
                    while tiles >= 0:
                        if self.new_stance == "attacking":
                            if boat.original_stance == "attacking":
                                if self.new_x-(self.gamegrid.gridx/6)+self.gamegrid.gridx*(self.horizontal_attackingrange+1) > boat.x > self.new_x-(self.gamegrid.gridx/6)-self.gamegrid.gridx*self.horizontal_attackingrange:
                                    if self.new_y-(self.gamegrid.gridy/6)+self.gamegrid.gridy*self.length > boat.y + self.gamegrid.gridy * tiles > self.new_y-(self.gamegrid.gridy/6):
                                        attackable = True
                                if self.new_x-(self.gamegrid.gridx/6)+self.gamegrid.gridx> boat.x > self.new_x-(self.gamegrid.gridx/6):
                                    if self.new_y-(self.gamegrid.gridy/6)+self.gamegrid.gridy*(self.length+self.vertical_attackingrange) > boat.y + self.gamegrid.gridy * tiles > self.new_y-(self.gamegrid.gridy/6)-self.gamegrid.gridy*self.vertical_attackingrange:
                                        attackable = True
                            elif boat.original_stance == "defending":
                                if self.new_x-(self.gamegrid.gridx/6)+self.gamegrid.gridx*(self.horizontal_attackingrange+1) > boat.x + self.gamegrid.gridy * tiles > self.new_x-(self.gamegrid.gridx/6)-self.gamegrid.gridx*self.horizontal_attackingrange:
                                    if self.new_y-(self.gamegrid.gridy/6)+self.gamegrid.gridy*self.length > boat.y > self.new_y-(self.gamegrid.gridy/6):
                                        attackable = True
                                if self.new_x-(self.gamegrid.gridx/6)+self.gamegrid.gridx> boat.x + self.gamegrid.gridy * tiles  > self.new_x-(self.gamegrid.gridx/6):
                                    if self.new_y-(self.gamegrid.gridy/6)+self.gamegrid.gridy*(self.length+self.vertical_attackingrange) > boat.y> self.new_y-(self.gamegrid.gridy/6)-self.gamegrid.gridy*self.vertical_attackingrange:
                                        attackable = True
                        elif self.new_stance == "defending":
                            if boat.original_stance == "attacking":
                                if self.new_x-(self.gamegrid.gridx/6)+(self.gamegrid.gridx*self.length)> boat.x > self.new_x-(self.gamegrid.gridx/6):
                                    if self.new_y-(self.gamegrid.gridy/6)+self.gamegrid.gridy*(self.vertical_defendingrange+1) > boat.y + self.gamegrid.gridy * tiles > self.new_y-(self.gamegrid.gridy/6)-self.gamegrid.gridy*self.vertical_defendingrange:
                                        attackable = True
                            elif boat.original_stance == "defending":
                                if self.new_x-(self.gamegrid.gridx/6)> boat.x + self.gamegrid.gridy * tiles  > self.new_x-(self.gamegrid.gridx/6)+(self.gamegrid.gridx*self.length):
                                    if self.new_y-(self.gamegrid.gridy/6)+self.gamegrid.gridy*(self.vertical_defendingrange+1) > boat.y> self.new_y-(self.gamegrid.gridy/6)-self.gamegrid.gridy*self.vertical_defendingrange:
                                        attackable = True
                        tiles -= 1
                    if attackable:
                        Game1.currentplayer.attackable_boats.append(boat)
                if len(Game1.currentplayer.attackable_boats) == 0:
                    game_error("Er zijn geen boten in de buurt!")

    def confirm_stats(self):
        if self.original_stance == "defending" and self.new_stance == "defending":
            self.switch_x = self.switch_x + (self.new_x - self.x)
        self.x = self.new_x
        self.y = self.new_y
        self.original_stance = self.new_stance
        self.movement = self.steps
        self.attack_amount = self.original_attack_amount
        self.EMP = False
        self.horizontal_attackingrange -= self.range_buff
        self.vertical_attackingrange -= self.range_buff
        self.vertical_defendingrange -= self.range_buff
        self.range_buff = 0

GameGrid = Grid(display_width, display_height)


#Posities boten
positie_short_boat1_x = GameGrid.gridstartx + (GameGrid.gridx/6) -(GameGrid.gridx*1)
positie_short_boat1_y = GameGrid.gridstarty + (GameGrid.gridy/6)
positie_short_boat1_y_p2 = GameGrid.gridstarty + (GameGrid.gridy/6) + (GameGrid.gridy*18)

positie_short_boat2_x = GameGrid.gridstartx + (GameGrid.gridx/6)  -(GameGrid.gridx*1)*2
positie_short_boat2_y = GameGrid.gridstarty + (GameGrid.gridy/6)
positie_short_boat2_y_p2 = GameGrid.gridstarty + (GameGrid.gridy/6) + (GameGrid.gridy*18)

positie_medium_boat1_x = GameGrid.gridstartx + (GameGrid.gridx/6)  -(GameGrid.gridx*1)*3
positie_medium_boat1_y = GameGrid.gridstarty + (GameGrid.gridy/6)
positie_medium_boat1_y_p2 = GameGrid.gridstarty + (GameGrid.gridy/6) + (GameGrid.gridy*17)

positie_medium_boat2_x = GameGrid.gridstartx + (GameGrid.gridx/6)  -(GameGrid.gridx*1)*4
positie_medium_boat2_y = GameGrid.gridstarty + (GameGrid.gridy/6)
positie_medium_boat2_y_p2 = GameGrid.gridstarty + (GameGrid.gridy/6) + (GameGrid.gridy*17)

positie_large_boat1_x = GameGrid.gridstartx + (GameGrid.gridx/6)  -(GameGrid.gridx*1)*5
positie_large_boat1_y = GameGrid.gridstarty + (GameGrid.gridy/6)
positie_large_boat1_y_p2 = GameGrid.gridstarty + (GameGrid.gridy/6) + (GameGrid.gridy*16)

positie_large_boat2_x = GameGrid.gridstartx + (GameGrid.gridx/6)  -(GameGrid.gridx*1)*6
positie_large_boat2_y = GameGrid.gridstarty + (GameGrid.gridy/6)
positie_large_boat2_y_p2 = GameGrid.gridstarty + (GameGrid.gridy/6) + (GameGrid.gridy*16)

#Alle boten
short_boat1 = Boat(positie_short_boat1_x, positie_short_boat1_y, 2, 3, GameGrid, 2, 2, 2, 2, 3)
short_boat2 = Boat(positie_short_boat2_x, positie_short_boat2_y, 2, 3, GameGrid, 2, 2, 2, 2, 3)
medium_boat1 = Boat(positie_medium_boat1_x, positie_medium_boat1_y, 3, 2, GameGrid, 3, 3, 3, 3, 4)
medium_boat2 = Boat(positie_medium_boat2_x, positie_medium_boat2_y, 3, 2, GameGrid, 3, 3, 3, 3, 4)
large_boat1 = Boat(positie_large_boat1_x, positie_large_boat1_y, 4, 1, GameGrid, 4, 4, 4, 4, 5)
large_boat2 = Boat(positie_large_boat2_x, positie_large_boat2_y, 4, 1, GameGrid, 4, 4, 4, 4, 5)

short_boat1_p2 = Boat(positie_short_boat1_x, positie_short_boat1_y_p2, 2, 3, GameGrid, 2, 2, 2, 2, 3)
short_boat2_p2 = Boat(positie_short_boat2_x, positie_short_boat2_y_p2, 2, 3, GameGrid, 2, 2, 2, 2, 3)
medium_boat1_p2 = Boat(positie_medium_boat1_x, positie_medium_boat1_y_p2, 3, 2, GameGrid, 3, 3, 3, 3, 4)
medium_boat2_p2 = Boat(positie_medium_boat2_x, positie_medium_boat2_y_p2, 3, 2, GameGrid, 3, 3, 3, 3, 4)
large_boat1_p2 = Boat(positie_large_boat1_x, positie_large_boat1_y_p2, 4, 1, GameGrid, 4, 4, 4, 4, 5)
large_boat2_p2 = Boat(positie_large_boat2_x, positie_large_boat2_y_p2, 4, 1, GameGrid, 4, 4, 4, 4, 5)

P1 = Player()
P2 = Player()

Game1 = Game(P1, P1, P2)


card_adrenaline_rush = Card("Adrenaline Rush",image1, "utility", 4)
card_advanced_rifling = Card("Advanced Rifling",image2, "offense", 2)
card_aluminium_hull = Card("Aluminium Hull",image3, "special", 1)
card_backup = Card("Backup",image4, "utility", 2)
card_emp = Card("EMP",image5, "offense", 4)
card_extra_fuel_2 = Card("Extra Fuel 2",image6, "utility", 6)
card_extra_fuel = Card("Extra Fuel",image7, "utility", 4)
card_far_sight = Card("Far Sight",image8, "special", 1)
card_fmj = Card("FMJ",image10, "offense", 2)
card_hack_intel = Card("Hack Intel",image11, "special", 1)
card_jack_sparrow = Card("Jack Sparrow",image12, "special", 1)
card_rally = Card("Rally",image14, "utility", 1)
card_reinforced_hull = Card("Reinforced Hull",image15, "defense", 2)
card_repair = Card("Repair",image16, "special", 2)
card_rifling = Card("Rifling",image17, "offense", 2)
card_sabotage = Card("Sabotage",image18, "defense", 2)
card_smokescreen = Card("Smokescreen",image19, "defense", 2)

Game1.allcards = [card_adrenaline_rush, card_advanced_rifling, card_aluminium_hull, card_backup, card_emp, card_extra_fuel_2, card_extra_fuel, card_far_sight, card_fmj, card_hack_intel, card_rally, card_reinforced_hull, card_repair, card_rifling]
for card in Game1.allcards:
        if card.type == "offense":
            Game1.offense_cards.append(card)
            while card.amount > 0:
                Game1.normal_deck.append(card)
                card.amount -= 1
        elif card.type == "defense":
            Game1.defense_cards.append(card)
            while card.amount > 0:
                Game1.normal_deck.append(card)
                card.amount -= 1
        elif card.type == "utility":
            Game1.utility_cards.append(card)
            while card.amount > 0:
                Game1.normal_deck.append(card)
                card.amount -= 1
        elif card.type == "special":
            Game1.special_cards.append(card)
            while card.amount > 0:
                Game1.special_deck.append(card)
                card.amount -= 1


def text_objects(text, color, size = "small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    if size == "rules":
        textSurface = rulesfont.render(text, True, color)
    if size == "stats":
        textSurface = headingfont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def game_error(text):
    Game1.message_show = pygame.time.get_ticks()
    screen.fill(white)
    textSurf, textRect = text_objects(text, red, "small")
    textRect.center = (int(display_width / 2), int(display_height / 2)-display_height*0.48)
    screen.blit(textSurf, textRect)


def text_to_screen(text, color, y_displace = 0, size = "small", x_displace = 0):
    textSurf, textRect = text_objects(text, color, size)
    textRect.center = (int(display_width / 2)+x_displace, int(display_height / 2)+y_displace)
    screen.blit(textSurf, textRect)


def text_to_button(text, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(text, color, size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    screen.blit(textSurf, textRect)


def settings(screen, x, y=0, width=settingsCogwheel_width, height=settingsCogwheel_height):
    screen.blit(settingsCogwheel, [x, y])
    if x+width > pygame.mouse.get_pos()[0] > x and y+height > pygame.mouse.get_pos()[1] > y:
        if pygame.mouse.get_pressed()[0] == 1:
            while pygame.mouse.get_pressed()[0] == 1:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP and x + width > pygame.mouse.get_pos()[0] > x and y + height > pygame.mouse.get_pos()[1] > y:
                        if event.button == 1:
                            do_action("settings")
                            break
                    else:
                        break


def sound_on_function(screen, x, y, width=sound_on_width, height=sound_on_height):
    screen.blit(sound_on, [x, y])
    if x+width > pygame.mouse.get_pos()[0] > x and y+height > pygame.mouse.get_pos()[1] > y:
        if pygame.mouse.get_pressed()[0] == 1:
            while pygame.mouse.get_pressed()[0] == 1:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP and x + width > pygame.mouse.get_pos()[0] > x and y + height > pygame.mouse.get_pos()[1] > y:
                        if event.button == 1:
                            do_action("sound_on")
                            break
                    else:
                        break


def sound_off_function(screen, x, y, width=sound_off_width, height=sound_off_height):
    screen.blit(sound_off, [x, y])
    if x+width > pygame.mouse.get_pos()[0] > x and y+height > pygame.mouse.get_pos()[1] > y:
        if pygame.mouse.get_pressed()[0] == 1:
            while pygame.mouse.get_pressed()[0] == 1:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP and x + width > pygame.mouse.get_pos()[0] > x and y + height > pygame.mouse.get_pos()[1] > y:
                        if event.button == 1:
                            do_action("sound_off")
                            break
                    else:
                        break


def button(text, x, y, width, height, inactive_color, active_color, text_color, action = None):
    if x+width > pygame.mouse.get_pos()[0] > x and y+height > pygame.mouse.get_pos()[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if pygame.mouse.get_pressed()[0] == 1 and action != None:
            while pygame.mouse.get_pressed()[0] == 1:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP and x + width > pygame.mouse.get_pos()[0] > x and y + height > pygame.mouse.get_pos()[1] > y:
                        if event.button == 1:
                            do_action(action)
                            if Game1.sound == True:
                                pygame.mixer.Sound.play(button_click)
                            break
                    else:
                        break
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    text_to_button(text, text_color, x, y, width, height)


def update_shit():
    global display_height
    global display_width
    global GameGrid
    GameGrid = Grid(display_width, display_height)
    GameGrid.draw(screen)
    settings(screen, display_width-settingsCogwheel_width)
    sound_on_function(screen, display_width / 2 - (sound_on_width / 2) + 150,
                      display_height / 2 - (sound_on_height / 2))
    sound_off_function(screen, display_width/2-(sound_off_width/2) + 150, display_height/2-(sound_off_height/2))

    # Posities boten
    global positie_short_boat1_x
    positie_short_boat1_x = GameGrid.gridstartx + (GameGrid.gridx / 6) - (GameGrid.gridx * 1)
    global positie_short_boat1_y
    positie_short_boat1_y = GameGrid.gridstarty + (GameGrid.gridy / 6)
    global positie_short_boat1_y_p2
    positie_short_boat1_y_p2 = GameGrid.gridstarty + (GameGrid.gridy / 6) + (GameGrid.gridy * 18)

    global positie_short_boat2_x
    positie_short_boat2_x = GameGrid.gridstartx + (GameGrid.gridx / 6) - (GameGrid.gridx * 1) * 2
    global positie_short_boat2_y
    positie_short_boat2_y = GameGrid.gridstarty + (GameGrid.gridy / 6)
    global positie_short_boat2_y_p2
    positie_short_boat2_y_p2 = GameGrid.gridstarty + (GameGrid.gridy / 6) + (GameGrid.gridy * 18)

    global positie_medium_boat1_x
    positie_medium_boat1_x = GameGrid.gridstartx + (GameGrid.gridx / 6) - (GameGrid.gridx * 1) * 3
    global positie_medium_boat1_y
    positie_medium_boat1_y = GameGrid.gridstarty + (GameGrid.gridy / 6)
    global positie_medium_boat1_y_p2
    positie_medium_boat1_y_p2 = GameGrid.gridstarty + (GameGrid.gridy / 6) + (GameGrid.gridy * 17)

    global positie_medium_boat2_x
    positie_medium_boat2_x = GameGrid.gridstartx + (GameGrid.gridx / 6) - (GameGrid.gridx * 1) * 4
    global positie_medium_boat2_y
    positie_medium_boat2_y = GameGrid.gridstarty + (GameGrid.gridy / 6)
    global positie_medium_boat2_y_p2
    positie_medium_boat2_y_p2 = GameGrid.gridstarty + (GameGrid.gridy / 6) + (GameGrid.gridy * 17)

    global positie_large_boat1_x
    positie_large_boat1_x = GameGrid.gridstartx + (GameGrid.gridx / 6) - (GameGrid.gridx * 1) * 5
    global positie_large_boat1_y
    positie_large_boat1_y = GameGrid.gridstarty + (GameGrid.gridy / 6)
    global positie_large_boat1_y_p2
    positie_large_boat1_y_p2 = GameGrid.gridstarty + (GameGrid.gridy / 6) + (GameGrid.gridy * 16)

    global positie_large_boat2_x
    positie_large_boat2_x = GameGrid.gridstartx + (GameGrid.gridx / 6) - (GameGrid.gridx * 1) * 6
    global positie_large_boat2_y
    positie_large_boat2_y = GameGrid.gridstarty + (GameGrid.gridy / 6)
    global positie_large_boat2_y_p2
    positie_large_boat2_y_p2 = GameGrid.gridstarty + (GameGrid.gridy / 6) + (GameGrid.gridy * 16)

    # Alle boten
    global short_boat1
    short_boat1 = Boat(positie_short_boat1_x, positie_short_boat1_y, 2, 3, GameGrid, 2, 2, 2, 2, 3)
    global short_boat2
    short_boat2 = Boat(positie_short_boat2_x, positie_short_boat2_y, 2, 3, GameGrid, 2, 2, 2, 2, 3)
    global medium_boat1
    medium_boat1 = Boat(positie_medium_boat1_x, positie_medium_boat1_y, 3, 2, GameGrid, 3, 3, 3, 3, 4)
    global medium_boat2
    medium_boat2 = Boat(positie_medium_boat2_x, positie_medium_boat2_y, 3, 2, GameGrid, 3, 3, 3, 3, 4)
    global large_boat1
    large_boat1 = Boat(positie_large_boat1_x, positie_large_boat1_y, 4, 1, GameGrid, 4, 4, 4, 4, 5)
    global large_boat2
    large_boat2 = Boat(positie_large_boat2_x, positie_large_boat2_y, 4, 1, GameGrid, 4, 4, 4, 4, 5)

    global short_boat1_p2
    short_boat1_p2 = Boat(positie_short_boat1_x, positie_short_boat1_y_p2, 2, 3, GameGrid, 2, 2, 2, 2, 3)
    global short_boat2_p2
    short_boat2_p2 = Boat(positie_short_boat2_x, positie_short_boat2_y_p2, 2, 3, GameGrid, 2, 2, 2, 2, 3)
    global medium_boat1_p2
    medium_boat1_p2 = Boat(positie_medium_boat1_x, positie_medium_boat1_y_p2, 3, 2, GameGrid, 3, 3, 3, 3, 4)
    global medium_boat2_p2
    medium_boat2_p2 = Boat(positie_medium_boat2_x, positie_medium_boat2_y_p2, 3, 2, GameGrid, 3, 3, 3, 3, 4)
    global large_boat1_p2
    large_boat1_p2 = Boat(positie_large_boat1_x, positie_large_boat1_y_p2, 4, 1, GameGrid, 4, 4, 4, 4, 5)
    global large_boat2_p2
    large_boat2_p2 = Boat(positie_large_boat2_x, positie_large_boat2_y_p2, 4, 1, GameGrid, 4, 4, 4, 4, 5)

    global card_adrenaline_rush
    card_adrenaline_rush = Card("Adrenaline Rush", image1, "utility", 4)
    global card_advanced_rifling
    card_advanced_rifling = Card("Advanced Rifling", image2, "offense", 2)
    global card_aluminium_hull
    card_aluminium_hull = Card("Aluminium Hull", image3, "special", 1)
    global card_backup
    card_backup = Card("Backup", image4, "utility", 2)
    global card_emp
    card_emp = Card("EMP", image5, "offense", 4)
    global card_extra_fuel_2
    card_extra_fuel_2 = Card("Extra Fuel 2", image6, "utility", 6)
    global card_extra_fuel
    card_extra_fuel = Card("Extra Fuel", image7, "utility", 4)
    global card_far_sight
    card_far_sight = Card("Far Sight", image8, "special", 1)
    global card_fmj
    card_fmj = Card("FMJ", image10, "offense", 2)
    global card_hack_intel
    card_hack_intel = Card("Hack Intel", image11, "special", 1)
    global card_jack_sparrow
    card_jack_sparrow = Card("Jack Sparrow", image12, "special", 1)
    global card_rally
    card_rally = Card("Rally", image14, "utility", 1)
    global card_reinforced_hull
    card_reinforced_hull = Card("Reinforced Hull", image15, "defense", 2)
    global card_repair
    card_repair = Card("Repair", image16, "special", 2)
    global card_rifling
    card_rifling = Card("Rifling", image17, "offense", 2)
    global card_sabotage
    card_sabotage = Card("Sabotage", image18, "defense", 2)
    global card_smokescreen
    card_smokescreen = Card("Smokescreen", image19, "defense", 2)


def do_action(action):
    if action == "quit":
        pygame.quit()
        quit()
    if action == "high score":
        highScore()
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
    elif action == "next_player":
        Game1.changeplayers()
    elif action == "next_player_setup":
        Game1.nextplayer_setup()
    elif action == "next_player_ingame":
        Game1.nextplayer_ingame()
    elif action == "inputname":
        if len(P1.boatlist) == 4 and len(P2.boatlist) == 4 or Game1.setup_counter > 9:
            gameLoop()
        else:
            inputName()
    elif action == "chooseboats":
        Game1.changeplayers()
        chooseBoats()
    elif action == "shortboat1":
        if Game1.currentplayer == P1:
            Game1.currentplayer.boatlist.append(short_boat1)
            Game1.available_boats.remove(short_boat1)
        else:
            Game1.currentplayer.boatlist.append(short_boat1_p2)
            Game1.available_boats.remove(short_boat1_p2)
    elif action == "shortboat2":
        if Game1.currentplayer == P1:
            Game1.currentplayer.boatlist.append(short_boat2)
            Game1.available_boats.remove(short_boat2)
        else:
            Game1.currentplayer.boatlist.append(short_boat2_p2)
            Game1.available_boats.remove(short_boat2_p2)
    elif action == "mediumboat1":
        if Game1.currentplayer == P1:
            Game1.currentplayer.boatlist.append(medium_boat1)
            Game1.available_boats.remove(medium_boat1)
        else:
            Game1.currentplayer.boatlist.append(medium_boat1_p2)
            Game1.available_boats.remove(medium_boat1_p2)
    elif action == "mediumboat2":
        if Game1.currentplayer == P1:
            Game1.currentplayer.boatlist.append(medium_boat2)
            Game1.available_boats.remove(medium_boat2)
        else:
            Game1.currentplayer.boatlist.append(medium_boat2_p2)
            Game1.available_boats.remove(medium_boat2_p2)
    elif action == "largeboat1":
        if Game1.currentplayer == P1:
            Game1.currentplayer.boatlist.append(large_boat1)
            Game1.available_boats.remove(large_boat1)
        else:
            Game1.currentplayer.boatlist.append(large_boat1_p2)
            Game1.available_boats.remove(large_boat1_p2)
    elif action == "largeboat2":
        if Game1.currentplayer == P1:
            Game1.currentplayer.boatlist.append(large_boat2)
            Game1.available_boats.remove(large_boat2)
        else:
            Game1.currentplayer.boatlist.append(large_boat2_p2)
            Game1.available_boats.remove(large_boat2_p2)
    elif action == "remove_boat":
        Game1.available_boats.append(Game1.currentplayer.boatlist[-1])
        Game1.currentplayer.boatlist.pop()
    elif action == "settings":
        gameSettings()
    elif action == "sound_on":
        Game1.sound = True
        pygame.mixer.music.play()
    elif action == "sound_off":
        Game1.sound = False
        pygame.mixer.music.stop()
    elif action == "1920*1080":
        global display_height
        global display_width
        global screen
        display_width = 1920
        display_height = 1080
        screen = pygame.display.set_mode((display_width, display_height))
        update_shit()
        pygame.display.update()
    elif action == "1000*800":
        display_width = 1000
        display_height = 800
        screen = pygame.display.set_mode((display_width, display_height))
        update_shit()
        pygame.display.update()
    elif action == "fullscreen":
        display_width = int(user32.GetSystemMetrics(0))
        display_height = int(user32.GetSystemMetrics(1))
        screen = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
        update_shit()
        pygame.display.update()


def gameSettings():
    settings_pause = True
    while settings_pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settings_pause = False

        screen.fill(white)
        text_to_screen("Settings", black, -display_height * 0.3, "medium")
        text_to_screen("Sound:", black, -display_height * 0, "small")
        text_to_screen("Resolution:", black, +display_height * 0.2, "small")
        button("1920*1080", display_width-200, display_height*0.8, 200, 80, red, green, black, "1920*1080")
        button("1000*800", 0, display_height*0.8, 200, 80, red, green, black, "1000*800")
        button("Fullscreen", display_width/2 - 100, display_height*0.8, 200, 80, red, green, black, "fullscreen")

        if Game1.sound == True:
            sound_off_function(screen, display_width/2-(sound_off_width/2) + 150, display_height/2-(sound_off_height/2))
        if Game1.sound == False:
            sound_on_function(screen, display_width/2-(sound_on_width/2) + 150, display_height/2-(sound_on_height/2))

        pygame.display.update()

def gamePause():
    paused = True

    pygame.draw.rect(screen, white, (0, display_height*0.3, display_width, display_height*0.1), 0)
    text_to_screen("Het spel is gepauzeerd", black, -display_height*0.15, "medium")
    settings(screen, display_width-settingsCogwheel_width)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False


def inputName():
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            elif event.type == pygame. KEYDOWN:
                if event.key == pygame.K_q:
                    Game1.currentplayer.name += "q"
                elif event.key == pygame.K_w:
                    Game1.currentplayer.name += "w"
                    pygame.display.update()
                elif event.key == pygame.K_e:
                    Game1.currentplayer.name += "e"
                    pygame.display.update()
                elif event.key == pygame.K_r:
                    Game1.currentplayer.name += "r"
                    pygame.display.update()
                elif event.key == pygame.K_t:
                    Game1.currentplayer.name += "t"
                    pygame.display.update()
                elif event.key == pygame.K_y:
                    Game1.currentplayer.name += "y"
                    pygame.display.update()
                elif event.key == pygame.K_u:
                    Game1.currentplayer.name += "u"
                    pygame.display.update()
                elif event.key == pygame.K_i:
                    Game1.currentplayer.name += "i"
                    pygame.display.update()
                elif event.key == pygame.K_o:
                    Game1.currentplayer.name += "o"
                    pygame.display.update()
                elif event.key == pygame.K_p:
                    Game1.currentplayer.name += "p"
                    pygame.display.update()
                elif event.key == pygame.K_a:
                    Game1.currentplayer.name += "a"
                    pygame.display.update()
                elif event.key == pygame.K_s:
                    Game1.currentplayer.name += "s"
                    pygame.display.update()
                elif event.key == pygame.K_d:
                    Game1.currentplayer.name += "d"
                    pygame.display.update()
                elif event.key == pygame.K_f:
                    Game1.currentplayer.name += "f"
                    pygame.display.update()
                elif event.key == pygame.K_g:
                    Game1.currentplayer.name += "g"
                    pygame.display.update()
                elif event.key == pygame.K_h:
                    Game1.currentplayer.name += "h"
                    pygame.display.update()
                elif event.key == pygame.K_j:
                    Game1.currentplayer.name += "j"
                    pygame.display.update()
                elif event.key == pygame.K_k:
                    Game1.currentplayer.name += "k"
                    pygame.display.update()
                elif event.key == pygame.K_l:
                    Game1.currentplayer.name += "l"
                    pygame.display.update()
                elif event.key == pygame.K_z:
                    Game1.currentplayer.name += "z"
                    pygame.display.update()
                elif event.key == pygame.K_x:
                    Game1.currentplayer.name += "x"
                    pygame.display.update()
                elif event.key == pygame.K_c:
                    Game1.currentplayer.name += "c"
                    pygame.display.update()
                elif event.key == pygame.K_v:
                    Game1.currentplayer.name += "v"
                    pygame.display.update()
                elif event.key == pygame.K_b:
                    Game1.currentplayer.name += "b"
                    pygame.display.update()
                elif event.key == pygame.K_n:
                    Game1.currentplayer.name += "n"
                    pygame.display.update()
                elif event.key == pygame.K_m:
                    Game1.currentplayer.name += "m"
                    pygame.display.update()
                elif event.key == pygame.K_SPACE:
                    Game1.currentplayer.name += " "
                elif event.key == pygame.K_BACKSPACE:
                    Game1.currentplayer.name = Game1.currentplayer.name[:-1]
                    pygame.display.update()
        screen.fill(white)
        if Game1.currentplayer == P1:
            text_to_screen("Naam P1: "+ str(Game1.currentplayer.name), black, -display_height*0.35, "medium")
        else:
            text_to_screen("Naam P2: "+ str(Game1.currentplayer.name), black, -display_height*0.35, "medium")
        if Game1.currentplayer.name:
            if Game1.currentplayer == P1:
                button("Volgende", display_width * 0.825, display_height * 0.81, 190, 60, green, light_blue, black,
                       "next_player")
            elif Game1.currentplayer == P2:
                button("Start game", display_width * 0.825, display_height * 0.81, 190, 60, green, light_blue, black, "chooseboats")
        button("Hoofdmenu", display_width * 0.825, display_height * 0.92, 190, 60, green, light_blue, black, "main")
        settings(screen, display_width-settingsCogwheel_width)
        pygame.display.update()

    pygame.quit()
    quit()

def chooseBoats():
    gameExit = False
    while not gameExit:
        if P1.name == "set" and P2.name == "up":
            P1.boatlist = [short_boat1, short_boat2, medium_boat1, medium_boat2]
            P2.boatlist = [short_boat1_p2, short_boat2_p2, medium_boat1_p2, medium_boat2_p2]
            P1.currentboat = P1.boatlist[0]
            P2.currentboat = P2.boatlist[0]
            gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        screen.fill(white)
        # All boat selects
        if len(Game1.available_boats) > 4:
            if len(Game1.currentplayer.boatlist) < 4:
                if (Game1.currentplayer == P1 and len(P1.boatlist) == len(P2.boatlist)):
                    if short_boat1 in Game1.available_boats:
                        button("Kort schip", display_width * 0.15, display_height * 0.3, 220, 50, red, light_blue,
                               black,
                               "shortboat1")
                    if short_boat2 in Game1.available_boats:
                        button("Kort schip", display_width * 0.85 - 190, display_height * 0.3, 220, 50, red,
                               light_blue,
                               black, "shortboat2")
                    if medium_boat1 in Game1.available_boats:
                        button("Gemiddeld schip", display_width * 0.15, display_height * 0.4, 220, 50, red, light_blue,
                               black,
                               "mediumboat1")
                    if medium_boat2 in Game1.available_boats:
                        button("Gemiddeld schip", display_width * 0.85 - 190, display_height * 0.4, 220, 50, red,
                               light_blue,
                               black, "mediumboat2")
                    if large_boat1 in Game1.available_boats:
                        button("Groot schip", display_width * 0.15, display_height * 0.5, 220, 50, red, light_blue,
                               black,
                               "largeboat1")
                    if large_boat2 in Game1.available_boats:
                        button("Groot schip", display_width * 0.85 - 190, display_height * 0.5, 220, 50, red,
                               light_blue,
                               black, "largeboat2")
                if (Game1.currentplayer == P2 and len(P2.boatlist) < len(P1.boatlist)):
                    if short_boat1_p2 in Game1.available_boats:
                        button("Kort schip", display_width * 0.15, display_height * 0.3, 220, 50, red, light_blue,
                               black,
                               "shortboat1")
                    if short_boat2_p2 in Game1.available_boats:
                        button("Kort schip", display_width * 0.85 - 190, display_height * 0.3, 220, 50, red,
                               light_blue,
                               black, "shortboat2")
                    if medium_boat1_p2 in Game1.available_boats:
                        button("Gemiddeld schip", display_width * 0.15, display_height * 0.4, 220, 50, red, light_blue,
                               black,
                               "mediumboat1")
                    if medium_boat2_p2 in Game1.available_boats:
                        button("Gemiddeld schip", display_width * 0.85 - 190, display_height * 0.4, 220, 50, red,
                               light_blue,
                               black, "mediumboat2")
                    if large_boat1_p2 in Game1.available_boats:
                        button("Groot schip", display_width * 0.15, display_height * 0.5, 220, 50, red, light_blue,
                               black,
                               "largeboat1")
                    if large_boat2_p2 in Game1.available_boats:
                        button("Groot schip", display_width * 0.85 - 190, display_height * 0.5, 220, 50, red,
                               light_blue,
                               black, "largeboat2")
        if Game1.currentplayer == P1 and len(P1.boatlist) > len(P2.boatlist):
            button("Volgende", display_width * 0.825, display_height * 0.81, 190, 60, green, light_blue, black,
                   "next_player")
            button("Verwijder gekozen boot", display_width * 0.5 - 250, display_height * 0.75, 500, 50, green, light_blue, black, "remove_boat")

        elif Game1.currentplayer == P2 and len(P1.boatlist) == len(P2.boatlist):
            button("Verwijder gekozen boot", display_width * 0.5 - 250, display_height * 0.75, 500, 50, green, light_blue, black, "remove_boat")
            if len(P2.boatlist) == 4:
                button("Start game", display_width * 0.825, display_height * 0.83, 190, 60, green, light_blue, black,
                    "start")
            else:
                button("Volgende", display_width * 0.825, display_height * 0.81, 190, 60, green, light_blue, black,
                       "next_player")

        if len(Game1.currentplayer.boatlist) > 0:
            Game1.currentplayer.currentboat = Game1.currentplayer.boatlist[0]
        else:
            Game1.currentplayer.currentboat = 0

        if len(Game1.available_boats) > 4:
            text_to_screen((str(Game1)) + ", kies een schip", black, -(display_height * 0.35), "medium")
        else:
            text_to_screen("Druk op start game", black, -(display_height * 0.35), "medium")

        button("Hoofdmenu", display_width * 0.825, display_height * 0.92, 190, 60, green, light_blue, black, "main")
        settings(screen, display_width-settingsCogwheel_width)
        pygame.display.flip()

    pygame.quit()
    quit()


def gameIntro():
    if Game1.sound == True:
        pygame.mixer.music.load("soundtrack" + str(Game1.soundtrack) + ".wav")
        pygame.mixer.music.play()
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        screen.fill(white)
        text_to_screen("Battleships", black, -(display_height*0.35), "medium")
        button("Start game", (display_width/2)-75 , (display_height*0.35), 150, 50, red, light_blue, black, "inputname")
        button("Help", (display_width / 2) - 75, (display_height * 0.45), 150, 50, red, light_blue, black, "rules_main")
        button("Highscore",  (display_width/2)-75, (display_height*0.55), 150, 50, red, light_blue, black, "high score")
        button("Quit", (display_width/2)-75, (display_height*0.65), 150, 50, red, light_blue,black, "quit")

        #screen.blit(card1.image, [50, 50])
        settings(screen, display_width-settingsCogwheel_width)
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
            text_to_screen("Welkom in het regelboek", black, 0, "small", -100)
            text_to_screen("Navigeer met de knoppen hier rechts", black, +50, "rules", -100)

        elif page == "voorbereiding":
            text_to_screen("Welkom op pagina voorbereiding", black, -100, "small", -100)
            text_to_screen("Iedere speler begint met vier schepen", black, -50, "rules", -100)
            text_to_screen("en 2 kaarten van de basis stapel. De spelers", black, -25, "rules", -100)
            text_to_screen("plaatsen hun schepen tegen zijn/haar eigen haven",black, 0, "rules", -100)
            text_to_screen("aan in de aanvalspositie. De speler mag zelf", black, +25, "rules", -100)
            text_to_screen("bepalen waar de schepen staan, zolang ze maar", black, +50, "rules", -100)
            text_to_screen("tegen zijn/haar eigen haven staat.", black, +75, "rules", -100)

        elif page == "spelverloop":
            text_to_screen("Welkom op pagina spelverloop", black, -150, "small", -100)
            text_to_screen("Aan het begin van een speler zijn/haar beurt", black, -100, "rules", -100)
            text_to_screen("trekt de speler één kaart van de normale stapel.", black, -75, "rules", -100)
            text_to_screen("Kaarten mogen alleen gebruikt worden voor het aanvallen.", black, -50, "rules", -100)
            text_to_screen("De speler die aan de beurt is mag zijn schepen verplaatsen,", black, -25, "rules", -100)
            text_to_screen("wanneer een schip van de tegenstander binnen het aanvals", black, 0, "rules", -100)
            text_to_screen("bereik staat van de speler die aan de beurt is staat, mag", black, +25, "rules", -100)
            text_to_screen("de speler die aan de beurt is zijn tegenstanders schip aanvallen.", black, +50, "rules", -100)
            text_to_screen("Er mag per beurt maximaal 2 keer aangevallen worden", black, +75, "rules", -100)
            text_to_screen("en elk schip mag maar maximaal 1 keer per beurt aanvallen.", black, +100, "rules", -100)
            text_to_screen("Met 'a' kun je gaan aanvallen met je geselecteerde boot.", black, +125, "rules", -100)
            text_to_screen("Tijdens het aanvallen kun je eventueel wisselen tussen aan", black, +150, "rules", -100)
            text_to_screen("te vallen schepen met spatie. Met de enter knop val je aan.", black, +175, "rules", -100)
            text_to_screen("met de backspace knop stop je met aanvallen.", black, +200, "rules", -100)


        elif page == "boten":
            text_to_screen("Welkom op pagina boten", black, -150, "small", -100)
            text_to_screen("Er zijn verschillende schepen in dit spel", black, -100, "rules", -100)
            text_to_screen("met elk andere lengtes. Als een schip vernietigt", black, -75, "rules", -100)
            text_to_screen("wordt, zal dit schip op het veld blijven liggen", black, -50, "rules", -100)
            text_to_screen("als obstakel waar niet doorheen gegaan kan", black, -25, "rules", -100)
            text_to_screen("worden. Wanneer een speler al zijn schepen kwijt,", black, 0, "rules", -100)
            text_to_screen("is verliest deze speler. De winnaar is de speler", black, +25, "rules", -100)
            text_to_screen("die als laatste met een niet vernietigt schip", black, +50, "rules", -100)
            text_to_screen("overblijft.", black, +75, "rules", -100)


        elif page == "bewegen & posities":
            text_to_screen("Welkom op pagina bewegen & posities", black, -225, "small", -100)
            text_to_screen("Wanneer een speler aan de beurt is mag de speler", black, -175, "rules", -100)
            text_to_screen("al zijn/haar schepen verplaatsen volgens het aantal", black, -150, "rules", -100)
            text_to_screen("stappen dat het schip kan zetten. Ook kun je de", black, -125, "rules", -100)
            text_to_screen("positie van je schepen veranderen, wanneer je dit", black, -100, "rules", -100)
            text_to_screen("doet telt dat als 1 stap. Wanneer een schip in zijn", black, -75, "rules", -100)
            text_to_screen("aanvalspositie staat heeft het schip zijn standaard", black, -50, "rules", -100)
            text_to_screen("aanval bereik. Wanneer een schip in zijn verdedigingspositie", black, -25, "rules", -100)
            text_to_screen("staat mag deze niet verplaatst worden (Hulpkaarten hebben nog", black, 0, "rules", -100)
            text_to_screen("wel effect). Spelers mogen 2 keer per beurt aanvallen.", black, +25, "rules", -100)
            text_to_screen("Aanvallen kan alleen wanneer een schip van de tegenstander", black, +50, "rules", -100)
            text_to_screen("in het bereik staat van een van jouw schepen. Met de", black, +75, "rules", -100)
            text_to_screen("pijltjestoetsen kan je een boot bewegen. Je kunt", black, +100, "rules", -100)
            text_to_screen("je geselecteerde boot veranderen met spatie.", black, +125, "rules", -100)


        elif page == "kaarten":
            text_to_screen("Welkom op pagina kaarten", black, -125, "small", -100)
            text_to_screen("Er zijn 3 verschillende stapels kaarten in het spel: de basisstapel, speciale stapel", black, -75, "rules", -100)
            text_to_screen("en de weggooistapel. In de basisstapel zitten alle offensieve, defensieve en hulpkaarten.", black, -50, "rules", -100)
            text_to_screen("In de speciale stapel zitten zoals de naam al zegt alle speciale kaarten. Speciale kaarten", black, -25, "rules", -100)
            text_to_screen("zijn meestal pernamente buffs. Alle kaarten die al zijn gebruikt gaan naar de weggooistapel.", black, 0, "rules", -100)
            text_to_screen("Al deze kaarten komen weer terug in het spel zodra de normale stapel leeg is.", black, 25, "rules", -100)

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
        button("Hoofdmenu", display_width*0.75, display_height*0.92, 250, 60, green, light_blue, black, "main")
        settings(screen, display_width-settingsCogwheel_width)
        pygame.display.update()

    pygame.quit()
    quit()


def gameLoop():
     attacking = False
     gameExit = False
     gameOver = False
     while not gameExit:
         now = pygame.time.get_ticks()
         if now - Game1.message_show >= Game1.message_cooldown:
             Game1.message_show = now
             screen.fill(white)

         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameExit = True
             elif event.type == pygame.KEYDOWN and not gameOver:
                 if event.key == pygame.K_p:
                     gamePause()
                 elif event.key == pygame.K_f:
                     P2.boatlist = []
                 if not attacking:
                     if event.key == pygame.K_RIGHT:
                         Game1.currentplayer.currentboat.move("right")
                     elif event.key == pygame.K_LEFT:
                         Game1.currentplayer.currentboat.move("left")
                     elif event.key == pygame.K_t:
                         Game1.currentplayer.cards_in_hand.append(card_sabotage)
                     if not Game1.setup:
                         if event.key == pygame.K_SPACE:
                             Game1.currentplayer.nextboat()
                         elif event.key == pygame.K_c:
                             Game1.currentplayer.currentboat.change_stance()
                         elif event.key == pygame.K_DOWN:
                             Game1.currentplayer.currentboat.move("down")
                         elif event.key == pygame.K_UP:
                             Game1.currentplayer.currentboat.move("up")
                         elif event.key == pygame.K_a:
                             if Game1.currentplayer.currentboat.attack_amount > 0 and Game1.currentplayer.attack_amount > 0:
                                 Game1.currentplayer.currentboat.attack_check()
                                 if len(Game1.currentplayer.attackable_boats) > 0:
                                     attacking = True
                                     Game1.currentplayer.targeted_boat = Game1.currentplayer.attackable_boats[0]
                 elif attacking:
                     if event.key == pygame.K_SPACE:
                         Game1.currentplayer.next_attackable_boat()
                     elif event.key == pygame.K_RETURN:
                         Game1.currentplayer.attack(Game1.currentplayer.targeted_boat)
                         if Game1.sound == True:
                             pygame.mixer.Sound.play(attack_sound)
                         attacking = False
                     elif event.key == pygame.K_BACKSPACE:
                         Game1.currentplayer.targeted_boat = 0
                         attacking = False

         screen.fill(white, (0, display_height*0.06, display_width, display_height))
         screen.fill(white, (0, 0, display_width*0.1, display_height))
         screen.fill(white, (display_width*0.9, 0, display_width*0.1, display_height))

         GameGrid.draw(screen)
         if not Game1.setup:
             Game1.currentplayer.currentboat.draw_range(screen)
             Game1.currentplayer.show_stats(screen)
             Game1.currentplayer.show_enemy_stats(screen)


         for boat in P1.boatlist:
             boat.draw(screen, black)
         for boat in P2.boatlist:
             boat.draw(screen, brown)
         for boat in P1.destroyed_boats:
             boat.draw(screen, grey)
         for boat in P2.destroyed_boats:
             boat.draw(screen, grey)

         if not Game1.setup:
             for element in Game1.currentplayer.boatlist:
                 element.draw_new(screen)

         if Game1.setup or P1.name == "set" and P2.name == "up":
             Game1.currentplayer.currentboat.movement = Game1.currentplayer.currentboat.steps
             Game1.currentplayer.currentboat.attack_amount = Game1.currentplayer.currentboat.original_attack_amount
             Game1.currentplayer.currentboat.draw_new(screen)

         if attacking:
            Game1.currentplayer.show_target_stats(screen)
            Game1.currentplayer.draw_targetedboat(screen)

         GameGrid.draw_trapcards(screen)

         Game1.currentplayer.selectedboat(screen)

         if not gameOver:
             button("Hoofdmenu", display_width * 0.825, display_height * 0.92, 190, 60, green, light_blue, black, "main")

             if Game1.setup:
                 button("Volgende", display_width * 0.825, display_height * 0.81, 190, 60, green, light_blue, black,
                        "next_player_setup")
             else:
                 button("Volgende", display_width * 0.825, display_height * 0.81, 190, 60, green, light_blue, black,
                        "next_player_ingame")

         if Game1.setup_counter == 8:
             Game1.currentplayer.draw_from_deck(Game1.normal_deck, 2)
             Game1.nextplayer_setup()
             Game1.currentplayer.draw_from_deck(Game1.normal_deck, 2)
             Game1.nextplayer_ingame()
             Game1.setup = False
             Game1.setup_counter = 9

         if P1.boatlist == [] or P2.boatlist == []:
             gameOver = True
             button("Highscore", (display_width / 2) - 75, (display_height * 0.45), 150, 50, red, light_blue,
                    black, "high score")

         Game1.currentplayer.hand_length = 0
         for card in Game1.currentplayer.cards_in_hand:
            card.draw_card(screen)
            Game1.currentplayer.hand_length += 1

         Game1.currentplayer.pick_card_length = 0
         for card in Game1.currentplayer.pick_cards:
             card.draw_pick_card(screen)
             Game1.currentplayer.pick_card_length += 1
         settings(screen, display_width-settingsCogwheel_width)
         pygame.display.update()


     pygame.quit()
     quit()


def highScore():
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            screen.fill(white)
            text_to_screen("Highscores", black, -display_height*0.4)
            text_to_screen("Er zijn nog geen scores!", black)
            button("Hoofdmenu", display_width * 0.25, display_height * 0.75, 190, 60, green, light_blue, black, "main")
            button("Quit game", display_width * 0.75-190, display_height * 0.75, 190, 60, green, light_blue, black, "quit")
            settings(screen, display_width-settingsCogwheel_width)
            pygame.display.update()

    pygame.quit()
    quit()

gameIntro()
