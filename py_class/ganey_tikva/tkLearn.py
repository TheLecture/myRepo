from tkinter import *

num = 0

#-----------------פונקציות:-----------------------

def whenClicked():
    print("You clicked the sec button !")
 
def whenClicked2():
    num=int(numToConvert.get())
    numLabel.config(text=f"Num: {num}")
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



numToConvert = Entry(window,border=7,font=5)
numToConvert.pack()


numLabel = Label(window, text=num)
numLabel.pack()

stamLabael=Label(text="im here")
stamLabael.place(x=0,y=0)


myBtn2 = Button(window,text="my sec btn",command=whenClicked)
myBtn2.pack(pady=50)


myBtn3 = Button(window,text="click Here!",command=whenClicked2)
myBtn3.pack(pady=50)


window.mainloop()



