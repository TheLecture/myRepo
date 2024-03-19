myList = [(1,2),(3,4),(5,2),(7,8),(9,10)]


res_list = list(filter(lambda tup:tup[1]%3==0,myList))

print(res_list)
        
        






#----------------Q2:-------------------

name_list= []
for i in range(5):
    name_list.append(input("please enter a name:\n"))
# name_list= ["Rafi","Moshe","yair","tal","Oz"]

new_list = list(filter(lambda name:name if name[0].isupper() else None,name_list))

print(new_list)




        
    