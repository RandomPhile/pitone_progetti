import random
def ij_to_index(i,j,cols):
	return j*cols + i

def index_to_ij(n,cols):
	return [n%cols, int(n/cols)]

def check(touching,n,cols,rows,grid):
	pos = index_to_ij(n,cols)
	i,j = pos[0],pos[1]
	if j==0:
		if i==0:
			order = random.sample([1,2],2)
		elif i==cols-1:
			order = random.sample([2,3],2)
		else:
			order = random.sample([1,2,3],3)
	elif j==rows-1:
		if i==0:
			order = random.sample([0,1],2)
		elif i==cols-1:
			order = random.sample([0,3],2)
		else:
			order = random.sample([0,1,3],3)
	elif i==0:
		order = random.sample([0,1,2],3)
	elif i==cols-1:
		order = random.sample([0,2,3],3)
	else:
		order = random.sample([0,1,2,3],4)
	
	for d in order:
		if not grid[touching[d]].visited:
			return d
	return -2

def draw(lista):
	for n in range(len(lista)):
		lista[n].show()

def opposite_wall(n):
	if n==0:
		return 2
	elif n==2:
		return 0
	elif n==1:
		return 3
	elif n==3:
		return 1
	return -1
