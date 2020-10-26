import pgzrun
import pygame as pg
import random

a = ['cymbals','violin','guitar','library','office','restroom','art room','mountain',
    'rainbow','river','punk','reggae','blues','auditorium','gymnasium',
    'playground','classical','ambulance','motorcycle','bookstore','restaurant','supermarket']
pg.init()
screen = pg.display.set_mode((800, 500))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)
game_over = False


def main():
    screen.clear()
    screen.fill(PINK)
    for LETTER in a:    
        screen.draw.text(LETTER["letter"], (LETTER["x"], LETTER["y"]), fontsize=50, color=WHITE)
        screen.draw.text("RIGHT: " + str(SCORE["RIGHT"]), (WIDTH - 130, 10), fontsize=30, color=WHITE)
        screen.draw.text("WRONG: " + str(SCORE["WRONG"]), (WIDTH - 130, 40), fontsize=30, color=WHITE)

    if game_over:
        screen.fill('black')
        message = 'Score : '+str(SCORE["RIGHT"])
        screen.draw.text(message, topleft=(10,10), fontsize=50)

def update():
    if inter == 1:
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 5:
                SCORE["WRONG"] += 1
                delete_letter(i)
        while len(ON_SCREEN_LETTERS) < 5:
            add_letter()

def on_key_down(key, mod):
    input_box = InputBox(300, 400, 200, 32)
    input_boxes = [input_box]
    done = False
    if input_boxes:
        for i, LETTER in enumerate(a):
            if LETTER["letter"] == input_box:
               SCORE["RIGHT"] += 1
               delete_letter(i)
               return
        else:
            SCORE["WRONG"] += 1

def add_letter():
    letter = random.choice(a).lower()
    x = random.randint(100, WIDTH - 200)
    y = 1
    a.append({"letter": letter, "x": x, "y": y})

def delete_letter(i):
    del a[i]
    add_letter()

def time_up():
    global game_over
    game_over = True

clock.schedule(time_up, 10.0)

pgzrun.go()