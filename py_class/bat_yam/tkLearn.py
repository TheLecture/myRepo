from tkinter import *

num = 0

#-----------------פונקציות:-----------------------

def whenClicked():
    print("You clicked the sec button !")
 
def whenClicked2():
    num=int(numToConvert.get())
    numLabel.config(text=num)
    return num

#-------------תחילת יצירת החלון:-----------------

window = Tk()

window.title("my window")

window.geometry("400x400+400+100")

window.configure(bg="black")

myString =Label(window,text="That is my first label",bg="light green") 

myString.pack(pady=30)


myBtn = Button(window,text="my first btn", command=lambda: print("You clicked the first button"))
myBtn.pack(side=("bottom"))



numToConvert = Entry(window)
numToConvert.pack()


numLabel = Label(window, text=num)
numLabel.pack()


myBtn2 = Button(window,text="my sec btn",command=whenClicked)
myBtn2.pack(pady=50)


myBtn3 = Button(window,text="click Here!",command=whenClicked2)
myBtn3.pack(pady=50)

myBtn4 = Button(window,text="click Here!",command=whenClicked2)
myBtn3.pack(pady=50)

txt = Text(window)
txt.pack(pady=50)


window.mainloop()



