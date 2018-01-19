import pygame
#import pygame.event
#import pygame.event.type
#from pygame.locals import *
from random import randint
from copy import copy
#-- this is desinged to run on raspberry-pi-display wit no keyboard nor mouse
#-- https://www.raspberrypi.org/blog/the-eagerly-awaited-raspberry-pi-display/
#-- on start tries to load last edited image
#-- touch screen to draw
#-- touch top left  corner to enter color selector
#-- touch top right corner to save image and quit
#-- inside color selector pick color then touch bottom right corner to exit

#-- color predefinitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
blacka=(0,0,0,1)

#-- set screen resolution
sizeX,sizeY=800,480
size=(sizeX,sizeY)
pygame.init()

#-- comment uncoment to select platform
#windowSurface = pygame.display.set_mode(size,pygame.FULLSCREEN)#run on raspi
windowSurface = pygame.display.set_mode(size)#debug on PC

#-- title of window
pygame.display.set_caption('draw2')

#-- set states and constants
buttonSize=5
mouseDown=False
state=0
running=True
palleteBoxSize=10
palleteSaveZone=sizeX-sizeY
color=(randint(0,255),randint(0,255),randint(0,255))
#-- try to load last edited image
try:
	image=pygame.image.load('image.png')
	windowSurface.blit(image,(0,0))
except:
	windowSurface.fill(BLACK)
pygame.display.update()
# run the game loop
while running:
	#-- get mouse position
	mouseX,mouseY=pygame.mouse.get_pos()
	mouse=(mouseX,mouseY)
	#windowSurface.blit(image, (-1,-1))
	if state==0:#-- draw mode
		#-- draw where cursor is
		if mouseDown:pygame.draw.circle(windowSurface,color, mouse, 5, 0)
		#-- draw interface
		pygame.draw.rect(windowSurface, (100,0,0), (sizeX-buttonSize,0,buttonSize,buttonSize))
		pygame.draw.rect(windowSurface, (0,0,100), (0,0,buttonSize,buttonSize))
		#-- if mouse is top right corner to save image and quit
		if mouseX>sizeX-buttonSize and mouseY<buttonSize:running=False
		#-- if mouse is top left enter color selector
		if mouseX<buttonSize and mouseY<buttonSize:
			state=1#-pallete
			#-- save image from screen to variable 
			image=copy(windowSurface)
			#-- blacken screen
			windowSurface.fill(BLACK)
	else:#-- color selector
		#-- draw pallete
		for x in range((sizeX-palleteSaveZone)//palleteBoxSize):
			for y in range(sizeY//palleteBoxSize):
				r=x*1.0/((sizeX-palleteSaveZone)//palleteBoxSize)*255
				b=y*1.0/(sizeY//palleteBoxSize)*255
				pygame.draw.rect(windowSurface,(r,0,b),(x*palleteBoxSize,y*palleteBoxSize,palleteBoxSize,palleteBoxSize))
		#-- draw interface
		pygame.draw.rect(windowSurface, (100,0,100), (sizeX-buttonSize,sizeY-buttonSize,buttonSize,buttonSize))#-exit button
		#-- calculate coordinates of current color
		x=color[0]/255.0*(sizeX-palleteSaveZone)
		y=color[2]/255.0*(sizeY)
		#-- draw color marker
		pygame.draw.rect(windowSurface, (0,0,0), (x,y,buttonSize,buttonSize))#-color cursor
		#-- calculate color from mouse coordinates
		if mouseDown and mouseX<sizeX-palleteSaveZone:#-select new color
			color=(int(mouseX*1.0/((sizeX-palleteSaveZone))*255),0,int(mouseY*1.0/(sizeY)*255))
			pygame.display.set_caption(str(color))
		#-- test for exit to draw mode
		if mouseX>sizeX-buttonSize and mouseY>sizeY-buttonSize:
			state=0#-draw
			windowSurface.blit(image,(0,0))
	#-- update screen
	pygame.display.update()
	#-- convert events to states
	for event in pygame.event.get():
		if event.type == pygame.QUIT:running=False
		elif event.type==pygame.MOUSEBUTTONDOWN:mouseDown=True
		elif event.type==pygame.MOUSEBUTTONUP:mouseDown=False
		elif event.type == pygame.KEYDOWN:
			if event.key==27:running=False#esc
#-- save on exit
pygame.image.save(windowSurface,'image.png')
#-- without this never quits on raspi
pygame.quit()