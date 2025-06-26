#draw line
from tkinter import *
root=Tk()
c=Canvas(root,width=600,height=500)
c.pack()
c.create_line(0,0,600,500,width=5,fill="red",dash=(3,3))
c.create_rectangle(150,425,450,375,fill="yellow",outline="blue",width=5)
root.mainloop()

#create oval
from tkinter import *
root=Tk()
c=Canvas(root,width=600,height=500)
c.pack()
c.create_oval(70,120,300,150,fill="red",outline="black", width=4)
root.mainloop()

#create arc
from tkinter import *
root=Tk()
c=Canvas(root,width=600,height=400)
c.pack()
c.create_arc(0,150,250,0,width=6,fill="pink", outline="blue")
root.mainloop()

#create circle
from tkinter import *
root=Tk()
c=Canvas(root,width=600,height=500)
c.pack()
c.create_oval(120, 50, 220, 150,fill="pink",outline="blue",width=3)
root.mainloop()

#create square
from tkinter import *
root=Tk()
c=Canvas(root,width=600,height=500)
c.pack()
c.create_rectangle(150,450,450,150,fill="skyblue",outline="blue",width=4)
root.mainloop()
