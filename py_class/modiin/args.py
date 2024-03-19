def myfunc(*args): 
    if len(args)>=8:
        total = 0
        counter = 0
        str_list = []
        for arg in args:
            if type(arg)==int:
                counter+=1
                total+=arg
            elif type(arg)==str:
                str_list.append(arg)
            else:
                return "wrong type of argument ."
        finalStr =' '.join(str_list)
        return finalStr,(total/counter)
    else:
        return "i expect to get at list 8 params..."



list1 = [1,"$",3,"*",5,"s",7,"y",9,"k"] 
        
print(myfunc(*list1)) # תביא לי את הערכים שיש בתוך ליסט 1 ולא את ליסט אחד עצמו .


