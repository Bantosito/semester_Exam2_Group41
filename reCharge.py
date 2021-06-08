#This part of code handles the graphical user interface of the program as well as
# handles the logic of the whole program as appMain.py only consists of loose functions.
#reCharges functions are demonstrative and based on a premade data, that requires rework and updates to be more precised.
#Any inconsistencies with the actual data are due to the lack of detailed data on some chargers, and charging points.

#Created by group 41
#last change 08.06.2021

import tkinter as tk # Standard library used to create the
from PIL import Image, ImageTk #Standard library used to load the image into the
import appMain #import the logic of the main app

myColor = "#3DD393" #hexadecimal notation of a color

#Function that after pressing th show map function executes filtering function than plots the graph with the appropriate data.
def openMap():
    appMain.chargerCompanySort(var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get())
    appMain.chargerFunctionSort(var7.get(),var8.get(),var9.get(),var10.get(),var11.get())
    appMain.plotChargersMap()

#function used to activate and desactivte buttons on the left side (show all soperators)
def checkButtonStateChange():
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



#Graphical interface of the program
window = tk.Tk()
window.title("reCharge") #set the program title

canvas = tk.Canvas(width=600, height=300, bg="#3DD393") #background
canvas.grid(columnspan=6,rowspan=6) #create a grid

#above part handles the background picture.
background = Image.open('background.png')
background = ImageTk.PhotoImage(background)
canvas.background = background
bg = canvas.create_image(0, 0, anchor=tk.NW, image=background)

#Create a show map button 
mapShowText = tk.StringVar()
showMapButton = tk.Button(textvariable=mapShowText, command=lambda:openMap(), width = 17, background= myColor )
mapShowText.set("Show Map")
showMapButton.grid(column= 1, row = 5, sticky= 'en')


#Code below is  used to draw the checkboxes
var1 = tk.IntVar()
checkbuton=  tk.Checkbutton(window,text="Show chargers of all operators", variable=var1,background=myColor, command=lambda:checkButtonStateChange())
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
tk.Checkbutton(window,text="Show CHAdeMO chargers", variable=var7,background=myColor).grid(row=0, column= 5, sticky= 'w')

var8 = tk.IntVar()
tk.Checkbutton(window,text="Show ccs2", variable=var8,background=myColor).grid(row=1, column=5, sticky= 'w')

var9 = tk.IntVar()
tk.Checkbutton(window,text="Show type 2 combo", variable=var9,background=myColor).grid(row=2, column= 5, sticky= 'w')

var10 = tk.IntVar()
tk.Checkbutton(window,text="Stations with more than 2 spots", variable=var10,background=myColor).grid(row=3, column= 5, sticky= 'w')

var11 = tk.IntVar()
tk.Checkbutton(window,text="Show opened 24/7", variable=var11,background=myColor).grid(row=4, column= 5, sticky= 'w')

window.mainloop()