import tkinter as tk
import numpy as np
import math

####### CONSTANTS #########
width, height, margin = 500, 500, 10
n_lines = 20
####### TKINTER ###########
root = tk.Tk()
root.title('Bezier')
canvas = tk.Canvas(root, bg="lightgray", width=width, height=height)
canvas.pack()

P0 = np.array([margin, height/2])
P1 = np.array([width-margin, height/2])
C0 = np.array([width/3,height/4])

points = [P0.tolist(),P1.tolist()]
controls = [C0.tolist()]

def _create_point(self, P, **kwargs):
	rad = 4
	x,y = P[0], P[1]
	return self.create_oval(x-rad, y-rad, x+rad, y+rad, **kwargs)
tk.Canvas.create_point = _create_point

def lerp(Pi,Pf,t):
	return np.dot((1-t),Pi) + np.dot(t,Pf)

tags = []
down = 0
def aggiorna_punto(tags_new,coord):
	global controls,points,tags
	print(tags,tags_new)
	if tags_new == []:
		print('aaa')
		tags_new = tags.copy()
	else:
		print('bbb')
		tags = tags_new.copy()
	if 'current' in tags_new:
		tags_new.remove('current')
	if 'control' in tags_new:
		tags_new.remove('control')
		controls[int(tags_new[0])] = coord

	elif 'point' in tags_new:
		tags_new.remove('point')
		points[int(tags_new[0])] = coord
	print(tags,tags_new)
	loop()
	return

def pressed(event):
	global down
	down = 1
	tags_new = list(canvas.gettags(canvas.find_closest(event.x, event.y)))
	aggiorna_punto(tags_new, [event.x, event.y])
	

def released(event):
	global down
	down = 0

def moved(event):
	if down:
		count = 0
		aggiorna_punto([], [event.x, event.y])
		

#linea = []
def loop():
	global points,controls,linea
	linea = []

	C0 = np.array(controls[0])
	P0 = np.array(points[0])
	P1 = np.array(points[1])
	canvas.delete("all")
	for i in range(len(points)):
		canvas.create_point(points[i], fill='black',width=0,tags=('point',i))
	for i in range(len(controls)):
		canvas.create_point(controls[i], fill='blue',width=0,tags=('control',i))

	canvas.create_line(P0.tolist(),C0.tolist(),fill="black",width=1)
	canvas.create_line(C0.tolist(),P1.tolist(),fill="black",width=1)

	for t in [number/n_lines for number in range(n_lines+1)]:
		linea.append([lerp(lerp(P0,C0,t),lerp(C0,P1,t),t).tolist()])
		#canvas.create_point(lerp(lerp(P0,C0,t),lerp(C0,P1,t),t),fill="black",width=0)
	canvas.create_line(linea,fill="red",width=1)

loop()
canvas.bind("<Button>", pressed)
canvas.bind("<Motion>", moved)
canvas.bind("<ButtonRelease>", released)
root.mainloop()