import pygame 
import random

def create():
   enemy={}
   enemy["x"]=400
   enemy["y"]=200
   enemy["color"] = [0,255,255]
   enemy["size"] = 100
   return enemy

def move():
  enemy["x"]+=0.1
  enemy["y"]+=0.0
  pygame.draw.circle(screen, enemy["color"] , [int(enemy["x"]),int(enemy["y"])], enemy["size"])
  


pygame.init()

screensize=700
screen=pygame.display.set_mode([screensize,screensize]) # Control screen size

enemy=create()



for i in range(100000000):
  screen.fill([0,0,0])
  
  pygame.event.get()
  x,y = pygame.mouse.get_pos() # Get mouse position
  pcolor = [0, 255, 0]
  psize = 15
  pygame.draw.circle(screen, pcolor , [x,y], psize)
  move()
  
  pygame.display.update()
