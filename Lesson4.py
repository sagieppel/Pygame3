import pygame 
import random
#------------------------------------------
def create():
   enemy={}
   enemy["x"]=200
   enemy["y"]=200
   enemy["color"] = [255,0,0]
   enemy["size"] = 30
   enemy["speedx"] =0.1
   enemy["speedy"] = 0
   return enemy
#------------------------------------------------
def move():
  if enemy["x"]>x:
      enemy["speedx"] = -0.2
  else:
       enemy["speedx"] = 0.2
  
  if enemy["y"]>y:
      enemy["speedy"] = -0.2
  else:
       enemy["speedy"] = 0.2
   
  if abs(enemy["x"]-x)< enemy["size"]:
      if  abs(enemy["y"]-y)< enemy["size"]:
            enemy["color"] = [0,0,255]
  
  enemy["x"]+=enemy["speedx"]
  enemy["y"]+=enemy["speedy"]
  pygame.draw.circle(screen, enemy["color"] , [int(enemy["x"]),int(enemy["y"])], enemy["size"])
#------------------------------------------------------------------

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

  pygame.draw.circle(screen, pcolor , [x,y], psize) # Draw circle at mouse pistion
  
  move() # Move enemy
  pygame.display.update()
