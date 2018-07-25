import pygame, sys
from pygame.locals import *
from random import randint
#-- set screen resolution
size=sizeX,sizeY=800,480
pygame.init()

windowSurface=pygame.display.set_mode(size)
#-- title of window
pygame.display.set_caption('wsDraw')

#-- set states and constants
mouseDown=False
running=True
brushSize=30

# run the game loop
while running:
	#-- convert events to states
	for event in pygame.event.get():
		if event.type == QUIT:running=False
		elif event.type==pygame.MOUSEBUTTONDOWN:mouseDown=True
		elif event.type==pygame.MOUSEBUTTONUP:mouseDown=False
		elif event.type == pygame.KEYDOWN:
			if event.key==K_ESCAPE:running=False#esc
	
	#-- get mouse position
	mouse=mouseX,mouseY=pygame.mouse.get_pos()
	#-- randomise color
	color=(randint(0,255),randint(0,255),randint(0,255))
	#-- draw where cursor is
	if mouseDown:pygame.draw.circle(windowSurface,color, mouse, brushSize, 0)
	#-- update screen
	pygame.display.update()

#-- save on exit
pygame.image.save(windowSurface,'image.png')
#-- without this never quits on raspi
pygame.quit()