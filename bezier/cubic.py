import tkinter as tk
import numpy as np
import math

####### CONSTANTS #########
width, height, margin = 500, 500, 50
rad = 5
n_lines = 100
####### TKINTER ###########
root = tk.Tk()
root.title('Bezier')
canvas = tk.Canvas(root, bg="lightgray", width=width, height=height)
canvas.pack()

P0 = [margin, 2*height/3]
P1 = [width-margin, 2*height/3]

C0 = [width/4,height/4]
C1 = [3*width/4,height/4]

points = [P0,P1]
controls = [C0,C1]

def _create_point(self, P, **kwargs):
	global rad
	x,y = P[0], P[1]
	return self.create_oval(x-rad, y-rad, x+rad, y+rad, **kwargs)
tk.Canvas.create_point = _create_point

def lerp(Pi,Pf,t):
	return (np.dot((1-t),np.array(Pi)) + np.dot(t,np.array(Pf))).tolist()

tags = []
down = 0
def aggiorna_punto(tags_new,coord):
	global controls,points,tags
	if tags_new == []:
		tags_new = tags.copy()
	else:
		tags = tags_new.copy()
	if 'current' in tags_new:
		tags_new.remove('current')
	if 'control' in tags_new:
		tags_new.remove('control')
		controls[int(tags_new[0])] = coord

	elif 'point' in tags_new:
		tags_new.remove('point')
		points[int(tags_new[0])] = coord
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
		aggiorna_punto([], [min(max(rad,event.x),width), min(max(rad,event.y),height)])
		

def loop():
	global points,controls
	linea = []

	canvas.delete("all")
	for i in range(len(points)):
		canvas.create_point(points[i], fill='black',width=0,tags=('point',i))
	for i in range(len(controls)):
		canvas.create_point(controls[i], fill='blue',width=0,tags=('control',i))

	canvas.create_line(points[0],controls[0],fill="black",width=1)
	#for i in range(len(controls)-1):
		#canvas.create_line(controls[i],controls[i+1],fill="black",width=1)
	canvas.create_line(points[1],controls[-1],fill="black",width=1)

	for t in [number/n_lines for number in range(n_lines+1)]:
		L01 = lerp(points[0],controls[0],t)
		L12 = lerp(controls[0],controls[1],t)
		L23 = lerp(controls[1],points[1],t)
		L1 = lerp(L01,L12,t)
		L2 = lerp(L12,L23,t)
		L = lerp(L1,L2,t)
		linea.append(L)

		#linea.append([lerp(lerp(points[0],controls[0],t),lerp(controls[0],points[1],t),t)])
	canvas.create_line(linea,fill="red",width=2)

loop()
canvas.bind("<Button>", pressed)
canvas.bind("<Motion>", moved)
canvas.bind("<ButtonRelease>", released)
root.mainloop()