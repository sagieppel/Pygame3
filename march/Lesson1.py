import pygame 
import random

pygame.init()

screensize=700
screen=pygame.display.set_mode([screensize,screensize]) # Control screen size 

for i in range(100000000):
 # screen.fill(0)
  pygame.event.get()
  x,y = pygame.mouse.get_pos()
  
  red=random.randint(0,255)
  blue=random.randint(0,255)
  green=random.randint(0,255)
  
  x = x+random.randint(-40,40)
  y = y+random.randint(-40,40)
  
  size = random.randint(0,5)
  
  pygame.draw.circle(screen, [red,green,blue], [x,y], size)
  pygame.time.wait(10)
 
  pygame.display.update()
