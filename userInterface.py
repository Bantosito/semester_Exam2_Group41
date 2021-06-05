import tkinter as tk
from tkinter.constants import BOTTOM, CHECKBUTTON, RIGHT, YES

from matplotlib.pyplot import fill, get
from PIL import Image, ImageTk 
from numpy import right_shift
#import appMain
myColor = "#3DD393"

def openMap():
    print("var1",var1.get(),"var2",var2.get())

def zupa():
    print("select")
    if var1.get() == 1:
        cleverCheck.config(state="disabled")
        teslaCheck.config(state='disabled')
        ionityCheck.config(state='disabled')
        spertoCheck.config(state='disabled')
        eonCheck.config(state="disabled")
    else:
        cleverCheck.config(state="normal")
        teslaCheck.config(state="normal")
        ionityCheck.config(state="normal")
        spertoCheck.config(state="normal")
        eonCheck.config(state="normal")

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
checkbuton=  tk.Checkbutton(window,text="Show all chargers providers", variable=var1,background=myColor, command=lambda:zupa())
checkbuton.grid(row=0,column=0, sticky= 'w')
checkbuton.select()
var2 = tk.IntVar()
cleverCheck = tk.Checkbutton(window,text="Show Clever chargers",state="disabled", variable=var2,background=myColor,)
cleverCheck.grid(row=1, sticky= 'w')
var3 = tk.IntVar()
teslaCheck = tk.Checkbutton(window,text="Show Tesla chargers",state="disabled", variable=var3,background=myColor)
teslaCheck.grid(row=2, sticky= 'w')
var4 = tk.IntVar()
ionityCheck=tk.Checkbutton(window,text="Show Ionity chargers", state="disabled",variable=var4,background=myColor)
ionityCheck.grid(row=3, sticky= 'w')
var5 = tk.IntVar()
spertoCheck=tk.Checkbutton(window,text="Show Sperto chargers", state="disabled",variable=var5,background=myColor)
spertoCheck.grid(row=4, sticky= 'w')
var6 = tk.IntVar()
eonCheck = tk.Checkbutton(window,text="Show E-on chargers",state="disabled", variable=var6,background=myColor)
eonCheck.grid(row=5, sticky= 'w')
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

