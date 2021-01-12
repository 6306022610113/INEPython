import pgzrun
import pygame
from random import randint, choice
import string

WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

bgbutton = pygame.display.set_mode((WIDTH,HEIGHT))

image = pygame.image.load(r'PRGAME\images\img1.jpg')
image1 = pygame.image.load(r'PRGAME\images\img2.jpg')
image2 = pygame.image.load(r'PRGAME\images\img3.jpg')
image3 = pygame.image.load(r'PRGAME\images\img4.jpg')
image4 = pygame.image.load(r'PRGAME\images\img5.jpg')

run = True

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,screen,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 48)
            text = font.render(self.text, 1, (255,255,255))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

startbutton = button((0,0,0),100,170,200,50, 'START')
leaderbutton = button((0,0,0),100,250,200,50, 'BOARD')
exitbutton = button((0,0,0),100,330,200,50, 'EXIT')
easybutton = button((0,0,0),300,200,200,50, 'EASY')
normalbutton = button((0,0,0),300,250,200,50, 'NORMAL')
hardbutton = button((0,0,0),300,300,200,50, 'HARD')
puasebutton = button((0,0,0),600,530,120,50, 'PUASE')
homebutton = button((0,0,0),150,480,200,50, 'HOME')
menubutton = button((0,0,0),300,450,200,50, 'EXIT')
resumebutton = button((0,0,0),300,200,200,50, 'RESUME')
startbutton1 = 0
leaderbutton1 = 0
exitbutton1 = 0
easybutton1 = 0
puasebutton1 = 0
menubutton1 = 0
resumebutton1 = 0
normalbutton1 = 0
hardbutton1 = 0
homebutton1 = 0  
puasebutton1 = 0

vocab = ['cat','dog','ant','fox','face','mask','drop','bag','bird','bad','good']

vocab2 = ['dancer','bread','candy','bingo','chest','night','china','yellow','black','arrive']

vocab3 = ['carefully','quickly','science','rectangle','headache','america','blanket','clothes'
        ,'airport','bathroom','birthday','morning']

# LETTER = {"letter": "", "x": 0, "y": 0}
ON_SCREEN_LETTERS = []
VELOCITY = 2
SCORE = {"RIGHT": 0, "WRONG": 0}
WORD_FONT_SIZE = 50
MODE_EASY = 1
MODE_NORMAL = 1
WORD_LENGTH = 0
game_over = False


def draw():  # Pygame Zero draw function
    global SCORE ,ON_SCREEN_LETTERS
    screen.clear()
    bgbutton.blit(image,(0,0))
    startbutton.draw(bgbutton,(0,0,0))
    leaderbutton.draw(bgbutton,(0,0,0))
    exitbutton.draw(bgbutton,(0,0,0))
    """
    SCORE["RIGHT"] = 0
    SCORE["WRONG"] = 0
    ON_SCREEN_LETTERS = []
    """
    if startbutton1 == 1:
        screen.clear()
        bgbutton.blit(image4,(0,0))
        easybutton.draw(bgbutton,(0,0,0))
        normalbutton.draw(bgbutton,(0,0,0))
        hardbutton.draw(bgbutton,(0,0,0))
        homebutton.draw(bgbutton,(0,0,0))
        if easybutton1 == 1 or normalbutton1 == 1 or hardbutton1 == 1 :
            screen.clear()
            bgbutton.blit(image3,(0,0))
            puasebutton.draw(bgbutton,(0,0,0))
            for LETTER in ON_SCREEN_LETTERS:
                screen.draw.text(LETTER["letter"], (LETTER["x"], LETTER["y"]), fontsize=WORD_FONT_SIZE, color=WHITE)
            screen.draw.text("RIGHT: " + str(SCORE["RIGHT"]), (WIDTH - 130, 10), fontsize=30, color=WHITE)
            screen.draw.text("WRONG: " + str(SCORE["WRONG"]), (WIDTH - 130, 40), fontsize=30, color=WHITE)

        if game_over:
            bgbutton.blit(image2,(0,0))
            message = 'Score : '+str(SCORE["RIGHT"])
            screen.draw.text(message, topleft=(300,200),fontsize=50, color=WHITE)
            menubutton.draw(bgbutton,(0,0,0))
        
    if puasebutton1 == 1:
        bgbutton.fill((0,0,0))
        bgbutton.blit(image4,(0,0))
        resumebutton.draw(bgbutton,(0,0,0))
        menubutton.draw(bgbutton,(0,0,0))
       
  

    if exitbutton1 == 1:
        pygame.quit()
        quit()      


def update():
    if startbutton1 == 1 and easybutton1 == 1: 
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 5:
                SCORE["WRONG"] += 1
                delete_letter(i)
        if MODE_EASY == 1:
            while WORD_LENGTH < 1:
            # while len(WORD_LENGTH) < 1:
                add_letter()

    if startbutton1 == 1 and normalbutton1 == 1: 
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 5:
                SCORE["WRONG"] += 1
                delete_letter(i)
        if MODE_EASY == 1:
            while WORD_LENGTH < 1:
            # while len(WORD_LENGTH) < 1:
                add_letter()

    if startbutton1 == 1 and hardbutton1 == 1: 
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 5:
                SCORE["WRONG"] += 1
                delete_letter(i)
        if MODE_EASY == 1:
            while WORD_LENGTH < 1:
            # while len(WORD_LENGTH) < 1:
                add_letter()


def on_key_down(key, mod, unicode):
    print(unicode)
    if unicode:
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            if LETTER["letter"] == unicode:
                SCORE["RIGHT"] += 1
                delete_letter(i)
                return
        else:
            SCORE["WRONG"] += 1


def add_letter():
    #letter = choice(string.ascii_letters).lower()
    #x = randint(10, WIDTH - 20)
    #y = 1
    #ON_SCREEN_LETTERS.append({"letter": letter, "x": x, "y": y})
    global WORD_LENGTH,startbutton1,easybutton1,normalbutton1
    # letter = choice(string.ascii_letters).lower()
    if startbutton1 == 1 and easybutton1 == 1:
        letter = choice(vocab).lower()
        padding = WORD_FONT_SIZE / 2 
        x = randint(10, 600)
        for i, LETTER in enumerate(letter):
            y = i-1 
            ON_SCREEN_LETTERS.append({"letter": LETTER, "x": x + (i * padding), "y": y})
        WORD_LENGTH += 1

    if normalbutton1 == 1 and startbutton1 == 1 :
        letter = choice(vocab2).lower()
        padding = WORD_FONT_SIZE / 2 
        x = randint(10, 600)
        for i, LETTER in enumerate(letter):
            y = i-1 
            ON_SCREEN_LETTERS.append({"letter": LETTER, "x": x + (i * padding), "y": y})
        WORD_LENGTH += 1
    
    if hardbutton1 == 1 and startbutton1 == 1 :
        letter = choice(vocab3).lower()
        padding = WORD_FONT_SIZE / 2 
        x = randint(10, 600)
        for i, LETTER in enumerate(letter):
            y = i-1 
            ON_SCREEN_LETTERS.append({"letter": LETTER, "x": x + (i * padding), "y": y})
        WORD_LENGTH += 1
     
def delete_letter(i):
    global WORD_LENGTH
    del ON_SCREEN_LETTERS[i]
    if len(ON_SCREEN_LETTERS) < 1:
        add_letter()

def time_up():
    global game_over
    game_over = True

clock.schedule(time_up, 180.0)

def on_mouse_down(pos):
    global startbutton1,leaderbutton1,exitbutton1,easybutton1,normalbutton1,hardbutton1,homebutton1,run,puasebutton1
    global SCORE ,ON_SCREEN_LETTERS
    while run:
        draw()
        pygame.display.update()
    #    button = pygame.Rect(100,170,200,50)
    #    button1 = pygame.rect(100,250,200,50)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
    #        mouse = pygame.mouse.get_pos()
    #        click = pygame.mouse.get_pressed()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if puasebutton1 != 1 and startbutton1 < 1:
                    if startbutton.isOver(pos):
                        if startbutton1 < 1:
                            startbutton1 += 1
                            return startbutton1
                if exitbutton1 <= 1:
                    if exitbutton.isOver(pos):
                        exitbutton1 += 1
                        SCORE["RIGHT"] = 0
                        SCORE["WRONG"] = 0
                        ON_SCREEN_LETTERS = []
                        
#           __________________________________________
                if easybutton1 != 1 and normalbutton1 != 1 and hardbutton1 != 1:             
                    if easybutton1 <= 1 and startbutton1 == 1:
                        if easybutton.isOver(pos):
                            easybutton1 += 1
                            return easybutton1
                           # add_letter()
                    if normalbutton1 <= 1 and startbutton1 == 1:
                        if normalbutton.isOver(pos):
                            normalbutton1 += 1
                            return normalbutton1
                    if hardbutton1 <= 1 and startbutton1 == 1:
                        if hardbutton.isOver(pos):
                            hardbutton1 += 1
                            return hardbutton1
#           __________________________________________   
                if startbutton1 == 1:
                    if puasebutton.isOver(pos):
                        if puasebutton1 >= 0 and puasebutton1 < 1:
                            puasebutton1 += 1
                if homebutton1 <= 1 :
                    if homebutton.isOver(pos):
                        if startbutton1 == 1:
                            startbutton1 -= 1
                            return startbutton1
                if puasebutton1 == 1:
                    if resumebutton.isOver(pos):
                        if startbutton1 == 1 and menubutton1 != 1:
                            puasebutton1 -= 1
                            return puasebutton1
                if menubutton1 < 1:
                    if menubutton.isOver(pos):
                        if startbutton1 == 1:
                            startbutton1 -= 1
                            return startbutton1
                        if easybutton1 == 1:
                            easybutton1 -= 1
                            return easybutton1
                        if normalbutton1 == 1:
                            normalbutton1 -= 1
                            return normalbutton1
                        if hardbutton1 == 1:
                            hardbutton1 -= 1
                            return hardbutton1
                        if puasebutton1 == 1:
                            puasebutton1 -= 1
                            return puasebutton1
                    

            

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

    #def mouse_touch(pos):
    #    for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                if startbutton.isOver(pos):
                    startbutton.color = (0,128,0)
                else :
                    startbutton.color = (0,0,0)
        #           ____________________________________
                if leaderbutton.isOver(pos):
                    leaderbutton.color = (128,128,0)
                else :
                    leaderbutton.color = (0,0,0)
        #           ____________________________________
                if exitbutton.isOver(pos):
                    exitbutton.color = (128,0,0)
                else:
                    exitbutton.color = (0,0,0)
        #           ____________________________________
                if easybutton.isOver(pos):
                    easybutton.color = (0,0,128)
                else:
                    easybutton.color = (0,0,0)
        #           ____________________________________
                if normalbutton.isOver(pos):
                    normalbutton.color = (0,0,128)
                else:
                    normalbutton.color = (0,0,0)
        #           ____________________________________
                if hardbutton.isOver(pos):
                    hardbutton.color = (0,0,128)
                else:
                    hardbutton.color = (0,0,0)
        #           ____________________________________
                if homebutton.isOver(pos):
                    homebutton.color = (0,0,128)
                else:
                    homebutton.color = (0,0,0)
        #           ____________________________________
                if puasebutton.isOver(pos):
                    puasebutton.color = (0,0,128)
                else:
                    puasebutton.color = (0,0,0)
        #           ____________________________________
                if menubutton.isOver(pos):
                    menubutton.color = (0,0,128)
                else:
                    menubutton.color = (0,0,0)
        #           ____________________________________
                if resumebutton.isOver(pos):
                    resumebutton.color = (0,0,128)
                else:
                    resumebutton.color = (0,0,0)
        #           ____________________________________

pgzrun.go()