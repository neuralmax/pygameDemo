#-- shadow in the network
import pygame, sys
from random import random,randint
from pygame.locals import *

def safeGet(x,y,d):
	if x>=0 and x<sizeX and y>=0 and y<sizeY:return arr[x][y][d]
	else:return 0
		
dirs=[[
[ 0, 0, 1],
[ 0, 0, 2],
[ 0, 0, 3],
[-1, 0, 0],
[-1,-1, 1],

[ 0,-1, 2],
[ 1,-1, 3],
[ 0,-1, 1],
[ 1,-1, 2],
[ 2,-1, 3],

[ 1, 0, 0],
[ 1, 0, 1],
[ 1, 0, 2],
[ 1, 0, 3],
],[
[ 0, 0, 0],
[ 0, 0, 2],
[ 0, 0, 3],
[-1, 0, 0],
[-1,-1, 1],

[ 0,-1, 2],
[ 1,-1, 3],
[ 0, 1, 0],
[ 1,-1, 2],
[ 2,-1, 3],

[ 1, 0, 2],
[ 2, 0, 3],
[ 1, 1, 0],
[ 1, 1, 1],
[ 1, 1, 2],
[ 1, 1, 3],

]

]
def getNeighbours(x,y,d):
	neighbours=[]
	if d=0:
		neighbours.append()
		
	for dt in range
	neighbours.append
	arr

# set up pygame
pygame.init()

# set up the window
size=(sizeX,sizeY)=(500,260)
gridSz=10
radius=50
nthFrame=100
screen=pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption('gridArt')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen.fill(BLACK)

pygame.draw.line(screen, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(screen, BLUE, (120, 60), (60, 120))
pygame.draw.line(screen, BLUE, (60, 120), (120, 120), 4)

arr=[[[0 for dir in range(4)] for y in range(sizeY//gridSz)] for x in range(sizeX//gridSz)]

pygame.display.update()
frameCnt=0
mousePressed=False
fadeOut=False
starter=[randint(0,sizeX),randint(0,sizeY)]
# run the game loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == K_SPACE:
				fadeOut=True
		elif event.type==pygame.MOUSEBUTTONDOWN:
			mousePressed=True
		elif event.type==pygame.MOUSEBUTTONUP:
			mousePressed=False
	if mousePressed:
		mouseX,mouseY=mousePos=pygame.mouse.get_pos()
		(pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()

			
	screen.fill(BLACK)
	for ix in range(len(arr)):
		for iy in range(len(arr[0])):
			for id in range(len(arr[0][0])):

				if random()<.001:
					if arr[ix][iy][id]==0 and not fadeOut:arr[ix][iy][id]=1
					else:arr[ix][iy][id]=0
				if mousePressed:
					if mouseX-radius<ix*gridSz and mouseX+radius>ix*gridSz and mouseY-radius<iy*gridSz and mouseY+radius>iy*gridSz:
						if random()<.1:arr[ix][iy][id]=0
			if arr[ix][iy][0]==1:pygame.draw.line(screen,WHITE,(ix*gridSz,iy*gridSz),((ix+1)*gridSz,(iy)*gridSz))
			if arr[ix][iy][1]==1:pygame.draw.line(screen,WHITE,(ix*gridSz,iy*gridSz),((ix+1)*gridSz,(iy+1)*gridSz))
			if arr[ix][iy][2]==1:pygame.draw.line(screen,WHITE,(ix*gridSz,iy*gridSz),((ix)*gridSz,(iy+1)*gridSz))
			if arr[ix][iy][3]==1:pygame.draw.line(screen,WHITE,(ix*gridSz,iy*gridSz),((ix-1)*gridSz,(iy+1)*gridSz))
	frameCnt+=1
	#pygame.display.set_caption('gridArt frameCnt:'+str(frameCnt)+' onesCnt'+str(onesCnt)+' rnd'+str(random()>.5))
	pygame.display.update()
	
	#if frameCnt%nthFrame==0:pygame.image.save(screen,'frame'+str(frameCnt//nthFrame)+'.png')
