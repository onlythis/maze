#merge sort

def merge(lst):
	print("splitting: "+str(lst))
	if(len(lst)>1):
		mid=len(lst)//2
		left=lst[:mid]
		right=lst[mid:]
		merge(left)
		merge(right)
		i,j,k=0,0,0
		while(i<len(left) and j<len(right)):
			if(left[i]<right[j]):
				lst[k]=left[i]
				i+=1
			else:
				lst[k]=right[j]
				j+=1
			k+=1
		while(i<len(left)):
			lst[k]=left[i]
			i+=1
			k+=1
		while(j<len(right)):
			lst[k]=right[j]
			j+=1
			k+=1
	print("merging: " + str(lst))
	return lst
		
		
l=[1,2,8,7,5,10,20,14,15,17,13,4,1,2,3,4,65,54,23,43,2,1,34,5,34,6]

print(len(merge(l)))
print(len(l))
