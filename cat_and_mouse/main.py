'''
cat on land is 4 times faster than the mouse on water
'''
import tkinter as tk
import numpy as np
import math

####### CONSTANTS #########
speed_ratio = 4
width, height = 500,500
margin = 10
r = min([width,height])/2 - margin
#1: mouse runs opposite of cat
tactic = 1

####### TKINTER ###########
root = tk.Tk()
root.title('Cat and Mouse')
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()


#R:  vettore in coordinate polari     (ro, theta)
#Rc: vettore in coordinate cartesiane (x,y)

ORIGIN = np.array([0,0])#     ORIGINc=ORIGIN

def clean_angle(a):
	if a>=0:
		return a - math.tau*int(a/(math.tau))
	else:
		return a + math.tau*(int(a/(math.tau))+1)


def polar_to_cartesian(R):
	return np.array([math.cos(R[1])*R[0], math.sin(R[1])*R[0]])

def cartesian_to_polar(Rc):
	return np.array([np.linalg.norm(Rc), math.atan2(Rc[1],Rc[0])])

def transform_cartesian(Rc):
	return np.array([Rc[0]+width/2, -Rc[1]+height/2])

def normalize(VECTOR):
	return np.dot(VECTOR,1/math.sqrt(np.linalg.norm(VECTOR)))

def _create_circle(self, R, rad, **kwargs):
	Rc_ = transform_cartesian(polar_to_cartesian(R))
	x,y = Rc_[0], Rc_[1]
	return self.create_oval(x-rad, y-rad, x+rad, y+rad, **kwargs)
tk.Canvas.create_circle = _create_circle

class Cat(object):
	def __init__(self, R, v):
		self.R, self.v = R, v

	def step(self, clockwise):
		w = self.v/r
		self.R[1] += w*clockwise

	def show(self):
		canvas.create_circle(self.R, 5, fill='red',outline='darkred')


class Mouse(object):
	def __init__(self, R, v):
		self.R,self.v = R,v

	def step(self, cat_R):
		Rc = polar_to_cartesian(self.R)
		cat_Rc = polar_to_cartesian(cat_R)
		Dc = cat_Rc - Rc
		D = cartesian_to_polar(Dc)

		V = np.array([self.v, D[1]+math.pi])
		#canvas.create_line(transform_cartesian(Rc)[0],transform_cartesian(Rc)[1],transform_cartesian(cat_Rc)[0],transform_cartesian(cat_Rc)[1])
		Rc += polar_to_cartesian(V)
		self.R = cartesian_to_polar(Rc)
		
	def show(self):
		canvas.create_circle(self.R, 4, fill='blue',outline='darkblue')


#######
canvas.create_circle(ORIGIN,r, fill='lightblue', outline='black')
canvas.create_circle(ORIGIN,2, fill='black', outline='black')

cat = Cat(np.array([r,4*math.pi/8]),30)
mouse = Mouse(np.array([r/2,7*math.pi/8]),10)

count=0
def loop():
	global count

	mouse.show()
	cat.show()
	
	mouse.step(cat.R)

	mouse_Rc = polar_to_cartesian(mouse.R)
	cat_Rc = polar_to_cartesian(cat.R)
	Dc = mouse_Rc - cat_Rc
	D = cartesian_to_polar(Dc)

	
	#print(np.cross(cat_Rc,Dc))
	if np.cross(mouse_Rc,cat_Rc)>0:
		cat.step(-1)
	else:
		cat.step(1)
	

	if count<3000 and mouse.R[0]<=r:
		if count==0:
			canvas.delete("all")
			canvas.create_circle(ORIGIN,r, fill='lightblue', outline='black')
			canvas.create_circle(ORIGIN,2, fill='black', outline='black')
		#print('CAT  :',cat.a)
		#print('MOUSE:',xy_to_a(mouse.x,mouse.y))
		
		count+=1
		root.after(10,loop)

loop()

root.mainloop()