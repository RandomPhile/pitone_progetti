import tkinter

window = tkinter.Tk()
# to rename the title of the window
window.title("FINESTRA")
# pack is used to show the object in the window
label = tkinter.Label(window, text = "Questa finestra e stata creata con tkinter").pack()
window.mainloop()
