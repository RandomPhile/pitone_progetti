import tkinter as tk
import random

#random.seed(10)
randomize = random.random()

root = tk.Tk()
root.title("maze")
window_w, window_h = 400,600
squares_columns = 20
#window_w, window_h = 600, 830
w = tk.Canvas(root, width = window_w, height = window_h)
w.pack()

margin = 10
squares_rows = int(squares_columns*window_h/window_w)
print(squares_columns,squares_rows)
squares_size = ((window_w-2*margin)/squares_columns)#eventualmente int()
p_horiz, p_vert = 0.3, 0.4

def xy_to_index(row,col):
	return row*squares_columns + col

def index_to_xy(index):
	return [index/squares_columns, index%squares_columns]


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
	def __init__(self, x, y, hue, border):
		#super(square, self).__init__()
		self.x, self.y= x, y
		self.hue, self.border = hue, border

	@property
	def col(self):
		return '#ffff' + str(format(255 - int(self.hue*255/100), 'x')).zfill(2)

def create_squares():
	squares = []
	y = margin
	for row in range(squares_rows):
		x = margin
		for col in range(squares_columns):
			contorno = ''
			#chiaroscuro = int((x+y)*100/(window_w+window_h))
			chiaroscuro = 30
			squares.append(square(x,y,chiaroscuro,contorno))
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
				#elimino un orizz
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
				#elimino un vert
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
			
			#print('###',i,'###')
			#print(squares[i].border)
			squares[i].border = squares[i].border.replace(remove,'')
			#print(squares[i].border)
			#print('Indice:',i,remove)
			prova = True



create_maze()
refine_maze()


for sq in squares:
	draw_square(sq)
	pass

root.mainloop()
