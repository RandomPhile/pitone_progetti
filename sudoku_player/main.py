import tkinter as tk
import numpy as np

width, height, m = 510, 510, 5
grid_size = min(width,height)
size = (grid_size-2*m)/9
t = 5
print(size)
#print(cols,rows)
grid = []

root = tk.Tk()
root.title("Sudoku Player")
canvas = tk.Canvas(root, width = width, height = height,bg="gray20")
canvas.pack()

selected = []

def xy_to_index(pos):
	return pos[0]*9 + pos[1]

def index_to_xy(index):
	return [int(index/9), index%9]

def pressed(event):
	global selected
	selected = [int(event.x/size),int(event.y/size)]
	if xy_to_index(selected) in initial:
		selected=[]
	print(selected)

zeros = np.array([[0,0,0, 0,0,0, 0,0,0],[0,0,0, 0,0,0, 0,0,0],[0,0,0, 0,0,0, 0,0,0],[0,0,0, 0,0,0, 0,0,0],[0,0,0, 0,0,0, 0,0,0],[0,0,0, 0,0,0, 0,0,0],[0,0,0, 0,0,0, 0,0,0],[0,0,0, 0,0,0, 0,0,0],[0,0,0, 0,0,0, 0,0,0]])

numbers = np.array([
	[1,0,0, 0,0,0, 0,0,0],
	[2,0,0, 0,0,0, 0,0,0],
	[3,0,0, 0,0,0, 0,0,0],

	[4,0,0, 0,0,0, 0,0,0],
	[5,0,0, 0,0,0, 0,0,0],
	[6,0,0, 0,0,0, 0,0,0],

	[7,0,0, 0,0,0, 0,0,0],
	[8,0,0, 0,0,0, 0,0,0],
	[9,0,0, 0,0,0, 0,0,0]])

initial = []
for i in np.argwhere(numbers!=0):
	initial.append(xy_to_index(i))

def pressed(event):
	global selected
	selected = [int(event.y/size),int(event.x/size)]
	if xy_to_index(selected) in initial:
		selected=[]
	print(selected)

def key_pressed(event):
	if selected:
		n = event.char
		try:
			n = int(n)
		except:
			print('Inserire un numero tra 1 e 9, non   ',n)
		else:
			if n != 0:
				print(n)
				update_n(selected,n)

def draw_grid():
	for i in [1,2,4,5,7,8]:
		canvas.create_line(m,m+size*i,grid_size-m,m+size*i,width=1)
		canvas.create_line(m+size*i,m,m+size*i,grid_size-m,width=1)
	for i in [0,3,6,9]:
		canvas.create_line(m,m+size*i,grid_size-m,m+size*i,width=3)
		canvas.create_line(m+size*i,m,m+size*i,grid_size-m,width=3)

def draw_numbers(numbers):
	for row in range(9):
		for col in range(9):
			if xy_to_index([row,col]) in initial:
				canvas.create_text(m+size/2+col*size,m+size/2+row*size,text=numbers[row][col],font=("Purisa",int(size*0.7)),fill="blue")
			else:
				canvas.create_text(m+size/2+col*size,m+size/2+row*size,text=numbers[row][col],font=("Purisa",int(size*0.7)))

def update_n(selected,n):
	canvas.create_rectangle(m+selected[1]*size+t, m+selected[0]*size+t, m+size+selected[1]*size-t, m+size+selected[0]*size-t,fill="gray20",width=0)
	canvas.create_text(m+size/2+selected[1]*size,m+size/2+selected[0]*size,text=n,font=("Purisa",int(size*0.7)),fill="lightblue")

draw_grid()
draw_numbers(numbers)

canvas.bind("<Button>", pressed)
root.bind("<KeyPress>", key_pressed)
root.mainloop()