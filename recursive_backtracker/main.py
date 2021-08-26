import tkinter as tk
import random
from functions import *

width, height, w, speed = 510, 810, 10, 1
#width, height, w, speed = 1440, 900, 10, 1

margin = 5
cols, rows = int((width-2*margin)/w), int((height-2*margin)/w)
#print(cols,rows)
grid = []

root = tk.Tk()
#root.attributes("-fullscreen", True)
root.title("Recursive Backtracker")
canvas = tk.Canvas(root, width = width, height = height)
canvas.pack()
random.seed()

class Cell(object):
	def __init__(self, i, j,col):
		self.i, self.j = i,j
		self.walls = [True,True,True,True]
		self.visited = False
		self.col = col

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
			canvas.create_rectangle(x,y,x+w,y+w,width=0,fill=self.col)

def setup():
	global grid,stack,current,count
	grid = []
	for j in range(rows):
		for i in range(cols):
			cell = Cell(i,j,'#aa00aa')
			grid.append(cell)
			#cell.show()
	stack = []
	current = grid[0]
	current.visited = True
	stack.append(current)
	count=0

def fin():
	global count
	print('steps: ',count)

def loop():
	global stack,count

	current = stack[-1]
	stack.pop(-1)
	current.show()

	n = ij_to_index(current.i,current.j,cols)
	touching = [n-cols,n+1,n+cols,n-1]
	
	d = check(touching,current.i,current.j,cols,rows,grid)
	
	if d != -2:
		stack.append(current)
		grid[n].walls[d] = False
		grid[n].col = '#aa00aa'
		grid[touching[d]].walls[opposite_wall(d)] = False
		grid[touching[d]].visited = True
		grid[touching[d]].col = '#ff00ff'
		stack.append(grid[touching[d]])
	
	count+=1
	if len(stack) > 0:
		if count%speed==0:
			root.after(1,loop)
		else:
			root.after(0,loop)
	else:
		root.after(1,fin)
		pass
setup()
loop()
root.mainloop()