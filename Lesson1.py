import pygame 
import random

pygame.init()

screensize=700
screen=pygame.display.set_mode([screensize,screensize]) # Control screen size 

for i in range(100000000):
  red=random.randint(0,255)
  blue=random.randint(0,255)
  green=random.randint(0,255)
  
  x = 500
  y = 500
  scale=60
  pygame.draw.circle(screen, [red,green,blue], [x,y], scale)
  pygame.display.update()
