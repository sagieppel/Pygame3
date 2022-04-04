import pygame 
import random

def create():
    circle={}
    circle["color"] = [200,255,0]
    circle["x"] = 100
    circle["y"] = 200
    circle["radius"] = 10
    return circle


def draw(circle):
       pygame.draw.circle(screen, circle["color"] , [int(circle["x"]),int(circle["y"])], int(circle["radius"]))


pygame.init()
screensize=600 
screen=pygame.display.set_mode([screensize,screensize])
circle=create()

for i in range(10000):
       screen.fill([0,0,0])
     #  pygame.event.get()
     #  x,y = pygame.mouse.get_pos() # Get mouse position
       draw(circle)
       pygame.display.update()
