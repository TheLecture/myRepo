#-------------------Q1 ZIP----------------------------------
def my_func(list1,list2): #    יצירת הפונקציה שמקבלת 2 פרמפטרים 
    new_list = []          #       יצירת רשימה חדשה שתחזיק את המכפלות
    for num1,num2 in zip(list1,list2): # ביצוע לולאה על 
        new_list.append(num1*num2)
        
    return new_list













#--------------------Q2 JOIN-------------------------

def strTogether(string_list,sign):
    newstr = ""
    if len(string_list)==0:
        return " the list is empty  ."
    else:
        for item in string_list:
            if len(item)>=3:
                newstr = sign.join(string_list)
            
    if len(newstr)==0:
        return " Eror:no string with sufficient length" 
    else:       
        return newstr


print(strTogether(["R","Me","tl","Ik","k"],'-'))

















listt = [1,2,3,4,3,10]
listttt = [5,6,7,8,10,2]

print(my_func(listt,listttt))