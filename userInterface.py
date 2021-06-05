import tkinter as tk
from tkinter.constants import BOTTOM, CHECKBUTTON, RIGHT, YES

from matplotlib.pyplot import fill, get
from PIL import Image, ImageTk 
from numpy import right_shift
#import appMain
myColor = "#3DD393"

def openMap():
    print("var1",var1.get())

def zupa():
    print("select")
   
window = tk.Tk()
window.title("reCharge")



canvas = tk.Canvas(width=600, height=300, bg="#3DD393")
canvas.grid(columnspan=6,rowspan=6)

background = Image.open('background.png')
background = ImageTk.PhotoImage(background)
canvas.background = background
bg = canvas.create_image(0, 0, anchor=tk.NW, image=background)


mapShowText = tk.StringVar()
showMapButton = tk.Button(textvariable=mapShowText, command=lambda:openMap(), width = 17, background= myColor )
mapShowText.set("Show Map")
showMapButton.grid(column= 1, row = 5, sticky= 'en')

var1 = tk.IntVar()
tk.Checkbutton(window,text="Show all chargers", variable=var1,background=myColor, command=lambda:zupa()).grid(row=0,column=0, sticky= 'w')

var2 = tk.IntVar()
tk.Checkbutton(window,text="Show Clever chargers", variable=var2,background=myColor,).grid(row=1, sticky= 'w')

var3 = tk.IntVar()
tk.Checkbutton(window,text="Show Tesla chargers", variable=var3,background=myColor).grid(row=2, sticky= 'w')

var4 = tk.IntVar()
tk.Checkbutton(window,text="Show Ionity chargers", variable=var4,background=myColor).grid(row=3, sticky= 'w')

var5 = tk.IntVar()
tk.Checkbutton(window,text="Show Sperto chargers", variable=var5,background=myColor).grid(row=4, sticky= 'w')

var6 = tk.IntVar()
tk.Checkbutton(window,text="Show E-on chargers", variable=var6,background=myColor).grid(row=5, sticky= 'w')

var7 = tk.IntVar()
tk.Checkbutton(window,text="Show E-on chargers", variable=var7,background=myColor).grid(row=0, column= 5, sticky= 'w')

var8 = tk.IntVar()
tk.Checkbutton(window,text="Show E-on chargers", variable=var8,background=myColor).grid(row=1, column=5, sticky= 'w')

var9 = tk.IntVar()
tk.Checkbutton(window,text="Show E-on chargers", variable=var9,background=myColor).grid(row=2, column= 5, sticky= 'w')

var10 = tk.IntVar()
tk.Checkbutton(window,text="Show E-on chargers", variable=var10,background=myColor).grid(row=3, column= 5, sticky= 'w')

var11 = tk.IntVar()
tk.Checkbutton(window,text="Show E-on chargers", variable=var11,background=myColor).grid(row=4, column= 5, sticky= 'w')

var12 = tk.IntVar()
tk.Checkbutton(window,text="Show E-on chargers", variable=var12,background=myColor).grid(row=5,column=5, sticky= 'w')

window.mainloop()

