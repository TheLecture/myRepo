def my_func(*args):
    counter = 0
    total = 0
    all_strings=[]
    if len(args)>=8:
        for arg in args:
                if type(arg)== int:
                    counter+=1
                    total+=arg
                else:
                    all_strings.append(str(arg))
    else:
        print("you need to enter at least 8 arguments .")
    print(total/counter)
    print(" ".join(all_strings))
    
    
    
    
my_list = ["A","B",1,2,"C",3,4,"D"]   
my_func(*my_list)