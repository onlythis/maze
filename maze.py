import random
w=64
h=64
grid =[[0 for a in range(w)] for b in range(h)]
grid_dir =[[[] for a in range(w)] for b in range(h)]
path=[]
treesize=16
start_positions=[]
branch_paths=[]
startx=16
starty=32
#array of start positions(one for each branch), array of branchpaths(one for each branch)
def quadTree():
	grid[startx][starty]+=1
	start_positions.append([startx,starty])
	branch_paths.append(growbranch(startx,starty,treesize,1))
	prevpaths=0
	currpaths=len(branch_paths)
	counter=0
	while(currpaths!=prevpaths):
		if(counter==25):
			print("countReached")
			print(counter)
			return start_positions
		for y in range(prevpaths,currpaths):
			search_opendirrs(start_positions[y][0],start_positions[y][1],branch_paths[y])
		prevpaths=currpaths
		currpaths=len(branch_paths)
		counter+=1

	return start_positions

	
def search_opendirrs(posx, posy, path):
	openings=0
	skips=0
	dirr=-1
	for x in range(len(path)):
		dirr=path[x]
		openings=0
		for y in range(4):
			openings+=checkgrid(posx,posy,y)
		if(openings<=2):
			skips+=1
		if(skips==4):
			for z in range(4):
				branch_paths.append(growbranch(posx,posy,treesize,z))
				start_positions.append([posx,posy])
			return 0
		if(dirr==0):
			posy-=1
		if(dirr==1):
			posx+=1
		if(dirr==2):
			posy+=1
		if(dirr==3):
			posx-=1
		if(posy<0):
			posy=63
		if(posy>63):
			posy=0
		if(posx<0):
			posx=63
		if(posx>63):
			posx=0

#def growrecursive(prevx,prevy,posx,posy,length):

def growbranch( posx, posy, length,initdirr):
	#better chance of continuing direction
	#North=0, East=1, South=2, West=3
	branch_path=[]
	dirr=initdirr
	for i in range(length):
		dirr=dont_turn_back(initdirr,dirr)
		if(i<4):
			dirr=initdirr
		n=0
		while(checkgrid(posx,posy,dirr)):
			if(n>100):
				return branch_path
			#gets reassigned then it can turn back
			dirr=dont_turn_back(initdirr,dirr)
			n+=1
		grid_dir[posy][posx].append([dirr,counterdirr(dirr)])
		#wont account for last block of path
		if(dirr==0):
			posy-=1
		if(dirr==1):
			posx+=1
		if(dirr==2):
			posy+=1
		if(dirr==3):
			posx-=1

		if(posy<0):
			posy=63
		if(posy>63):
			posy=0
		if(posx<0):
			posx=63
		if(posx>63):
			posx=0
		grid[posy][posx]+=1
		branch_path.append(dirr)
	return branch_path

#returns 1 if grid pos is taken
def checkgrid(posx,posy,dirr):
	if(dirr==0):
		if(posy<=-64):
			posy=64
		if(grid[posy-1][posx]>0):
			return 1
		else:
			return 0
	if(dirr==1):
		if(posx>=63):
			posx=-1
		if(grid[posy][posx+1]>0):
			return 1
		else:
			return 0
	if(dirr==2):
		if(posy>=63):
			posy=-1
		if(grid[posy+1][posx]>0):
			return 1
		else:
			return 0
	if(dirr==3):
		if(posx<=-64):
			posx=64
		if(grid[posy][posx-1]>0):
			return 1
		else:
			return 0

def dont_turn_back(initdirr,dirr):
	if(random.randint(0,1)==0):
		return initdirr
	else:
		if(random.randint(0,1)==0):
			return turnclock(dirr)
		else:
			return turncounter(dirr)

def turnclock(dirr):
	ret=dirr+1
	if(ret==4):
		ret=0
	return ret

def turncounter(dirr):
	ret=dirr-1
	if(ret==-1):
		ret=3
	return ret

def counterdirr(dirr):
	if(dirr<2):
		return dirr+2
	else:
		return dirr-2

def getGrid():
	return grid

def getPath():
	return path

def getbranchPaths():
	return branch_paths

if __name__ == "__main__":
	asdf=0
