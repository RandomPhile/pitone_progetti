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
	rad = 3
	x,y = P[0], P[1]
	return self.create_oval(x-rad, y-rad, x+rad, y+rad, **kwargs)
tk.Canvas.create_point = _create_point

def lerp(Pi,Pf,t):
	return np.dot((1-t),Pi) + np.dot(t,Pf)

down=0
def pressed(event):
	global C0,down,controls
	down = 1
	#print ('Pre',event.x,event.y)
	C0 = np.array([event.x,event.y])
	controls = [C0]
	loop()

def released(event):
	global down
	down = 0
	#print ('Rel',event.x,event.y)

def moved(event):
	global C0,down,controls
	if down:
		#print ('Mov',event.x,event.y)
		C0 = np.array([event.x,event.y])
		controls = [C0]
		loop()
#linea = []
def loop():
	global points,controls, P0, P1, C0,linea
	linea = []

	canvas.delete("all")
	for Point in points:
		canvas.create_point(Point, fill='black',width=0)
	for Control in controls:
		canvas.create_point(Control, fill='blue',width=0)

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