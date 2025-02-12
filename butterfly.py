import pgzrun
from random import randint

WIDTH = 500
HEIGHT= 500

butterfly =Actor("butterfly")
butterfly.pos = 100,100

def draw():
    screen.blit("forest",(0,0))
    butterfly.draw()
    
pgzrun.go()
    
