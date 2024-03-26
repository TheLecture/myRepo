def calculator():#operation_perform הפונקציה הראשית שלנו - תריץ את המחשבון, תבצע את הקלט ותבצע השמה בתוך הפונקציה
    print("Hello, Welcome to my simple calculator")
    num1 = float(input("please enter your first number:\n"))
    operator = input("please enter an operator(+,-,/,*,**):\n")
    num2 = float(input("please enter your another number:\n"))
    result = operation_perform(num1,num2,operator)# קריאה לפונקציה והשמה של המשתנים שלקטנו אל תוך הפונקציה operation_perform 
    print(f"result is: {num1} {operator} {num2} = {result}") # ביצוע הדפסה של מלל יחד עם המשתנים שלנו :


def operation_perform(num1,num2,operator):# פונקציה אשר בודקת את האופרטור שנקלט ולפיו מחזירה את התשובה של התרגיל החשבוני .
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            print("you cant split to 0, try agian...\n")
    elif operator == '*':
        return num1 * num2
    elif operator == '**':
        return num1**num2
    else:
        print("you did somthing wrong, try agian...\n")
        
               
calculator()# קריאה לפונקציה כדי להפעיל את המחשבון ולהתחיל לבצע קלט .

    
    