import pgzrun
from random import randint

width = 800
height = 600

score = 0

game_over = False

fox = Actor('fox')
fox.pos = 100,100
coin = Actor('coin')
coin.pos = 200,200

def draw():
    screen.fill('linen')
    fox.draw()
    coin.draw()
    screen.draw.text('Score : '+str(score),color='black', topleft=(10,10))
    if game_over:
        screen.fill('pink')
        message = 'Final Score : '+str(score)
        screen.draw.text(message, topleft=(10,10), fontsize=50)

def place_coin():
    coin.x = randint(20,(width - 20))
    coin.y = randint(20, (height - 20))

def update():
    global score
    if keyboard.left:
        fox.x -= 10
        if fox.x <= 20:
            fox.x = 780
    elif keyboard.right:
        fox.x += 10
        if fox.x >= 780:
            fox.x = 20
    elif keyboard.up:
        fox.y -= 10
        if fox.y <= 20:
            fox.y = 580
    elif keyboard.down:
        fox.y += 10
        if fox.y >= 580:
            fox.y = 20

    
    
    coin_collected = fox.colliderect(coin)
    if coin_collected:
        place_coin()
        score += 1


def time_up():
    global game_over
    game_over = True

clock.schedule(time_up, 60.0)

place_coin()
pgzrun.go()