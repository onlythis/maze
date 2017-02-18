import tensorflow
from tkinter import *
import scipy.misc

path= '/home/dan/Pictures/wood_ring2.png'
image=scipy.misc.imread(path)
anim=Tk()
canvas=Canvas(anim,width=1200,height=1000, bg ="#000000")
canvas.pack()
tkimg=PhotoImage(width=1200,height=1000)
canvas.create_image((600,500), image=tkimg, state="normal")
# create iter for image[y][x][z] before looping
# assign func str(hex( to variable? as well as len
# speed/performance
for x in range(1200):
	for y in range(1000):
		color="#"
		red=str(hex(image[y][x][0]))[2:]
		green=str(hex(image[y][x][1]))[2:]
		blue=str(hex(image[y][x][2]))[2:]
		while(len(red)!=2):
			red="0"+red
		while(len(green)!=2):
			green="0"+green
		while(len(blue)!=2):
			blue="0"+blue
		#blue='{0:{1}{2}}'.format(image[x][y][2],2,'X')
		
		color+=red+green+blue
		if(len(color)!=7):
			print(x,y,color,red,green,blue)
		tkimg.put(color,(x,y))
