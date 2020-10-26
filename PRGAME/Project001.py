import pgzrun
from random import randint, choice
import string

WIDTH = 800
HEIGHT = 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 62, 30)
game_over = False
ON_SCREEN_LETTERS = []
VELOCITY = 1
inter = 0
#toyo = Actor('re',(400,250))
SCORE = {"RIGHT": 0, "WRONG": 0}

def draw():
    #screen.blit(0,0,0)
    #toyo.draw()
    #if inter == 1:
    screen.clear()
        #screen.blit(0,0,0)
    for LETTER in ON_SCREEN_LETTERS:
        screen.draw.text(LETTER["letter"], (LETTER["x"], LETTER["y"]), fontsize=50, color=WHITE)
    screen.draw.text("RIGHT: " + str(SCORE["RIGHT"]), (WIDTH - 130, 10), fontsize=30, color=WHITE)
    screen.draw.text("WRONG: " + str(SCORE["WRONG"]), (WIDTH - 130, 40), fontsize=30, color=WHITE)

    if game_over:
        screen.fill('black')
        message = 'Score : '+str(SCORE["RIGHT"])
        screen.draw.text(message, topleft=(10,10), fontsize=50)

#def on_mouse_down(pos):
#    global inter
#    if toyo.collidepoint(pos):
#        print("yes")
#        inter += 1

def update():
    if inter == 1:
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 5:
                SCORE["WRONG"] += 1
                delete_letter(i)
        while len(ON_SCREEN_LETTERS) < 5:
            add_letter()


def on_key_down(key, mod, unicode):
    if unicode:
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            if LETTER["letter"] == unicode:
                SCORE["RIGHT"] += 1
                delete_letter(i)
                return
        else:
            SCORE["WRONG"] += 1


def add_letter():
    letter = choice(string.ascii_letters).lower()
    x = randint(10, WIDTH - 20)
    y = 1
    ON_SCREEN_LETTERS.append({"letter": letter, "x": x, "y": y})


def delete_letter(i):
    del ON_SCREEN_LETTERS[i]
    add_letter()

def time_up():
    global game_over
    game_over = True

clock.schedule(time_up, 10.0)

pgzrun.go()