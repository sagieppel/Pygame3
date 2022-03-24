import pygame 
import random

def create(x,y): # Create circle 
    circle={}
    circle["color"] =  [145,255,100]
    circle["x"] = x
    circle["y"] = y
    circle["radius"] = 10
    return circle


def draw(circle):
       pygame.draw.circle(screen, circle["color"] , [int(circle["x"]),int(circle["y"])], int(circle["radius"]))



pygame.init() # Set the screen
screensize=700 
screen=pygame.display.set_mode([screensize,screensize])


for i in range(100000):
     #  screen.fill([0,0,0])
       pygame.event.get()
       x,y = pygame.mouse.get_pos() # Get mouse position
       
       circle=create(x,y)
       #print(x)
     
       draw(circle)
       pygame.display.update()
