import pgzrun
import random
import string

width = 800
height = 400
a = ['cymbals','violin','guitar','library','office','restroom','art room','mountain',
    'rainbow','river','punk','reggae','blues','auditorium','gymnasium',
    'playground','classical','ambulance','motorcycle','bookstore','restaurant','supermarket']

def draw():
    screen.fill('black')
    for LETTER in ON_SCREEN_LETTERS:
        screen.draw.text(LETTER)
def add_letter():
    letter = random.choice(a).lower()

pgzrun.go()
draw()

