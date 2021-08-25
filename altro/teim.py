from Tkinter import *
window = Tk()
window.title("Timer")
num = 1

frame = Frame(window, width=100, height=100)

e=Entry(window)

def STOP():
    global num
    stampa= str(num)+ ".  "+e.get()
    Label(window, text = stampa).grid(row=(1+num),column=0)
    num += 1
    e.delete(0, 'end')



but_stop=Button(window, text="***STOP***", command=STOP)
but_stop.grid(row=0,column=0)

frame.bind("<Return>", STOP())

e.grid(row = 0, column=1)



mainloop()
