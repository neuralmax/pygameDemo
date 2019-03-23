import pygame, sys
from pygame.locals import *
from random import randint,random
from time import sleep,time
from math import sqrt

def interp(x,xa,xb,ya,yb):
	if xb==xa:return ya+(x-xa)*((yb-ya)/(0.1))
	return ya+(x-xa)*((yb-ya)/(xb-xa))

def drawCube(x,y,h):
	mx=int(cubeSz*1.5)
	cStep=255//hTot
	q=cStep*h
	w=q+cStep
	for i in range(mx):
		clr=(interp(i,0,mx,q,w),0,interp(i,0,mx,255-q,255-w))
		a=[x+cubeSzh*3, y-i]
		b=[x+cubeSzh*4,y+cubeSzh*3-i]
		c=[x+cubeSzh,y+cubeSzh*4-i]
		d=[x+0,y+cubeSzh-i]
		pol=[a,b,c,d]
		pygame.draw.polygon(windowSurface,clr,pol)
def drawPyramid(x,y,h):
	mx=int(cubeSz*1.5)
	for i in range(mx):
		if i%6>3:
			cm=200
			cStep=cm//hTot
			q=cStep*h
			w=q+cStep
			clr=(interp(i,0,mx,q,w),0,interp(i,0,mx,cm-q,cm-w))
		else:
			cStep=255//hTot
			q=cStep*h
			w=q+cStep
			clr=(interp(i,0,mx,q,w),0,interp(i,0,mx,255-q,255-w))
		m=(mx-i)/float(mx)
		a=[x+cubeSzh*2+cubeSzh*m, y+cubeSzh*2-cubeSzh*2*m-i]
		b=[x+cubeSzh*2+cubeSzh*2*m,y+cubeSzh*2+cubeSzh*m-i]
		c=[x+cubeSzh*2-cubeSzh*m,y+cubeSzh*2+cubeSzh*2*m-i]
		d=[x+cubeSzh*2-cubeSzh*2*m,y+cubeSzh*2-cubeSzh*m-i]
		pol=[a,b,c,d]
		pygame.draw.polygon(windowSurface,clr,pol)
def drawDiamond(x,y,h):
	mx=int(cubeSz*1.5)
	for i in range(mx):
		if i%6>3:
			cm=200
			cStep=cm//hTot
			q=cStep*h
			w=q+cStep
			clr=(interp(i,0,mx,q,w),0,interp(i,0,mx,cm-q,cm-w))
		else:
			cStep=255//hTot
			q=cStep*h
			w=q+cStep
			clr=(interp(i,0,mx,q,w),0,interp(i,0,mx,255-q,255-w))
		if i<mx//2:m=interp(i,0,mx/2,0,1)
		else:m=interp(i,mx/2,mx,1,0)
			
		a=[x+cubeSzh*2+cubeSzh*m, y+cubeSzh*2-cubeSzh*2*m-i]
		b=[x+cubeSzh*2+cubeSzh*2*m,y+cubeSzh*2+cubeSzh*m-i]
		c=[x+cubeSzh*2-cubeSzh*m,y+cubeSzh*2+cubeSzh*2*m-i]
		d=[x+cubeSzh*2-cubeSzh*2*m,y+cubeSzh*2-cubeSzh*m-i]
		pol=[a,b,c,d]
		pygame.draw.polygon(windowSurface,clr,pol)


# set up pygame
pygame.init()

# set up the window
sizeX,sizeY=size=1000,800
windowSurface = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption('click more red')

car,cag,cab,cbr,cbg,cbb=0,0,100,0,100,0
cubeSz=30
cubeSzh=cubeSz//2
cubeSza=int(cubeSz*1.5)

pygame.display.update()
mousePressed=False
colorDistance=60
getNext=True
debounce=True
change=0
squareScale=1.0
# run the game loop
showRgb=False
agentProportion=0.1
worldX,worldY,worldZ=25,20,5
agents=[[worldX-1,worldY-1,worldZ-1,0]for i in range(10)]
hTot=worldZ
cubes=[[[0 if random()>0.1 else 1 for x in range(worldX)] for y in range(worldY)] for z in range(worldZ)]
times=[0.1 for n in range(100)]
originX,originY=950,-150
frameCounter=0
imageCounter=0
runing=True
while runing:
	start=time()
	pressed=pygame.key.get_pressed()
	if pressed[pygame.K_a] and car<254:car+=1
	if pressed[pygame.K_s] and cag<254:cag+=1
	if pressed[pygame.K_d] and cab<254:cab+=1
	if pressed[pygame.K_z] and car>1:car-=1
	if pressed[pygame.K_x] and cag>1:cag-=1
	if pressed[pygame.K_c] and cab>1:cab-=1
	
	if pressed[pygame.K_KP4] and cbr<254:cbr+=1
	if pressed[pygame.K_KP5] and cbg<254:cbg+=1
	if pressed[pygame.K_KP6] and cbb<254:cbb+=1
	if pressed[pygame.K_KP1] and cbr>1:cbr-=1
	if pressed[pygame.K_KP2] and cbg>1:cbg-=1
	if pressed[pygame.K_KP3] and cbb>1:cbb-=1
	
	if pressed[pygame.K_UP] and squareScale>0:squareScale-=0.01
	if pressed[pygame.K_DOWN] and squareScale<1:squareScale+=0.01
	if pressed[pygame.K_LEFT]:cubes.append([randint(0,sizeX),randint(0,sizeY)])

	for event in pygame.event.get():
		if event.type == QUIT:runing=False
		elif event.type==pygame.MOUSEBUTTONDOWN:mousePressed=True
		elif event.type==pygame.MOUSEBUTTONUP:mousePressed=False
		elif event.type==pygame.KEYDOWN:
			
			if event.key==K_ESCAPE:runing=False
			if event.key==K_SPACE:cubes=[[[randint(0,1) for x in range(worldX)] for x in range(worldY)] for x in range(worldZ)]
			#if event.key==K_a:
				#if car<254:car+=1

	windowSurface.fill((0,0,0))
	for z,zn in enumerate(cubes):
		for y,yn in enumerate(zn):
			for x,xn in enumerate(yn):
				if xn==1:
					dx=originX-x*cubeSzh*3+y*cubeSzh-x*3+y
					dy=originY+x*cubeSzh+y*cubeSzh*3-z*cubeSza+x+y*3+z*3
					#dx=originX-x*cubeSzh*3+y*cubeSzh
					#dy=originY+x*cubeSzh+y*cubeSzh*3-z*cubeSza
					#dy=originY
					drawCube(dx,dy,z)
				elif xn==2:
					dx=originX-x*cubeSzh*3+y*cubeSzh-x*3+y
					dy=originY+x*cubeSzh+y*cubeSzh*3-z*cubeSza+x+y*3+z*3
					drawPyramid(dx,dy,z)
				elif xn==3:
					dx=originX-x*cubeSzh*3+y*cubeSzh-x*3+y
					dy=originY+x*cubeSzh+y*cubeSzh*3-z*cubeSza+x+y*3+z*3
					drawDiamond(dx,dy,z)
					
					
					
	for i,agent in enumerate(agents):
		if random()<0.2:agent[3]=randint(0,5)
		if i<len(agents)*agentProportion:cubes[agent[2]][agent[1]][agent[0]]=1
		else:cubes[agent[2]][agent[1]][agent[0]]=0
		if agent[3]==0 and agent[0]<worldX-1:agent[0]+=1
		if agent[3]==1 and agent[0]>0:agent[0]-=1
		if agent[3]==2 and agent[1]<worldY-1:agent[1]+=1
		if agent[3]==3 and agent[1]>0:agent[1]-=1
		if agent[3]==4 and agent[2]<worldZ-1:agent[2]+=1
		if agent[3]==5 and agent[2]>0:agent[2]-=1
		#print(agent[0],agent[1],agent[2])
		if i<len(agents)*agentProportion:cubes[agent[2]][agent[1]][agent[0]]=2
		else:cubes[agent[2]][agent[1]][agent[0]]=3
	
	pygame.display.update()
	#sleep(0.005)
	times.pop(0)
	times.append(1/(time()-start))
	fps=int(sum(times)/float(len(times)))
	pygame.display.set_caption('color picker n:'+str(len(cubes))+' fps: '+str(fps))
	frameCounter+=1
	if frameCounter==100:
		pygame.image.save(windowSurface,str(imageCounter)+'image.png')
		imageCounter+=1
		frameCounter=0
		if imageCounter==100:runing=False
		
pygame.image.save(windowSurface,'image.png')
pygame.quit()
sys.exit()
