from tkinter import *

userName = "User"
def changeName():
    userName= entrySpace.get()
    helloLbl.config(text=f"Hello {userName} !")
    
root=Tk()
root.title("My Win")
root.geometry("500x500+200+100")

helloLbl = Label(root,text=f"Hello {userName} !")
helloLbl.pack(pady=15)

secLbl= Label(root,text="please inser your first name: ")
secLbl.pack(pady=5)

entrySpace= Entry(root,font=7,bd=4)
entrySpace.pack(pady=3)

mybtn = Button(root,text="Insert Name !",command=changeName)
mybtn.pack()
root.mainloop()