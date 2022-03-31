import pygame 
import random

def create(x,y): # Create circle 
    circle={} # Create dictionary
    circle["color"] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    circle["x"] = x
    circle["y"] = y
    circle["size"] = 10
    circle["grow"] = 0
    circle["speedx"] = random.randint(-100,100)/100
    circle["speedy"] = random.randint(-100,100)/100
    return circle


def draw(circle): 
       if   circle["size"]<1:
              circle["grow"]=1
       if circle["size"]>100:
              circle["grow"]=-1
       circle["size"]+=circle["grow"] 
       
       circle["x"] +=  circle["speedx"]
       circle["y"] +=  circle["speedy"]
       pygame.draw.circle(screen, circle["color"] , [int(circle["x"]),int(circle["y"])], int(circle["size"]))

pygame.init() # Set the screen
screensize=700 
screen=pygame.display.set_mode([screensize,screensize])

ar=[] # Set array of circle 

for i in range(1000000):
       screen.fill([0,0,0])
       if len(ar)>500:
             del ar[0]
       
       pygame.event.get()
       x,y = pygame.mouse.get_pos() # Get mouse position
       circle=create(x,y)
       ar.append(circle) # Add circle to array
       for cir in ar: # go over all circle s in array
            draw(cir)
       pygame.display.update()
