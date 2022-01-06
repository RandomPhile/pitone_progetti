import tkinter as tk
from functions import *
import math

width, margin = 510, 5
height = width*math.sqrt(3)/2

x_max, y_max = width-2*margin, height-2*margin
wid = lambda x : x + margin
hei = lambda y : height - (y + margin)

root = tk.Tk()
root.title("lighthouse beam")
canvas = tk.Canvas(root, width = width, height = height)
canvas.pack()

def draw_triangle():
	triangle_coord = [wid(0),hei(0),wid(x_max/2),wid(0),wid(x_max),hei(0),wid(0),hei(0)]
	triangle = canvas.create_line(triangle_coord)

# https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines
count=0
def loop():
	global count
	

	count+=1
	if count<100:
		root.after(0,loop)

print(width*math.sqrt(3)/2)
print(round(width*math.sqrt(3)/2))
draw_triangle()
loop()
root.mainloop()