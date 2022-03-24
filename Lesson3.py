import pygame 
import random

def create(x,y): # Create circle 
    circle={}
    circle["color"] =  [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    circle["x"] = x
    circle["y"] = y
    circle["radius"] = 10
    circle["grow"]=0.1
    return circle


def draw(circle):
       pygame.draw.circle(screen, circle["color"] , [int(circle["x"]),int(circle["y"])], int(circle["radius"]))



pygame.init() # Set the screen
screensize=700 
screen=pygame.display.set_mode([screensize,screensize])
ar=[]

for i in range(100000):
      # screen.fill([0,0,0])
       pygame.event.get()
       x,y = pygame.mouse.get_pos() # Get mouse position
       circle=create(x,y)
       ar.append(circle)
       #print(x)
       for cir in ar:
            draw(cir)
       pygame.display.update()
