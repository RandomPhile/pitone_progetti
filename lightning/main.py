import tkinter as tk
import random
import time
import numpy as np

#random.seed(10)
randomize = random.random()

root = tk.Tk()
root.title("maze")
window_w, window_h = 400,400
columns = 25
window_w, window_h = 600, 830
w = tk.Canvas(root, width = window_w, height = window_h)
w.pack()

margin = 10
rows = int(columns*window_h/window_w)
#print('#Colonne:',columns,'#Righe',rows)
squares_size = ((window_w-2*margin)/columns)#eventualmente int()
p_horiz, p_vert = 0.4, 0.5

def xy_to_index(row,col):
	return row*columns + col

def index_to_xy(index):
	return [int(index/columns), index%columns]


def draw_square(sq):
	w.create_rectangle(sq.x, sq.y, sq.x+squares_size, sq.y+squares_size, fill=sq.col, width=0)
	if 'u' in sq.border:
		w.create_line(sq.x, sq.y, sq.x+squares_size, sq.y,width=2)
	if 'r' in sq.border:
		w.create_line(sq.x+squares_size, sq.y, sq.x+squares_size, sq.y+squares_size,width=2)
	if 'd' in sq.border:
		w.create_line(sq.x, sq.y+squares_size, sq.x+squares_size, sq.y+squares_size,width=2)
	if 'l' in sq.border:
		w.create_line(sq.x, sq.y, sq.x, sq.y+squares_size,width=2)

class square(object):
	def __init__(self, x, y, hue, border, base_color):
		#super(square, self).__init__()
		self.x, self.y= x, y
		self.hue, self.border, self.base_color = hue, border, base_color

	@property
	def col(self):
		return self.base_color + str(format(255 - int(self.hue*255/100), 'x')).zfill(2)

squares = []
def create_squares():
	y = margin
	for row in range(rows):
		x = margin
		for col in range(columns):
			contorno = ''
			#chiaroscuro = int((x+y)*100/(window_w+window_h))
			#chiaroscuro = int((y)*100/(window_h))
			chiaroscuro = 0
			squares.append(square(x,y,chiaroscuro,contorno, '#ddff'))
			x+=squares_size
		y+=squares_size

def create_border(which_sides):
	random.seed()
	random_list = []
	for i in range(4):
		random_list.append(random.random())
	out = ''
	if 'u' in which_sides:
		if random_list[0]<p_horiz:
			out=out+'u'
	if 'd' in which_sides:
		if random_list[1]<p_horiz:
			out=out+'d'
	if 'r' in which_sides:
		if random_list[2]<p_vert:
			out=out+'r'
	if 'l' in which_sides:
		if random_list[3]<p_vert:
			out=out+'l'
	return out


def create_maze():
	squares[xy_to_index(0,0)].border = create_border('drl')
	#colonna 0
	for row in range(1,rows):
		add = ''
		if 'd' in squares[xy_to_index(row-1,0)].border:
			add = 'u'
		squares[xy_to_index(row,0)].border = add + create_border('drl')
	#riga 0
	for col in range(1,columns):
		add = ''
		if 'r' in squares[xy_to_index(0,col-1)].border:
			add = 'l'
		squares[xy_to_index(0,col)].border = add + create_border('dr')
	#righe
	for row in range(1,rows):
		for col in range(1,columns):
			add = ''
			if 'd' in squares[xy_to_index(row-1,col)].border:
				add = 'u'
			if 'r' in squares[xy_to_index(row,col-1)].border:
				add += 'l'
			squares[xy_to_index(row,col)].border = add + create_border('dr')
			


def refine_maze():
	for i in range(columns*rows):
		border = squares[i].border
		if 'u' in border and 'd' in border and 'r' in border and 'l' in border:
			
			if random.random() < p_horiz/(p_horiz+p_vert):
				remove = random.choice(['u','d'])
				if remove == 'u':
					try:
						squares[i - columns].border = squares[i - columns].border.replace('d','')
					except:
						print('Impossibile rimuovere d da i-col')
				else:
					try:
						squares[i + columns].border = squares[i + columns].border.replace('u','')
					except:
						print('Impossibile rimuovere u da i+col')
			else:
				remove = random.choice(['r','l'])
				if remove == 'r':
					try:
						squares[i + 1].border = squares[i + 1].border.replace('l','')
					except:
						print('Impossibile rimuovere l da i+1')
				else:
					try:
						squares[i - 1].border = squares[i - 1].border.replace('r','')
					except:
						print('Impossibile rimuovere r da i-1')
			squares[i].border = squares[i].border.replace(remove,'')
			


create_squares()
create_maze()
refine_maze()

for sq in squares:
	draw_square(sq)

#########################################################################################
M = np.zeros((rows,columns))
M[0,int(columns/2)] = 1
animation = []

t=0
def update_maze():
	global t
	t=t+1
	if t<10:
		root.after(200,update_maze)

def solve():
	global animation
	for step in range(1,2*rows):
		for i in np.flatnonzero(M == step):
			
			if int(i/columns) >= rows-1:
				print('fin',step)
				return
			if 'r' not in squares[i].border and i%columns < columns-1 and M[int(i/columns), i%columns +1] == 0:
				M[int(i/columns), i%columns +1] = M[int(i/columns), i%columns] +1
			if 'd' not in squares[i].border and int(i/columns) < rows-1 and M[int(i/columns) +1, i%columns] == 0:
				M[int(i/columns) +1, i%columns] = M[int(i/columns), i%columns] +1
			if 'l' not in squares[i].border and i%columns > 1 and M[int(i/columns), i%columns -1] == 0:
				M[int(i/columns), i%columns -1] = M[int(i/columns), i%columns] +1
			if 'u' not in squares[i].border and int(i/columns) > 1 and M[int(i/columns) -1, i%columns] == 0:
				M[int(i/columns) -1, i%columns] = M[int(i/columns), i%columns] +1
		animation.append(M.flatten())

	#print(M)

solve()

def numbers():
	for i in range(len(animation[1])):
		w.create_text(squares[i].x+squares_size/2, squares[i].y+squares_size/2, font="Purisa",text=str(int(animation[-1][i])))

t=0
def next():
	global t
	
	for i in range(len(animation[1])):
		h=int(100*2*((animation[t][i]/(t+2))-0.5))
		if h>=0:
			squares[i].hue = h
		else:
			squares[i].hue = 0
		#print(animation[t][i], squares[i].hue, squares[i].col)
		draw_square(squares[i])

	#print('t:',t)
	t=t+1
	if t<len(animation):
		root.after(200,next)
	else:
		root.after(100,numbers)
next()



root.mainloop()