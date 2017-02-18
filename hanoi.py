#tower of hanoi

a=[4,3,2,1]
b=[]
c=[]

def move(n,source,target,aux):
	if(n>0):
		move(n-1,source,aux,target)
		target.append(source.pop())
		print(a,b,c,"------------------",sep="\n")
		move(n-1,aux,target,source)

move(4,a,b,c)
