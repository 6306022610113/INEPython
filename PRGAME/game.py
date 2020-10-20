
import pgzrun
import random
import string



WIDTH = 800
HEIGHT = 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 62, 30)
a = ['cymbals','violin','guitar','library','office','restroom','art room','mountain',
    'rainbow','river','punk','reggae','blues','auditorium','gymnasium',
    'playground','classical','ambulance','motorcycle','bookstore','restaurant','supermarket']
# LETTER = {"letter": "", "x": 0, "y": 0}
ON_SCREEN_LETTERS = []
VELOCITY = 1
SCORE = {"RIGHT": 0, "WRONG": 0}
def draw():  # Pygame Zero draw function
    screen.clear()
    screen.fill(PINK)
    for LETTER in ON_SCREEN_LETTERS:
        screen.draw.text(LETTER["letter"], (LETTER["x"], LETTER["y"]), fontsize=50, color=WHITE)
    screen.draw.text("RIGHT: " + str(SCORE["RIGHT"]), (WIDTH - 130, 10), fontsize=30, color=WHITE)
    screen.draw.text("WRONG: " + str(SCORE["WRONG"]), (WIDTH - 130, 40), fontsize=30, color=WHITE)
    

def update():
    for i, LETTER in enumerate(ON_SCREEN_LETTERS):
        LETTER["y"] += VELOCITY
        if LETTER["y"] == HEIGHT - 5:
            SCORE["WRONG"] += 1
            delete_letter(i)
    while len(ON_SCREEN_LETTERS) < 4:
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
    letter = random.choice(a).lower()
    x = random.randint(10, WIDTH - 20)
    y = 1
    ON_SCREEN_LETTERS.append({"letter": letter, "x": x, "y": y})

def delete_letter(i):
    del ON_SCREEN_LETTERS[i]
    add_letter()

#def stop():


pgzrun.go()
draw()