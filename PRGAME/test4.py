import pgzrun
WIDTH = 500
HEIGHT = 500
WHITE = (255, 255, 255)
gg = ''
mm = ''
def draw():
     screen.clear()
     screen.draw.text("TEXT: " + str(gg), (100, HEIGHT - 100), fontsize=30, color=WHITE)

def on_key_down(key, mod, unicode):
    global gg

    
    if keyboard.BACKSPACE:
        gg = gg[:-1]
    else:
        gg += unicode

pgzrun.go()