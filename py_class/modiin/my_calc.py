def mycalc():
    print("Hello, wellcome to my simple calculator :)")
    firstNum = float(input("please......."))
    operator = input("please......operator(+,-,/,*,**)")
    secNum = float(input("please...2nd.."))
    result = operation_perform(firstNum,operator,secNum)  
    
    print(result)  
    

                    
def operation_perform(num1,oprt,num2):
    if oprt == '+':
        return num1+num2
    elif oprt == '-':
        return num1-num2
    elif oprt == '*':
        return num1*num2
    elif oprt == '/':
        if num2 == 0:
            return " you cant split with 0"
        else: 
            return num1/num2
    elif oprt == '**':
       return num1**num2 
    else:
        return "invalid operator !, try agian . "
        
    


mycalc()