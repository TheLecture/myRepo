from tkinter import *

window = Tk()
window.title("My 1st Window")
window.geometry("300x500+500+100")
window.configure(bg="light blue")

myLbl = Label(window,text="My First Label !",font=6,bg="red")
myLbl.pack(pady=30)

myLbl2 = Label(window,text="My Sec Label !!!!!!",bg="green",)
myLbl2.pack()

myBtn = Button(window,text="Don`t Click Here",bg="yellow")
myBtn.pack(pady=15)


window.mainloop()