import tkinter as tk
import random

speed = 2
width, height = 510,810
w = 20
margin = 5
cols, rows = int((width-2*margin)/w), int((height-2*margin)/w)
#print(cols,rows)
grid = []

root = tk.Tk()
root.title("Recursive Backtracker")
canvas = tk.Canvas(root, width = width, height = height)
canvas.pack()
random.seed()

def ij_to_index(i,j):
	return j*cols + i

def index_to_ij(n):
	return [n%cols, int(n/cols)]

class Cell(object):
	def __init__(self, i, j,hue):
		self.i, self.j = i,j
		self.walls = [True,True,True,True]
		self.visited = False
		self.hue = hue

	def show(self):
		x = margin + self.i*w
		y = margin + self.j*w
		
		if self.walls[0]:
			canvas.create_line(x  ,  y,x+w,  y,width=2)
		if self.walls[1]:
			canvas.create_line(x+w,  y,x+w,y+w,width=2)
		if self.walls[2]:
			canvas.create_line(x  ,y+w,x+w,y+w,width=2)
		if self.walls[3]:
			canvas.create_line(x  ,  y,  x,y+w,width=2)

		if self.visited:
			canvas.create_rectangle(x,y,x+w,y+w,width=0,fill='#aa'+str(self.hue).zfill(2)+'aa')


for j in range(rows):
	for i in range(cols):
		cell = Cell(i,j,0)
		grid.append(cell)

def draw(lista):
	for n in range(len(lista)):
		lista[n].show()

def check(touching,n):
	pos = index_to_ij(n)
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
			#print('TESTA ','i:',i,'j:',j,'d:',d)
			return d
	#print('TESTA ','i:',i,'j:',j,'d:',d)
	return -2

def opposite_wall(n):
	if n==0:
		return 2
	elif n==2:
		return 0
	elif n==1:
		return 3
	elif n==3:
		return 1

stack = []
current = grid[0]
current.visited = True
stack.append(current)

useless_checks = 0
useless_steps = 0
def stop_now():
	global useless_checks
	for cell in grid:
		if cell.visited == False:
			useless_checks +=1
			return False
	return True

def stampa(lista):
	#print('STAMPA STACK')
	for cell in lista:
		print('CELLA: ', cell.visited)

def fin():
	global count
	print(count)
	#print('useless_checks',useless_checks,'useless_steps',useless_steps)

count=0
draw(grid)
def next():
	global stack,count#, useless_steps
	#stop = stop_now()

	current = stack[-1]
	stack.pop(-1)
	#print('ULTIMO','i:',current.i,'j:',current.j)
	current.show()

	n = ij_to_index(current.i,current.j)
	touching = [n-cols,n+1,n+cols,n-1]
	
	d = check(touching, n)
	#print('n:',n,'    d:',d)
	

	if d != -2:
		#print('d',d,'touching[d]',touching[int(d)])
		stack.append(current)

		grid[n].walls[d] = False
		#print('grid[n].walls          ', grid[n].walls)
		grid[touching[d]].walls[opposite_wall(d)] = False
		#print('grid[touching[d]].walls', grid[touching[d]].walls)

		grid[touching[d]].visited = True
		stack.append(grid[touching[d]])
	else:
		#print('retrofront')
		pass
	
	#if stop:
	#	useless_steps+=1
	count+=1
	if len(stack) > 0:
		if count%speed==0:
			root.after(1,next)
		else:
			root.after(0,next)
	else:
		root.after(1,fin)
		pass
next()
root.mainloop()