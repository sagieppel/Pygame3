import pygame 
import random

pygame.init()

screensize=700
screen=pygame.display.set_mode([screensize,screensize]) # Control screen size 

for i in range(100000000):
  pygame.event.get()
  x,y = pygame.mouse.get_pos()
  
  color = [0 , 200 ,0]
  
  size = 15
  
  pygame.draw.circle(screen, color, [x,y], size)
  
  pygame.display.update()
