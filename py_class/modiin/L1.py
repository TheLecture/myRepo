# #------------------------------------נתיב הקובץ------------------------------
# myfile = open("C:\\Users\\RafiL\\OneDrive\\Desktop\\py_class\\modiin\\text.txt","a+") # פתיחה של קובץ במוד a+

# myfile.writelines(["Alex\n","Rachel\n","Ross\n","Joey\n","Chandler\n"]) # ביצוע כתיבה לקובץ
# myfile.close()

#------------------------------------נתיב הקובץ------------------------------ 

myfile = open("C:\\Users\\RafiL\\OneDrive\\Desktop\\py_class\\modiin\\text.txt","r") # פתיחה של קובץ במוד r

def count(file):
    counter = 0
    lines = file.readlines()
    for line in lines:
        counter+=1
    return counter

print(count(myfile))

myfile.close()




