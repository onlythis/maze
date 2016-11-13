import numpy as np
import cv2
from maze import getGrid, getPath, quadTree, getbranchPaths
start_positions=quadTree()
grid=getGrid()
path=getPath()
branch_paths=getbranchPaths()
img = np.zeros((512,512,3), np.uint8)
pathcolor=[64 for x in range(3)]
pathcolor[1]=0


for i in range(len(branch_paths)):
	pos = start_positions[i]
	posx = pos[0]*8+3
	posy = pos[1]*8+3
	pathcolor[1]=0
	for j in range(len(branch_paths[i])):
		#this draws the lines	
		for n in range(8):
			for x in range(3):
				#x is color
				img[posy][posx][x]=pathcolor[x]
			pathcolor[1]+=1

			if(branch_paths[i][j]==0):
				posy-=1
				if(posy<0):
					posy=511
			if(branch_paths[i][j]==1):
				posx+=1
				if(posx>511):
					posx=0
			if(branch_paths[i][j]==2):
				posy+=1
				if(posy>511):
					posy=0
			if(branch_paths[i][j]==3):
				posx-=1
				if(posx<0):
					posx=511
			if(pathcolor[1]>255):
				pathcolor[1]=0
	for a in range(3):
		for b in range(3):
			img[posy-1+a][posx-1+b][1]=255
			img[posy-1+a][posx-1+b][2]=0
			img[posy-1+a][posx-1+b][0]=0


portion=len(start_positions)/3
count=0
for n in range(len(start_positions)):
	z=n/portion
	if(z==0):
		color=[0,222,0]
	if(z==1):
		color=[222,0,0]
	if(z==2):
		color=[0,0,222]
	if(z==3):
		color=[222,222,0]
	if(n==0 or n==len(start_positions)-1):
		color=[255,255,255]
	x=start_positions[n][0]
	y=start_positions[n][1]
	for a in range(5):
		for b in range(5):
			img[y*8+b+1][x*8+a+1] = color
			asdf=0

cv2.imwrite('/home/dan/Pictures/treegrid61.png',img)

