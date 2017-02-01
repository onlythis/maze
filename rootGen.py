import random
w=64
h=64
grid =[[0 for a in range(w)] for b in range(h)]
grid_dir =[[[0,0,0,0] for a in range(w)] for b in range(h)]
path=[]
treesize=16
start_positions=[[16,16],[32,16],[48,16],[16,32],[48,32],[16,48],[32,48],[48,48]]
roots=[]
#[label, [start_positions], [paths]]
roots_len=8
#array of start positions(one for each branch), array of branchpaths(one for each branch)
def quadTree():
	depth=0

	for x in range(roots_len):
		startx=start_positions[x][0]
		starty=start_positions[x][1]
		grid[starty][startx]+=1
		roots.append([x])
		roots[x].append([[startx,starty]])
		dirr=random.randint(0,3)
		roots[x].append([growbranch(startx,starty,treesize,dirr)])
	ARCSG=True #Any Root Can Still Grow
	rootsPrevDepth=[0 for abc in range(len(roots))]
	rootsCurrDepth=[0 for abc in range(len(roots))]
	RCG=[True for a in range(len(roots))]
	for x in range(len(roots)):
		rootsCurrDepth[x]=len(roots[x][1])
	while(ARCSG):
		for a in range(len(roots)):
			if(rootsPrevDepth[a]!=rootsCurrDepth[a]):
				for b in range(rootsPrevDepth[a],rootsCurrDepth[a]):
					posx=roots[a][1][b][0]
					posy=roots[a][1][b][1]
					path=roots[a][2][b]
					label=roots[a][0]
					search_opendirrs(posx,posy,path,depth,label)

			rootsPrevDepth[a]=rootsCurrDepth[a]
			rootsCurrDepth[a]=len(roots[a][1])
			if(rootsPrevDepth[a]==rootsCurrDepth[a]):
				RCG[a]=False
		depth+=1
		for z in range(len(RCG)):
			if(RCG[z]==True):
				break
			if(z==len(RCG)-1 and RCG[z]==False):
				ARCSG=False
	startposlen=0
	for a in range(len(roots)):
		startposlen+=len(roots[a][1])
	print("startposlen: "+str(startposlen))
	print("rootscurrdepth[3]: "+str(rootsCurrDepth[3]))
	print("depth: "+str(depth))
	return roots

	
def search_opendirrs(posx, posy, path, depth, label):
	openings=0
	skips=random.randint(0,2)
	dirr=-1
	#print("posx: "+str(posx)+" posy: "+str(posy)+" label: "+str(label)+" path: "+str(path))
	for x in range(len(path)):
		dirr=path[x]
		openings=0
		for y in range(4):
			openings+=checkgrid(posx,posy,y)
		if(openings<=2):
			skips+=1
		if(skips==5):
			for z in range(4):
				if(checkgrid(posx,posy,z)==0):
					#print(str(posx)+"  "+str(posy)+"  "+str(z))
					newpath=growbranch(posx,posy,treesize,z)
					roots[label][1].append([posx,posy])
					roots[label][2].append(newpath)
					#print("roots[label]: "+str(roots[label]))
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

#def findposdirs(): look at each square and see if it is part of path and which dirrs it can go.

def growbranch(posx, posy, length, initdirr):
	#better chance of continuing direction
	#North=0, East=1, South=2, West=3
	branch_path=[]
	dirr=initdirr
	for i in range(length):
		dirr=dont_turn_back(initdirr,dirr)
		if(i<8):
			dirr=initdirr
			#doesn't seem to work
		n=0

		while(checkgrid(posx,posy,dirr)):
			if(n>100):
				return branch_path
			#gets reassigned then it can turn back
			dirr=dont_turn_back(initdirr,dirr)
			n+=1

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

def getGrid():
	return grid

if __name__ == "__main__":
	asdf=0
	quadTree()
