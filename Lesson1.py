import pygame 
import random

pygame.init()
screensize=700
screen=pygame.display.set_mode([screensize,screensize])  

for i in range(10000000):
  red=random.randint(0,255)
  green=random.randint(0,255)
  blue=random.randint(0,255)
  
  pygame.draw.circle(screen, [red,green,blue], [350,350], 100)
  pygame.display.update()
