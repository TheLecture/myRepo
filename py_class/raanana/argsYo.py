def myfunc(*args):
    total = 0
    counter = 0
    strlst=[]
    if len(args)>=8:
        for arg in args:
            if type(arg)== int:
                total+=arg
                counter+=1
            elif type(arg)== str:
                strlst.append(arg)
            else:
                return "i expect to get an int or a str !"
        return total/counter, ' '.join(strlst)
    else:
        return  "i expect to get at list 8 params..." 
   

my_list = ["A","B",1,2,"C",3,4,"D"]   
print(myfunc(*my_list))