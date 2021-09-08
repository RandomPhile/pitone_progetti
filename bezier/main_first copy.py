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
controls = [C0]

def HSV_to_RGB(color_HSV):
	H,S,V = color_HSV[0],color_HSV[1],color_HSV[2]
	def f(n):
		k = (n + H/60) % 6
		return V - V*S*max(0,min(k, 4-k, 1))
	return [f(5), f(3), f(1)]
def RGB_to_hex(color_RGB):
	R,G,B = round(color_RGB[0]*255),round(color_RGB[1]*255),round(color_RGB[2]*255)
	return '#%02x%02x%02x' % (R, G, B)
def HSV_to_hex(color_HSV):
	return RGB_to_hex(HSV_to_RGB(color_HSV))

def _create_point(self, P, **kwargs):
	rad = 3
	x,y = P[0], P[1]
	return self.create_oval(x-rad, y-rad, x+rad, y+rad, **kwargs)
tk.Canvas.create_point = _create_point

def lerp(Pi,Pf,t):
	return np.dot((1-t),Pi) + np.dot(t,Pf)

count=0
down=0
def pressed(event):
	global count,C0,down
	down = 1
	print ('Pre',event.x,event.y)
	C0 = np.array([event.x,event.y])
	count = 0
	loop()

def released(event):
	global down
	down = 0
	print ('Rel',event.x,event.y)

def moved(event):
	global count,C0,down
	if down:
		print ('Mov',event.x,event.y)
		C0 = np.array([event.x,event.y])
		count = 0
		loop()

id = canvas.create_line(P0.tolist(),C0.tolist(),fill="black",width=1)
canvas.tag_bind(id, "<Motion>", lambda x: print(event))

def loop():
	global count,points,controls, P0, P1, C0
	
	mouse_pos = [root.winfo_pointerx()-root.winfo_rootx(), root.winfo_pointery()-root.winfo_rooty()]
	if mouse_pos[0]<width and mouse_pos[1]<height and mouse_pos not in points:
		points.insert(1,mouse_pos)
	
	canvas.delete("all")
	canvas.create_line(P0.tolist(),C0.tolist(),fill="black",width=1)
	canvas.create_line(C0.tolist(),P1.tolist(),fill="black",width=1)

	for t in [number/n_lines for number in range(n_lines+1)]:
		#canvas.create_point(lerp(P0,C0,t),fill="black",width=0)
		#canvas.create_point(lerp(C0,P1,t),fill="black",width=0)
		canvas.create_line(lerp(P0,C0,t).tolist(),lerp(C0,P1,t).tolist(),fill=HSV_to_hex([t*360,1,1]),width=1)
		canvas.create_point(lerp(lerp(P0,C0,t),lerp(C0,P1,t),t),fill="black",width=0)
	#canvas.create_line(points[0],controls,points[-1],fill="orange",width=1)
	


	if count<1:
		print('Tick: ',count)
		count+=1

		root.after(200,loop)


#canvas.bind('<Enter>', enter)
#canvas.bind('<Leave>', escher)

root.mainloop()