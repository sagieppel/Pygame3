import pygame 
import random

pygame.init()

screensize=700
screen=pygame.display.set_mode([screensize,screensize]) # Control screen size

enemy={}
enemy["x"]=50
enemy["y"]=50
enemy["color"] = [255,0,0]
enemy["size"] = 30


for i in range(100000000):
  pygame.event.get()
  x,y = pygame.mouse.get_pos()
  
  color = [0, 255, 0]
  size = 15
  
  screen.fill([0,0,0])
  pygame.draw.circle(screen, color , [x,y], size)
  
  
  enemy["x"]+=0.1
  enemy["y"]+=0.3
  pygame.draw.circle(screen, enemy["color"] , [int(enemy["x"]),int(enemy["y"])], enemy["size"])
  
  pygame.display.update()
