list1 = [1,2,3,4,5,6]
list2 = [7,8,9,10,11,12]

def sum_nums(num1,num2):
    return num1+num2

list3=list(map(sum_nums,list1,list2))


phonesList=[input("please enter phone number") for i in range(5)]
   
def lastFour(phonNum):
    return phonNum[-4:]

justFour = list(map(lastFour,phonesList))

print(justFour)
