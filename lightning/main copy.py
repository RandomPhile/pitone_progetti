import tkinter as tk
import random
import time

#random.seed(10)
randomize = random.random()

root = tk.Tk()
root.title("maze")
window_w, window_h = 400,600
squares_columns = 11
#window_w, window_h = 600, 830
w = tk.Canvas(root, width = window_w, height = window_h)
w.pack()

margin = 10
squares_rows = int(squares_columns*window_h/window_w)
print('#Colonne:',squares_columns,'#Righe',squares_rows)
squares_size = ((window_w-2*margin)/squares_columns)#eventualmente int()
p_horiz, p_vert = 0.3, 0.4

def xy_to_index(row,col):
	return row*squares_columns + col

def index_to_xy(index):
	return [int(index/squares_columns), index%squares_columns]


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
	for row in range(squares_rows):
		x = margin
		for col in range(squares_columns):
			contorno = ''
			#chiaroscuro = int((x+y)*100/(window_w+window_h))
			chiaroscuro = int((y)*100/(window_h))
			squares.append(square(x,y,chiaroscuro,contorno, '#5599'))
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
	squares[xy_to_index(0,0)].border = create_border('udrl')
	#colonna 0
	for row in range(1,squares_rows):
		add = ''
		if 'd' in squares[xy_to_index(row-1,0)].border:
			add = 'u'
		squares[xy_to_index(row,0)].border = add + create_border('drl')
	#riga 0
	for col in range(1,squares_columns):
		add = ''
		if 'r' in squares[xy_to_index(0,col-1)].border:
			add = 'l'
		squares[xy_to_index(0,col)].border = add + create_border('udr')
	#righe
	for row in range(1,squares_rows):
		for col in range(1,squares_columns):
			add = ''
			if 'd' in squares[xy_to_index(row-1,col)].border:
				add = 'u'
			if 'r' in squares[xy_to_index(row,col-1)].border:
				add += 'l'
			squares[xy_to_index(row,col)].border = add + create_border('dr')
			


def refine_maze():
	for i in range(squares_columns*squares_rows):
		border = squares[i].border
		if 'u' in border and 'd' in border and 'r' in border and 'l' in border:
			
			if random.random() < p_horiz/(p_horiz+p_vert):
				remove = random.choice(['u','d'])
				if remove == 'u':
					try:
						squares[i - squares_columns].border = squares[i - squares_columns].border.replace('d','')
					except:
						print('Impossibile rimuovere d da i-col')
				else:
					try:
						squares[i + squares_columns].border = squares[i + squares_columns].border.replace('u','')
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
i_inizio = int(squares_columns/2)



t = 1

class active_square(object):
	def __init__(self,i,t0,parents):
		self.i, self.t0, self.parents = i, t0, parents


i_set = set([i_inizio])
active_squares = []

#Primo quadrato
active_squares.append(active_square(i_inizio,0,[]))


def update_active_square(active_square):
	if t-active_square.t0<10:
		squares[active_square.i].base_color = '#ffff'
		squares[active_square.i].hue = 100/(t-active_square.t0)
	else:
		squares[active_square.i].base_color = '#5599'
		squares[active_square.i].hue = int((squares[active_square.i].y)*100/(window_h))
	draw_square(squares[active_square.i])

def move(sq):
	global t
	i_set.add(sq.i)
	riga,colonna = index_to_xy(sq.i)[0], index_to_xy(sq.i)[1]
	
	if riga == squares_rows-1:
		print('finito')
		t=10000
	
	parents_new = sq.parents + [sq.i]
	if 'r' not in squares[sq.i].border:
		if colonna<squares_columns-1:
			if squares[sq.i+1].base_color == '#5599' and sq.i+1 not in i_set:
				active_squares.append(active_square(sq.i+1,t,parents_new))
				#update_active_square(sq+1)
	if 'd' not in squares[sq.i].border:
		if riga<squares_rows-1:
			if squares[sq.i+squares_columns].base_color == '#5599' and sq.i+squares_columns not in i_set:
				active_squares.append(active_square(sq.i+squares_columns,t,parents_new))
				#update_active_square(sq+squares_columns)
	if 'l' not in squares[sq.i].border:
		if colonna>0:
			if squares[sq.i-1].base_color =='#5599' and sq.i-1 not in i_set:
				active_squares.append(active_square(sq.i-1,t,parents_new))
				#update_active_square(sq-1)
	if 'u' not in squares[sq.i].border:
		if riga>0:
			if squares[sq.i-squares_columns].base_color == '#5599' and sq.i-squares_columns not in i_set:
				active_squares.append(active_square(sq.i-squares_columns,t,parents_new))
				#update_active_square(sq-squares_columns)
	


def next():
	global t
	lista = []
	for active_sq in active_squares:
		lista.append(active_sq)

	for active_sq in lista:
		move(active_sq)

	for active_sq in lista:
		update_active_square(active_sq)


	#print('t:',t)
	t=t+1
	if t<30:
		root.after(200,next)

next()
#for n in range(30):
#	print(n,index_to_xy(n))

root.mainloop()
