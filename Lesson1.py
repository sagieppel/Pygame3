import pygame 
import random
pygame.init()
screen=pygame.display.set_mode([700,700])  
for i in range(100000000):
  pygame.draw.circle(screen, [0,255,0], [350,350], 100)
  pygame.display.update()
