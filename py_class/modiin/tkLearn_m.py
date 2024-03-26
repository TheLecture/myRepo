from tkinter import *

app = Tk() # יצירת אובייקת בשם אפפ שיחזיק את החלון שיוצרת הפונקציה טי-קיי

app.title("My First Window !")# הגדרת גותרת לחלון שלנו
app.geometry("270x400+500+100")# הגדרת גודל החלון(רוחב ואורך) ומיקומו על ציר איקס וווי
app.configure(bg="light green")# פונקציה שמאפשרת שינוי נראות של החלון כמו צבע וכו


myLbl1 = Label(app,text="Here is my first label !!",background="light blue",font=6,fg="red",underline=0)
                                  # יצירת אובייקט המכיל תווית טקסט בעלת הגדרות נוספות כמו צבע, גודל וכו'
myLbl1.pack()   # זימון ומיקום של אובייקט התווית שלנו על גבי החלון

app.mainloop() # הפעלה של החלון שלי באמצות בפונצקיה מייןלופ