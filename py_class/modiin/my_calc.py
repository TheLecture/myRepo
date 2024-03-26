def mycalc():
    print("Hello, wellcome to my simple calculator :)")
    firstNum = float(input("please enter a number\n"))
    operator = input("please enter an operator(+,-,/,*,**)\n")
    secNum = float(input("please enter another number\n"))
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