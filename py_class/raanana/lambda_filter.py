list1=[(1,2),(3,15),(5,6),(7,8),(9,12)]

split_three=list(filter(lambda tup:tup if tup[1]%3==0 else None,list1))

print(split_three)