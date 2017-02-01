import numpy as np
import cv2
from rootGen import getGrid, quadTree
roots=quadTree()
grid=getGrid()
img = np.zeros((512,512,3), np.uint8)
pathcolor=[0 for x in range(3)]
pathcolor[1]=0

def drawPath(posx,posy,dirr):
	if(dirr==0):
		for x in range(8):
			for z in range(3):
				img[posy][posx][z]=pathcolor[z]
			posy-=1
			if(posy==-1):
				posy=511
			pathcolor[1]+=1
	if(dirr==1):
		for x in range(8):
			for z in range(3):
				img[posy][posx][z]=pathcolor[z]
			posx+=1
			if(posx==512):
				posx=0
			pathcolor[1]+=1
	if(dirr==2):
		for x in range(8):
			for z in range(3):
				img[posy][posx][z]=pathcolor[z]
			posy+=1
			if(posy==512):
				posy=0
			pathcolor[1]+=1
	if(dirr==3):
		for x in range(8):
			for z in range(3):
				img[posy][posx][z]=pathcolor[z]
			posx-=1
			if(posx==-1):
				posx=511
			pathcolor[1]+=1

	return [posx,posy]

for i in range(len(roots)):
	pathcolor[0]+=64
	pathcolor[0]=pathcolor[0]%256
	pathcolor[2]+=0
	for x in range(len(roots[i][1])):
		posx = roots[i][1][x][0]*8
		posy = roots[i][1][x][1]*8
		pathcolor[1]=0
		#print("posx: "+str(posx)+" posy: "+str(posy))
		for z in range(5):
			img[posy+z-2][posx+z-2][2]=pathcolor[0]+32
			img[posy+z-2][posx-z+2][2]=pathcolor[0]+32
			img[posy+z-2][posx+z-2][1]=128
			img[posy+z-2][posx-z+2][1]=128
		for y in range(len(roots[i][2][x])):
			#drawBranch
			ret=drawPath(posx,posy,roots[i][2][x][y])
			posx=ret[0]
			posy=ret[1]



cv2.imwrite('/home/dan/Pictures/treegrid64.png',img)

