import pygame 
import random

pygame.init()
screen=pygame.display.set_mode([500,500]) 

for i in range(100000000):
   pygame.draw.circle(screen, [0,0,255], [100,100], 50)
   pygame.display.update()
