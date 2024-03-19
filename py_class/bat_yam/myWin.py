from tkinter import *
#----------- משתנים גלובליים:--------------------

#------------פונקציות:--------------------------

#--------------החלון שלי:--------------------
window=Tk()

window.title("Input Window")

window.geometry("400x500+400+100")

window.configure(bg="purple")

helloLbl = Label(window,text="Hello User !",font="4",bg="light green")
helloLbl.place(x=160,y=0)

pleaseStr=Label(window,text="please enter your name:",font="4",bg="light green")
pleaseStr.place(x=106,y=30)

userName=Entry(window)
userName.pack(pady=60)

myBtn=Button(window,text="Click here to change the Label!")
myBtn.place(x=106,y=80)

window.mainloop()