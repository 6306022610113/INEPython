import pygame 
import pgzrun
import random
import string


WIDTH = 800
HEIGHT = 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

image = pygame.image.load(r'PRGAME\images\BG5.jpg')
image1 = pygame.image.load(r'PRGAME\images\index2.jpg')
image2 = pygame.image.load(r'PRGAME\images\index3.jpg')

start = Actor('start')
start.pos = 390,200
start1 = 0
le = Actor('leader')
le.pos = 380,290
leader = 0
exit1 = Actor('exit')
exit1.pos = 378,370
exit2 = 0
easy = Actor('easy')
easy.pos = 200,300
easy1 = 0
normal = Actor('normal')
normal.pos = 350,300
normal1 = 0
hard = Actor('hard')
hard.pos = 500,300
hard1 = 0
pause = Actor('pause')
pause.pos = 700,480
con = Actor('conti')
replay = Actor('replay')
endgame = ('exit2')
pause1 = 0

vocab = ['cat','dog','ant','fox','face','mask','drop','bag','bird','bad','good']

vocab2 = ['dancer','bread','candy','bingo','chest','night','china','yellow','black','arrive']

vocab3 = ['carefully','quickly','science','rectangle','headache','america','blanket','clothes'
        ,'airport','bathroom','birthday','morning']

VELOCITY = 1
ON_SCREEN_LETTERS = []
SCORE = {"RIGHT": 0, "WRONG": 0}
trip = ''
mm = ''

def draw():
    screen.fill((0,0,0))
    screen.blit(image1,(0,0))
    start.draw()
    le.draw()
    exit1.draw()
    
    if start1 == 1:
        screen.clear()
        easy.draw()
        normal.draw()
        hard.draw()

    if easy1 == 1 or normal1 == 1 or hard1 == 1:
        screen.clear()
        screen.blit(image2,(0,0))
        pause.draw()
        for LETTER in ON_SCREEN_LETTERS:
            screen.draw.text(LETTER["letter"], (LETTER["x"], LETTER["y"]), fontsize=50, color=WHITE)
        screen.draw.text("RIGHT: " + str(SCORE["RIGHT"]), (WIDTH - 130, 10), fontsize=30, color=WHITE)
        screen.draw.text("WRONG: " + str(SCORE["WRONG"]), (WIDTH - 130, 40), fontsize=30, color=WHITE)
        screen.draw.text("VOCABULARY: " + str(trip), (10, HEIGHT - 30), fontsize=30, color=WHITE)
    if pause1 == 1:
        screen.clear()
        screen.blit(image,(0,0))
        con.draw()
        con.pos = 540,100
        endgame.draw()
        endgame.pos = 540,300
        replay.draw()
        replay.pos = 540, 500
#    if exit == 1:
#        screen.clear()
#        screen.blit('endback',(0,0))
#        playagain.draw()
#        screen.draw.text("CORRECT: " + str(SCORE["CORRECT"]), (WIDTH - 570, 200), fontsize=50, color=WHITE)
#        screen.draw.text("WRONG: " + str(SCORE["WRONG"]), (WIDTH - 550, 300), fontsize=50, color=WHITE)
#    if SCORE["WRONG"] == 3:
#       pause1 = 1
#        exit = 1

def on_mouse_down(pos):
    global pause1,start1,exit2,easy1,normal1,hard1,leader,ON_SCREEN_LETTERS
    if pause1 != 1 and start1 <= 1:
       if start.collidepoint(pos):
            if start1 >= 0 and start1 < 1:
                start1 += 1
    if easy1 != 1 and  normal1 != 1 and hard1 != 1:
        if easy.collidepoint(pos):
            if start1 == 1 and easy1 < 1:
                easy1 += 1
        if normal.collidepoint(pos):
            if start1 == 1 and normal1 < 1:
                normal1 += 1
        if hard.collidepoint(pos):
            if start1 == 1 and hard1 < 1:
                hard1 += 1
    if start1 == 1:
        if pause.collidepoint(pos):
            if pause1 >= 0 and pause1 < 1:
                pause1 += 1
#    if pause1 == 1:
#        if resumegame.collidepoint(pos):
#            if start1 == 1 and exit2 != 1:
#                pause1 -= 1
#    if pause1 == 1:
#        if replaygame.collidepoint(pos):
#            if start1 == 1 and exit2 != 1:
#               SCORE["RIGHT"] = 0 
#                SCORE["WRONG"] = 0
#                ON_SCREEN_LETTERS = []
#                pause1 -= 1
    if pause1 == 1:
        if exit1.collidepoint(pos):
            if exit2 >= 0 and exit2 < 1:
                exit2 += 1
#    if SCORE["WRONG"] == 1 or exit2 == 1:
#        if playagain.collidepoint(pos):
#            if playagain2 >= 0 and playagain2 < 1:
#                if start1 == 1:
#                    start1 = 0
#                if exit2 == 1:
#                   exit2 -= 1
#               if pause1 == 1:
#                    pause1 -= 1
#                if easy1 == 1:
#                    easy1 = 0
#                if normal1 == 1:
#                    normal1 = 0
#                if hard1 == 1:
#                    hard1 = 0
#               SCORE["RIGHT"] = 0 
#                SCORE["WRONG"] = 0
#               ON_SCREEN_LETTERS = []
            

def update():
    if start1 == 1 and pause1 != 1 and easy1 == 1:
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 5:
                SCORE["WRONG"] += 1
                delete_letter(i)
        while len(ON_SCREEN_LETTERS) < 1:
            add_letter()

    if start1 == 1 and pause1 != 1 and normal1 == 1:
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 5:
                SCORE["WRONG"] += 1
                delete_letter(i)
        while len(ON_SCREEN_LETTERS) < 1:
            add_letter()

    if start1 == 1 and pause1 != 1 and hard1 == 1:
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 5:
                SCORE["WRONG"] += 1
                delete_letter(i)
        while len(ON_SCREEN_LETTERS) < 1:
            add_letter()
            
def on_key_down(key, mod, unicode):
    global trip
    if keyboard.BACKSPACE:
        trip = trip[:-1]
    else:
        trip += unicode

    for i, LETTER in enumerate(ON_SCREEN_LETTERS):
        if LETTER["letter"] == trip:
            SCORE["RIGHT"] += 1
            delete_letter(i)
            trip = ''
            return

def add_letter():
    if start1 == 1 and easy1 == 1:
        letter = random.choice(vocab).lower()
        x = random.randint(100, WIDTH - 250)
        y = 1
        ON_SCREEN_LETTERS.append({"letter": letter, "x": x, "y": y})
    if start1 == 1 and normal1 == 1:
        letter = random.choice(vocab2).lower()
        x = random.randint(10, WIDTH - 100)
        y = 1
        ON_SCREEN_LETTERS.append({"letter": letter, "x": x, "y": y})
    if start1 == 1 and hard1 == 1:
        letter = random.choice(vocab3).lower()
        x = random.randint(10, WIDTH - 100)
        y = 1
        ON_SCREEN_LETTERS.append({"letter": letter, "x": x, "y": y})


def delete_letter(i):
    del ON_SCREEN_LETTERS[i]
    add_letter()

pgzrun.go()